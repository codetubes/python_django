from django import forms
from .models import Contact, Comment


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ["blog"]
