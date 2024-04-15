from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
   class Meta:
     model = Comment
     fields = ('name', 'email', 'body')


class ContactForm(forms.Form):
    lastname = forms.CharField(max_length=100)
    firstname = forms.CharField(max_length=100)
    birth_day = forms.DateField()
    email = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)
