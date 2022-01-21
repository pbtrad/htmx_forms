from django import forms
from django.forms.models import inlineformset_factory
from .models import Author, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title',
            'number_of_pages'
        )


BookFormSet = inlineformset_factory(
    Author,
    Book,
    form=BookForm,
    min_num=2,
    extra=1, 
    can_delete=False
)