from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('nameContact', 'email', 'phone', 'message')
        labels = {
            'nameContact': 'Nombre',
            'email': 'Correo Electrónico',
            'phone': 'Telefóno',
            'message': 'mensaje'
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["nameContact"].required = True
        self.fields["email"].required = True
        self.fields["phone"].required = False
        self.fields["message"].required = False
