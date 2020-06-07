from django import forms
from store.models import Size, Pizza


class PizzaForm(forms.ModelForm):
    pizz = forms.ModelChoiceField(queryset=Pizza.objects.all().order_by('title'), required=True, label=None,
                                initial=Pizza.objects.all().order_by('title').first(), help_text='Choose your destiny')
    size = forms.ChoiceField(choices=Size.SIZE_OPTIONS)
    quantity = forms.IntegerField(widget=forms.NumberInput(), min_value=1, required=True, initial=1)
    address = forms.CharField(max_length=64)
    phone = forms.CharField(max_length=15)
    comments = forms.CharField(max_length=100)

    class Meta:
        model = Pizza
        fields = ['id', ]

