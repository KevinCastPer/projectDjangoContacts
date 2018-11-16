from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.views import APIView
from django.http import Http404
from contacts.models import Contact
from .serializers import ContactSerializer
from django.core.mail import send_mail


class ContactMixin(object):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactList(ContactMixin, ListCreateAPIView):
    """
    List all contacts, or create new contact
    """

    def get(self, request, *args, **kwargs):
        # Si solo queremos que el administrador vea eso, tiene pinta que aquí hay que tocar algo
        # como se si el usuario esta autenticado o no? pues en request hay siempre el objeto user
        # y pregunto

        if request.user.is_anonymous and not request.user.is_staff:
            # staff => admin si esta loqueado se puede ver lista sino no.
            # anonymous => anonymous tampoco podran verlo
            # hay que devolver un "return" pero algo especial, porque tiene que indicar error 403
            # busca en la documentacion de django rest framework sobre ello
            # como devolver un error
            # si, tambien vale, pero no el 404, sino el 403
            return Response(status=status.HTTP_403_FORBIDDEN)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # esto es lo q se está ejecuntado
        # console.log(contact)
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            subject = "Gracias por registrar Formulario"
            emailTo = contact.email
            print('**************')
            print(emailTo)
            send_mail(
                subject,
                'Muchas gracias por contactar. Nos pondemos en contacto lo antes posible',
                'kevin@gmail.com',
                [emailTo],
                fail_silently=False,
            )
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class ContactDetails(ContactMixin, RetrieveUpdateDestroyAPIView):
    """
    Get, update, or delete a specific survey
    """

    def get_object(self, contact_id):
        try:
            return Contact.objects.get(pk=contact_id)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, contact_id, format=None):
        contact = self.get_object(contact_id)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def put(self, request, contact_id, format=None):
        contact = self.get_object(contact_id)
        serializer = ContactSerializer(contact, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, contact_id, format=None):
        contact = self.get_object(contact_id)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ContactList(APIView):
#     """
#     List all contacts, or create new contact
#     """
#
#     def get(self, request, format=None):
#         contact = Contact.objects.all()
#         serializer = ContactSerializer(contact, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ContactSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)
#
#
# class ContactDetails(APIView):
#     """
#     Get, update, or delete a specific survey
#     """
#
#     def get_object(self, contact_id):
#         try:
#             return Contact.objects.get(pk=contact_id)
#         except Contact.DoesNotExist:
#             raise Http404
#
#     def get(self, request, contact_id, format=None):
#         contact = self.get_object(contact_id)
#         serializer = ContactSerializer(contact)
#         return Response(serializer.data)
#
#     def put(self, request, contact_id, format=None):
#         contact = self.get_object(contact_id)
#         serializer = ContactSerializer(contact, data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, contact_id, format=None):
#         contact = self.get_object(contact_id)
#         contact.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def contact_list(request):
#
#     if request.method == 'GET':
#         contact = Contact.objects.all()
#         serializer = ContactSerializer(contact, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,
#                             status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def contact_details(request, contact_id):
#     """
#     Get, update, or delete specify contact
#     """
#     try:
#         contact = Contact.objects.get(pk=contact_id)
#     except Contact.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = ContactSerializer(contact)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         serializer = ContactSerializer(contact, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         contact.delete()
#         return Response(status.HTTP_204_NO_CONTENT)
