from django import forms
from .models import *
import os

class my_imageFile(forms.widgets.FileInput):
    template_name = 'main/widgets_imageFile.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['nameFile'] = 'static/main/images/photo.png'
        if (value is not None):
            try:
                if os.path.isfile(value.path):
                    context['widget']['nameFile'] = value.url
            except:
                pass
        return context   

class spr_defaultForm(forms.ModelForm):
    guid_update = forms.UUIDField(widget=forms.widgets.HiddenInput(), required=False)
    owner_old = forms.CharField(widget=forms.widgets.HiddenInput(), required=False)
    parent_old = forms.CharField(widget=forms.widgets.HiddenInput(), required=False)
    deleted = forms.BooleanField(widget=forms.widgets.HiddenInput(), required=False)

    code = forms.CharField(widget=forms.TextInput(), disabled=True,label = 'Код',required=False)    

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user') if ('user' in kwargs) else None
        owner_old = kwargs.pop('owner_old') if ('owner_old' in kwargs) else None
        parent_old = kwargs.pop('parent_old') if ('parent_old' in kwargs) else None

        super(spr_defaultForm,self).__init__(*args, **kwargs)
        if (self.instance):
            self.fields['owner_old'].initial = owner_old
            self.fields['parent_old'].initial = parent_old

    def clean_parent(self):
        data = self.cleaned_data['parent']
        if (data):
            if (data == self.instance):
                raise forms.ValidationError('Не допуcтимое значение подгруппы')   
        return data


class spr_companyForm(spr_defaultForm):

    type_company = forms.ChoiceField(choices=spr_company.TYPE,label='Вид организации:',widget=forms.Select(attrs={'class': 'form-select'})) 
    parent = forms.ModelChoiceField(queryset=spr_company.objects.all(), required=False, label='Головная организация:', widget=forms.Select(attrs={'class': 'form-select'}))
    name = forms.CharField(max_length=50, label='Наименование:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    name_full = forms.CharField(max_length=250, label='Полное наименование:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    inn = forms.CharField(max_length=12, label='ИНН:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    kpp = forms.CharField(max_length=9, label='КПП:', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    addres_u = forms.CharField(max_length=250, label='Юридический адрес:', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'autocomplete': 'off'}))
    addres_f = forms.CharField(max_length=250, label='Фактический адрес:', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'autocomplete': 'off'}))
    addres_p = forms.CharField(max_length=250, label='Почтовый адрес:', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'autocomplete': 'off'}))
    pref = forms.CharField(max_length=2, label='Префикс:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'title': 'Префикс'}))

    class Meta:
        model = spr_company
        exclude = ['reg_global'] 

    def clean_parent(self):
        parent = self.cleaned_data['parent']
        if (int(self.cleaned_data['type_company']) != 1):
            parent = None
        else:
            if (parent == None):
                raise forms.ValidationError("Не указана головная организация") 
            elif (parent == self.instance):
                raise forms.ValidationError("Не допустимое значение головной организации") 

        return parent   

    def __init__(self, *args, **kwargs):
        super(spr_companyForm,self).__init__(*args, **kwargs)
        if (self.instance):
            self.fields['parent'].queryset = spr_company.objects.filter(reg_global=self.user.reg_global, deleted=False, parent__isnull=True)
 

class spr_doljnostyForm(spr_defaultForm):
    class Meta:
        model = spr_doljnosty
        exclude = ['reg_global']


class spr_fizlitsoForm(spr_defaultForm):
    DateOfBirth = forms.DateField(label='Дата рождения',required=False,widget=forms.DateInput(format=('%Y-%m-%d'),attrs={'type': 'date'}))
    imageFile = forms.ImageField(label='Фото', widget=my_imageFile(attrs={'style': 'display:none'}), required=False)
    del_imageFile = forms.BooleanField(initial= False, required=False)

    class Meta:
        model = spr_fizlitso
        exclude = ['reg_global', 'name'] 

    #def clean_imageFile(self):
    #    data = self.cleaned_data['imageFile']
    #    return data

    def clean(self):
        cleaned_data = super(spr_fizlitsoForm, self).clean()
        if ('del_imageFile' in cleaned_data):
            if (cleaned_data['del_imageFile']):
                cleaned_data['imageFile'] = False

        imageFile = cleaned_data['imageFile']

        if (((imageFile == False) or (imageFile != self.instance.imageFile)) and self.instance.imageFile):
            if os.path.isfile(self.instance.imageFile.path):
                self.instance.imageFile.delete(False)   



class spr_nomenklaturaForm(spr_defaultForm):
    TYPE_nomenklatura = (
        (0, "Товар"),
        (1, "Услуга"),
        ) 

    name = forms.CharField(max_length=50, label='Наименование:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'spellcheck': 'false'}))
    type_nomenklatura = forms.ChoiceField(choices=TYPE_nomenklatura, label='Вид номенклатуры')

    def clean_unit(self):
        data = self.cleaned_data['unit']
        if (not data):
            raise forms.ValidationError("Не указана единица измерения")        
        return data

    class Meta:
        model = spr_nomenklatura
        exclude = ['reg_global', 'code']             

    def __init__(self, *args, **kwargs):
        super(spr_nomenklaturaForm,self).__init__(*args, **kwargs)
        if (self.instance):
            self.fields['parent'].queryset = spr_nomenklatura.objects.filter(Q(reg_global=self.user.reg_global),Q(group = True)) 


class spr_nomenklaturaForm_gr(spr_defaultForm):
    name = forms.CharField(max_length=50, label='Наименование:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'spellcheck': 'false'}))
    parent = forms.ModelChoiceField(queryset=spr_nomenklatura.objects.all(), required=False, label='Подгруппа:', widget=forms.Select())
    group = forms.BooleanField(widget=forms.widgets.HiddenInput(), required=False)

    class Meta:
        model = spr_nomenklatura
        exclude = ['reg_global', 'code', 'unit', 'alco', 'marked', 'type_nomenklatura']  

    def __init__(self, *args, **kwargs):
        super(spr_nomenklaturaForm_gr,self).__init__(*args, **kwargs)
        if (self.instance):
            self.fields['group'].initial = True
            self.fields['parent'].queryset = spr_nomenklatura.objects.filter(Q(reg_global=self.user.reg_global),Q(group = True)) 



class spr_objectForm(spr_defaultForm):
    owner = forms.ModelChoiceField(queryset=spr_company.objects.all(), label='Организация:', empty_label=None, widget=forms.Select(attrs={'class': 'form-select'}))
    name = forms.CharField(max_length=50, label='Наименование:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'spellcheck': 'false'}))

    tabl_spr_typemenu = forms.ModelMultipleChoiceField(queryset=spr_typemenu.objects.all(), required=False,widget=forms.CheckboxSelectMultiple)
    tabl_spr_zaly = forms.ModelMultipleChoiceField(queryset=spr_zaly.objects.all(), required=False,widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = spr_object
        exclude = ['reg_global'] 
     
    def __init__(self, *args, **kwargs):
        super(spr_objectForm,self).__init__(*args, **kwargs)
        if (self.instance):
            self.fields['owner'].queryset = spr_company.objects.filter(reg_global=self.user.reg_global)
            self.fields['tabl_spr_typemenu'].queryset = spr_typemenu.objects.filter(reg_global=self.user.reg_global, deleted=False)
            self.fields['tabl_spr_zaly'].queryset = spr_zaly.objects.filter(reg_global=self.user.reg_global, deleted=False) 


class spr_object_usersForm(spr_defaultForm):
    tabl_spr_role = forms.ModelMultipleChoiceField(queryset=spr_role.objects.all(), required=False,widget=forms.CheckboxSelectMultiple)    
    doljnost = forms.ModelChoiceField(queryset=spr_doljnosty.objects.all(), label='Должность:', widget=forms.Select())
    class Meta:
        model = spr_object_users
        exclude = ['reg_global'] 
    def __init__(self, *args, **kwargs):
        super(spr_object_usersForm,self).__init__(*args, **kwargs)
        if (self.instance):
            self.fields['owner'].queryset = spr_object.objects.filter(reg_global=self.user.reg_global)
            self.fields['tabl_spr_role'].queryset = spr_role.objects.filter(reg_global=self.user.reg_global, deleted=False)               
            self.fields['doljnost'].queryset = spr_doljnosty.objects.filter(reg_global=self.user.reg_global, deleted=False)


class spr_object_usersForm_el(spr_defaultForm):
    tabl_spr_role = forms.ModelMultipleChoiceField(queryset=spr_role.objects.all(), label='Роли:', required=False,widget=forms.CheckboxSelectMultiple)    
    doljnost = forms.ModelChoiceField(queryset=spr_doljnosty.objects.all(), label='Должность:', widget=forms.Select())
    fizlitso = forms.ModelChoiceField(queryset=spr_fizlitso.objects.all(), label='Физическое лицо:', widget=forms.Select())
    class Meta:
        model = spr_object_users
        exclude = ['reg_global']   

    def __init__(self, *args, **kwargs):
        super(spr_object_usersForm_el,self).__init__(*args, **kwargs)
        if (self.instance):
            self.fields['tabl_spr_role'].queryset = spr_role.objects.filter(reg_global=self.user.reg_global, deleted=False)               
            self.fields['doljnost'].queryset = spr_doljnosty.objects.filter(reg_global=self.user.reg_global, deleted=False)
            self.fields['fizlitso'].queryset = spr_fizlitso.objects.filter(reg_global=self.user.reg_global, deleted=False)


class spr_roleForm(spr_defaultForm):
    name = forms.CharField(max_length=50, label='Наименование:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'spellcheck': 'false'}))
    class Meta:
        model = spr_role
        exclude = ['reg_global', 'code'] 


class spr_statiyzatratForm(spr_defaultForm):
    name = forms.CharField(max_length=50, label='Наименование:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'spellcheck': 'false'}))

    class Meta:
        model = spr_statiyzatrat
        exclude = ['reg_global',]  


class spr_typemenuForm(spr_defaultForm):
    class Meta:
        model = spr_typemenu
        exclude = ['reg_global']               


class spr_unitsForm(spr_defaultForm):
    name = forms.CharField(max_length=50, label='Наименование:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'spellcheck': 'false'}))
    class Meta:
        model = spr_units
        exclude = ['reg_global', 'code']     


class spr_variantoplatyForm(spr_defaultForm):
    name = forms.CharField(max_length=50, label='Наименование:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'spellcheck': 'false'}))
    tabl_spr_statiyzatrat = forms.ModelMultipleChoiceField(queryset=spr_statiyzatrat.objects.all(), label='Статьи затрат:', required=False,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = spr_variantoplaty
        exclude = ['reg_global', 'code']  

    def __init__(self, *args, **kwargs):
        super(spr_variantoplatyForm,self).__init__(*args, **kwargs)
        if (self.instance):
            self.fields['tabl_spr_statiyzatrat'].queryset = spr_statiyzatrat.objects.filter(reg_global=self.user.reg_global)  


class spr_zalyForm(spr_defaultForm):
    class Meta:
        model = spr_zaly
        exclude = ['reg_global']                      


class spr_priznakdeleteForm(spr_defaultForm):
    class Meta:
        model = spr_priznakdelete
        exclude = ['reg_global']                      


class spr_picturesForm(spr_defaultForm):
    class Meta:
        model = spr_pictures
        exclude = ['reg_global']    


class spr_otdelyForm(spr_defaultForm):
    class Meta:
        model = spr_otdely
        exclude = ['reg_global']   


class spr_stavkandsForm(spr_defaultForm):
    class Meta:
        model = spr_stavkands
        exclude = ['reg_global']  


class spr_categoriesForm(spr_defaultForm):
    class Meta:
        model = spr_categories
        exclude = ['reg_global']  


class spr_grprintForm(spr_defaultForm):
    class Meta:
        model = spr_grprint
        exclude = ['reg_global']   


class spr_menuForm(spr_defaultForm):
    class Meta:
        model = spr_menu
        exclude = ['reg_global']      

class spr_menuForm_gr(spr_defaultForm):
    name = forms.CharField(max_length=50, label='Наименование:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'spellcheck': 'false'}))
    parent = forms.ModelChoiceField(queryset=spr_menu.objects.all(), required=False, label='Подгруппа:', widget=forms.Select())
    group = forms.BooleanField(widget=forms.widgets.HiddenInput(), required=False)

    class Meta:
        model = spr_menu
        exclude = ['reg_global', 'code', 'unit', 'alco', 'marked', 'type_nomenklatura']  

    def __init__(self, *args, **kwargs):
        super(spr_menuForm_gr,self).__init__(*args, **kwargs)
        if (self.instance):
            self.fields['group'].initial = True
            self.fields['parent'].queryset = spr_menu.objects.filter(Q(reg_global=self.user.reg_global),Q(group = True))    

class spr_conditionsForm(spr_defaultForm):
    class Meta:
        model = spr_conditions
        exclude = ['reg_global']                                                


class spr_modificatorsForm(spr_defaultForm):
    class Meta:
        model = spr_modificators
        exclude = ['reg_global']      


class spr_modificatorsForm_gr(spr_defaultForm):
    name = forms.CharField(max_length=50, label='Наименование:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'spellcheck': 'false'}))
    parent = forms.ModelChoiceField(queryset=spr_modificators.objects.all(), required=False, label='Подгруппа:', widget=forms.Select())
    group = forms.BooleanField(widget=forms.widgets.HiddenInput(), required=False)

    class Meta:
        model = spr_modificators
        exclude = ['reg_global']  

    def __init__(self, *args, **kwargs):
        super(spr_modificatorsForm_gr,self).__init__(*args, **kwargs)
        if (self.instance):
            self.fields['group'].initial = True
            self.fields['parent'].queryset = spr_modificators.objects.filter(Q(reg_global=self.user.reg_global),Q(group = True))   