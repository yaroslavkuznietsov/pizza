from django import forms
from store.models import Size, Pizza


class PizzaForm(forms.ModelForm):
    size = forms.ChoiceField(choices=Size.SIZE_OPTIONS)
    quantity = forms.IntegerField(widget=forms.NumberInput(), min_value=1, required=True, initial=1)

    class Meta:
        model = Pizza
        fields = ['id', ]
