from django import forms

from person_license.models import Person, License


class PersonForm(forms.ModelForm):
    name = forms.CharField(max_length=45,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter Name'}))
    mobile = forms.CharField(max_length=45,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter Mobile No.'}))

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['mobile'].required = False

    class Meta:
        model = Person
        fields = '__all__'


class LicenseForm(forms.ModelForm):
    license_number = forms.CharField(max_length=45,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control form-control-user',
                                                'placeholder': 'Enter License No.'}))
    issue_date = forms.CharField(max_length=45,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control form-control-user',
                                            'placeholder': 'Enter Issue Date'}))
    expiry_date = forms.CharField(max_length=45,
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control form-control-user',
                                             'placeholder': 'Enter Expiry Date'}))

    class Meta:
        model = License
        fields = '__all__'
