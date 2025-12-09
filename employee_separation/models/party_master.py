from django.db import models
import reversion


@reversion.register()
class PartyMaster(models.Model):
    id = models.AutoField(primary_key=True)
    party_code = models.CharField(max_length=20, unique=True)
    party_name = models.CharField(max_length=200)
    party_type = models.CharField(
        max_length=30,
        help_text="e.g. Applicant, Beneficiary, Buyer, Seller",
    )
    address_line1 = models.CharField(max_length=200, blank=True, null=True)
    address_line2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "LC_PARTY_MASTER"

    class UI_Meta:
        form = [
            {
                "label": "Party Code",
                "decorator": "party_code",
                "type": "textbox",
                "required": "true",
                "message": "Enter Party Code",
                "id": "party_code",
                "placeholder": "Please enter Party Code",
                "disabled": False,
            },
            {
                "label": "Party Name",
                "decorator": "party_name",
                "type": "textbox",
                "required": "true",
                "message": "Enter Party Name",
                "id": "party_name",
                "placeholder": "Please enter Party Name",
                "disabled": False,
            },
            {
                "label": "Party Type",
                "decorator": "party_type",
                "type": "textbox",   
                "required": "true",
                "message": "Enter Party Type (Applicant / Beneficiary etc.)",
                "id": "party_type",
                "placeholder": "Applicant / Beneficiary / Buyer / Seller",
                "disabled": False,
            },
            {
                "label": "Address Line 1",
                "decorator": "address_line1",
                "type": "textbox",
                "required": "false",
                "message": "",
                "id": "address_line1",
                "placeholder": "Address line 1",
                "disabled": False,
            },
            {
                "label": "City",
                "decorator": "city",
                "type": "textbox",
                "required": "false",
                "message": "",
                "id": "city",
                "placeholder": "City",
                "disabled": False,
            },
            {
                "label": "Country",
                "decorator": "country",
                "type": "textbox",
                "required": "false",
                "message": "",
                "id": "country",
                "placeholder": "Country",
                "disabled": False,
            },
        ]
