from django import forms


class PhoneForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, max_length=1000, label='', help_text='Enter Text Here')
