from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "<script>" in title:  # Basic XSS protection example
            raise forms.ValidationError("Invalid characters in title!")
        return title

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if "<script>" in name:  # Basic XSS protection example
            raise forms.ValidationError("Invalid characters in name!")
        return name
