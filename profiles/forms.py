from django import forms

class ContactForm(forms.Form):
	name    = forms.CharField(max_length=100, required=True, help_text='100 characters')
	email   = forms.EmailField(required=True)
	comment = forms.CharField(required=True, widget=forms.Textarea)
