from django import forms

math_operators = (
        ('add', '+'),
        ('sub', '-'),
        ('mult', '*'),
        ('div', '/'),
        )


class Mathcalc(forms.Form):
    num_a = forms.FloatField()
    math_op = forms.ChoiceField(math_operators)
    num_b = forms.FloatField()
