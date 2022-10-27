from socket import fromshare
from django import forms
from core.models import Post
from users.models import User


class EmailForm(forms.Form):
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea)


class PostCreateForm(forms.ModelForm):
    def __init__(self, *args, user:User, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Post
        fields = ['title', 'text']

    def save(self, commit: bool = ...):
        post =  super().save(False)
        post.user = self.user
        if commit:
            post.save()
        return post





class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']