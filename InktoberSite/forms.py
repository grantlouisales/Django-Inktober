from django import forms

class User(forms.Form):
    fname = forms.CharField(label = "First Name", max_length = 200)
    lname = forms.CharField(label = "Last Name", max_length = 200)
    check_box = forms.BooleanField(required=False)
    