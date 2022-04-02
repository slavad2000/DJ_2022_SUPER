from .models import *
from .forms import *


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
