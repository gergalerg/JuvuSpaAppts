from django import forms


class SpaInfoForm(forms.Form):
    spa_name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    neighborhood = forms.CharField(max_length=100)
    hours = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    website = forms.URLField(max_length=100)
    email_contact = forms.EmailField()
    pictures = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    cancel_policy = forms.CharField(
        max_length=2000,
        label="Cancellation Policy",
        widget=forms.Textarea,
        )
