from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from contacts.models import Contact
from .serializers import ContactSerializer
from .permissions import IsOwnerOrReadOnly


@api_view(['GET', 'POST'])
def contact_list(request):
    """
    List all contacts, or create new contact
    """
    if request.method == 'GET':
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def contact_details(request, contact_id):
    """
    Get, update, or delete specify contact
    """
    try:
        contact = Contact.objects.get(pk=contact_id)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        contact.delete()
        return Response(status.HTTP_204_NO_CONTENT)
