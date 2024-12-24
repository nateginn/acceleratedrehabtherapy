from django import forms


class MultiSelectFormField(forms.TypedMultipleChoiceField):
    widget = forms.CheckboxSelectMultiple
