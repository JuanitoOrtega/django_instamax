from .models import Post
from django.forms import ModelForm
from django import forms


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url', 'body']
        labels = {
            'body': 'Caption',
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption...', 'class': 'font1 text-4xl'}),
            'url': forms.TextInput(attrs={'placeholder': 'Añadir URL...'}),
        }


class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        labels = {
            'body' : '',
            # 'tags' : 'Category'
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'class': 'font1 text-4xl'}),
            # 'tags' : forms.CheckboxSelectMultiple(),
        }