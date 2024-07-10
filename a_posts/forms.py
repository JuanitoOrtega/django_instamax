from .models import *
from django.forms import ModelForm
from django import forms


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url', 'body', 'tags']
        labels = {
            'body': 'Caption',
            'tags': 'Category',
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption...', 'class': 'font1 text-4xl'}),
            'url': forms.TextInput(attrs={'placeholder': 'Añadir URL...'}),
            'tags': forms.CheckboxSelectMultiple(),
        }


class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'tags']
        labels = {
            'body' : '',
            'tags' : 'Category'
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'class': 'font1 text-4xl'}),
            'tags' : forms.CheckboxSelectMultiple(),
        }


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder': 'Añadir comentario...'})
        }
        labels = {
            'body': ''
        }
        
        
class ReplyCreateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder': 'Añadir respuesta...', 'class': "!text-sm"})
        }
        labels = {
            'body': ''
        }