from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        print(f"Sending email {self.cleaned_data['email']} with message : {self.cleaned_data['message']}")
            # cleaned_data it contains all the validated input data from the form
        # Send email logic here
