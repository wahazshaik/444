from rest_framework import serializers
from .models.bank_master import BankMaster
from .models.party_master import PartyMaster
from .models.plant_master import PlantMaster
from .models.lc_document_type import LCDocumentTypeMaster


class BankMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankMaster
        fields = "__all__"


class PartyMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyMaster
        fields = "__all__"


class PlantMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantMaster
        fields = "__all__"


class LCDocumentTypeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LCDocumentTypeMaster
        fields = "__all__"
