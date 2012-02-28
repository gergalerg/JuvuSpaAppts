from django import forms


class SpaInfoForm(forms.Form):
    spa_name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    city = forms.ChoiceField(
        choices=[('SanFrancisco', 'San Francisco')]
        )
    neighborhood = forms.ChoiceField(
        choices=[
            ('', '---'),
            ('Richmond_Presidio', 'Richmond/Presidio'),
            ('Marina_Cow_Hollow', 'Marina/Cow Hollow'),
            ('Pacific_Heights', 'Pacific Heights'),
            ('Russian_Hill_Nob_Hill', 'Russian Hill/Nob Hill'),
            ('North_Beach_Fishermans_Wharf', "North Beach/Fisherman's Wharf"),
            ('Union_Sq_Civic_Ctr_FiDi', 'Union Sq/Civic Ctr/FiDi'),
            ('SoMa_South_Beach', 'SoMa/South Beach'),
            ('Western_Addition', 'Western Addition'),
            ('Haight', 'Haight'),
            ('Castro', 'Castro'),
            ('Mission', 'Mission'),
            ('Potrero_Hill', 'Potrero Hill'),
            ('Noe_Valley', 'Noe Valley'),
            ('Bernal_Heights', 'Bernal Heights'),
            ('Twin_Peaks', 'Twin Peaks'),
            ('Sunset_Lake_Merced', 'Sunset/Lake Merced'),
            ('Ingleside_Excelsior', 'Ingleside/Excelsior'),
            ]
        )
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
