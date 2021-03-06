from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta():
        model=Post
        fields=('title','author','text')
        widgets = {
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }



class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('writer','text')
        widgets = {
            'writer': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
