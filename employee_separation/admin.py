from django.contrib import admin
from .models.bank_master import BankMaster
from .models.party_master import PartyMaster
from .models.plant_master import PlantMaster
from .models.lc_document_type import LCDocumentTypeMaster

admin.site.register(BankMaster)
admin.site.register(PartyMaster)
admin.site.register(PlantMaster)
admin.site.register(LCDocumentTypeMaster)