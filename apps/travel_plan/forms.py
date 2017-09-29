from datetime import date
from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import *

User = get_user_model()


class TravelPlanForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(format="%m/%d/%Y",
                                                        attrs={'class': 'form-control',
                                                               'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(format="%m/%d/%Y",
                                                      attrs={'class': 'form-control',
                                                             'type': 'date'}))

    class Meta:
        model = TravelPlan
        fields = ('destination', 'desc', 'start_date', 'end_date')

    def clean(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if start_date < datetime.date.today() or end_date < datetime.date.today():
            raise forms.ValidationError('The date cannot be in the past')
        if start_date > end_date:
            raise forms.ValidationError('Something wrong with your start/end date')
        return super(TravelPlanForm, self).clean()

# class BookForm(forms.ModelForm):

#     class Meta:
#         model = Book
#         fields = ('title',)


# class AuthorForm(forms.ModelForm):
#     first_name = forms.CharField(required=False)
#     last_name = forms.CharField(required=False)

#     class Meta:
#         model = Author
#         fields = ('first_name', 'last_name')
#         widgets = {
#             'first_name': forms.TextInput(attrs={'placeholder': 'first name'}),
#             'last_name': forms.TextInput(attrs={'placeholder': 'last name'})
#         }


# class SelectAuthorForm(forms.Form):
#     choose_author = forms.ModelChoiceField(queryset=Author.objects.all().order_by('first_name'),
#                                            label='Select an author',
#                                            required=False)


# class ReviewForm(forms.ModelForm):
#     rating = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])

#     class Meta:
#         model = Review
#         fields = ('comment', 'rating')
#         widgets = {
#             'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
#         }

