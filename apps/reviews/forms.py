from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import *


User = get_user_model()


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title',)


class AuthorForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = Author
        fields = ('first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last name'})
        }


class SelectAuthorForm(forms.Form):
    choose_author = forms.ModelChoiceField(queryset=Author.objects.all().order_by('first_name'),
                                           label='Select an author',
                                           required=False)


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])

    class Meta:
        model = Review
        fields = ('comment', 'rating')
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }

