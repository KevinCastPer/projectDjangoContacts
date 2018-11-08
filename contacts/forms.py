from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('nameContact', 'email', 'phone', 'message')
        # labels = {
        #     'nameContact': 'Nombre',
        #     'email': 'Correo Electrónico',
        #     'phone': 'Telefóno',
        #     'message': 'mensaje'
        # }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
