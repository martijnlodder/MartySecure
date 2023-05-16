from django import forms

class MFASetupForm(forms.Form):
    mfa_secret = forms.CharField(label='MFA-secret', max_length=16, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
