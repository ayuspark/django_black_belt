from datetime import date
from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import *

User = get_user_model()


class TravelPlanForm(forms.ModelForm):
    destination = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    desc = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'rows': '3'}),
                           label='Description:',)
    start_date = forms.DateField(widget=forms.DateInput(format="%m/%d/%Y",
                                                        attrs={'class': 'form-control',
                                                               'type': 'date'}),
                                 label='Travel Date From:')
    end_date = forms.DateField(widget=forms.DateInput(format="%m/%d/%Y",
                                                      attrs={'class': 'form-control',
                                                             'type': 'date'}),
                               label='Travel Date To:')

    class Meta:
        model = TravelPlan
        fields = ('destination', 'desc', 'start_date', 'end_date')

    def clean(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if start_date < date.today() or end_date < date.today():
            raise forms.ValidationError('The date cannot be in the past')
        if start_date > end_date:
            raise forms.ValidationError('How can you end before you start?!')
        return super(TravelPlanForm, self).clean()
