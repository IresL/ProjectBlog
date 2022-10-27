from django import forms
from users.models import User


class UserCreateForm(forms.ModelForm):
    class Meta:
        model =User
        fields = ['username', 'first_name', 'last_name', 'password']
    
    def save(self, commit: bool = ...):
        user:User =  super().save(commit)
        user.set_password(user.password)
        if commit:
            user.save()
        
        return user