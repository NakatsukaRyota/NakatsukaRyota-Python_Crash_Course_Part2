from django import forms

from .models import Blog, Entry


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["text"]
        labels = {"text": ""}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
