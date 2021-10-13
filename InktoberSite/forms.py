from django.forms import ModelForm
from .models import User

# forms.Form
class UserInfo(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
        """
        fname = forms.CharField(label = "First Name", max_length = 200)
        lname = forms.CharField(label = "Last Name", max_length = 200)
        email = forms.EmailField(label = "User Email", max_length = 200)
        prompt_idea = forms.CharField(label = "Prompt Idea", max_length = 200)
        """
