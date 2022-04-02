import code
from django import forms
from .models import *


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

