from django import forms
from django.forms import ModelForm
from . models import dlogin


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = dlogin
        fields = ['username','password']


class RegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = dlogin
        fields = ['username','password','email','first_name','last_name','dob','gender']


    def clean_username(self):
        username = self.cleaned_data.get('username')
        match = dlogin.objects.filter(username = username)
        if match :
            raise forms.ValidationError('This is username already in use.')
        else:
            return username

     

    def clean_email(self):
        email = self.cleaned_data.get('email')
        match = dlogin.objects.filter(email = email)
        if match :
            raise forms.ValidationError('This is email already in use.')
        else:
            return email

    
        
    
     

class SubscribeForm(ModelForm):
    class Meta:
        model = dlogin
        exclude = ('date_subscribed','messages_received')



#    **----------------------------------------------------------------**



# class PostForm(ModelForm):
#     class Meta :
#         model = Posts
#         fields = ['posts']