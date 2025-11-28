from django import forms

class InputForm(forms.Form): # forms.Form is a class from Django.forms module 
    name = forms.CharField(max_length=3)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput()) 


#-------SignUp--------

class SignupForm(forms.Form):
    username= forms.CharField(max_length=3)
    email= forms.EmailField()
    password= forms.CharField(widget=forms.PasswordInput())

#-------SignUp with ModelForm--------

from .models import User
class SignupForm1(forms.ModelForm): # ModelForm is used to create form based on model
    class Meta:
        model = User
        fields = "__all__"

#-------Blog Post Form with ModelForm--------

from .models import Blogpost
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = "__all__"