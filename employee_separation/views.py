from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import BankMaster,LCDocumentTypeMaster, PartyMaster, PlantMaster
from .serializers import (
    BankMasterSerializer,
    LCDocumentTypeMasterSerializer,
    PartyMasterSerializer,
    PlantMasterSerializer,
    
)
@api_view(["GET"])
def app_status(request):

    screens = [
        {
            'name': 'Bank Master',
            'module': 'bank-master',
            'path': '/masters/bank-master'
        },
        {
            'name': 'Party Master',
            'module': 'party-master',
            'path': '/masters/party-master'
        },
        {
            'name': 'Plant Master',
            'module': 'plant-master',
            'path': '/masters/plant-master'
        },
        {
            'name': 'LC Document Type',
            'module': 'lc-document-type',
            'path': '/masters/lc-document-type'
        }
    ]

    return Response({
        'status': True,
        'screens': screens,
        'message': 'App metadata loaded successfully'
    })

# class BankMasterViewSet(viewsets.ModelViewSet):
#     queryset = BankMaster.objects.filter(is_deleted=False, is_active=True)
#     serializer_class = BankMasterSerializer
#     authentication_classes = [TokenAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#     http_method_names = ["get", "post", "put", "patch", "delete"]

#     def perform_destroy(self, instance):

#         instance.is_deleted = True
#         instance.save(update_fields=["is_deleted"])


# class PartyMasterViewSet(viewsets.ModelViewSet):
#     queryset = PartyMaster.objects.filter(is_deleted=False, is_active=True)
#     serializer_class = PartyMasterSerializer
#     authentication_classes = [TokenAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#     http_method_names = ["get", "post", "put", "patch", "delete"]

#     def perform_destroy(self, instance):

#         instance.is_deleted = True
#         instance.save(update_fields=["is_deleted"])


# class PlantMasterViewSet(viewsets.ModelViewSet):
#     queryset = PlantMaster.objects.filter(is_deleted=False, is_active=True)
#     serializer_class = PlantMasterSerializer
#     authentication_classes = [TokenAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#     http_method_names = ["get", "post", "put", "patch", "delete"]

#     def perform_destroy(self, instance):

#         instance.is_deleted = True
#         instance.save(update_fields=["is_deleted"])


# class LCDocumentTypeMasterViewSet(viewsets.ModelViewSet):
#     queryset = LCDocumentTypeMaster.objects.filter(is_deleted=False, is_active=True)
#     serializer_class = LCDocumentTypeMasterSerializer
#     authentication_classes = [TokenAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#     http_method_names = ["get", "post", "put", "patch", "delete"]

#     def perform_destroy(self, instance):

#         instance.is_deleted = True
#         instance.save(update_fields=["is_deleted"])
