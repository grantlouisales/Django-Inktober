from django import forms

class UserInfo(forms.Form):
    fname = forms.CharField(label = "First Name", max_length = 200)
    lname = forms.CharField(label = "Last Name", max_length = 200)
    email = forms.EmailField(label = "User Email", max_length = 200)
    prompt_idea = forms.CharField(label = "Prompt Idea", max_length = 200)
    check_box = forms.BooleanField(required=False)
    