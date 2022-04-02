from .models import *
from .forms import *

class spr_companyForm(spr_defaultForm):

    type_company = forms.ChoiceField(choices=spr_company.TYPE,label='Вид организации:',widget=forms.Select(attrs={'class': 'form-select'})) 
    parent = forms.ModelChoiceField(queryset=spr_company.objects.all(), required=False, label='Головная организация:', widget=forms.Select(attrs={'class': 'form-select'}))
    name = forms.CharField(max_length=50, label='Наименование:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    name_full = forms.CharField(max_length=250, label='Полное наименование:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    inn = forms.CharField(max_length=12, label='ИНН:', widget=forms.NumberInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    kpp = forms.CharField(max_length=9, label='КПП:', required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    addres_u = forms.CharField(max_length=250, label='Юридический адрес:', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'autocomplete': 'off'}))
    addres_f = forms.CharField(max_length=250, label='Фактический адрес:', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'autocomplete': 'off'}))
    addres_p = forms.CharField(max_length=250, label='Почтовый адрес:', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'autocomplete': 'off'}))
    pref = forms.CharField(max_length=2, label='Префикс:', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))

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
