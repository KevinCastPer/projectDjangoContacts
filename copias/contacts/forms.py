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
        self.fields['nameContact'].widget.attrs['id'] = 'nameContact'
        self.fields['email'].widget.attrs['id'] = 'email'
        self.fields['phone'].widget.attrs['id'] = 'phone'
        self.fields['message'].widget.attrs['id'] = 'message'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
