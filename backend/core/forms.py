from django import forms
from . import models

class TopGroupForm(forms.Form):
    name = forms.CharField(label='Top App Group Name')

class AppAddForm(forms.Form):
    title = forms.CharField(label='Title of app')


class EntityTypeGroupForm(forms.Form):
    name = forms.CharField(label='Group Name')

class EntityTypeStringForm(forms.ModelForm):
    class Meta:
        model = models.EntityTypeString
        fields = ['content']

class EntityTypeTextForm(forms.ModelForm):
    class Meta:
        model = models.EntityTypeText
        fields = ['content']