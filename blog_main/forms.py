from django import forms
from blog_main.models import Post, PostComment


class PostForm(forms.ModelForm):


    class Meta():
        model = Post
        fields = ['author', 'title', 'text']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = PostComment
        fields = ['author', 'text',]

    widgets = {
        'author': forms.TextInput(attrs = {'class': 'textinputclass'}),
        'text': forms.Textarea(attrs = {'class': 'textinputclass'})

    }
