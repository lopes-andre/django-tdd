from django import forms

class HashForm(forms.Form):
    text = forms.CharField(
        label = 'Enter your text to be encoded to a hash:',
        widget=forms.Textarea
    )