from django.db import models
import reversion


@reversion.register()
class BankMaster(models.Model):
    id = models.AutoField(primary_key=True)
    bank_code = models.CharField(max_length=10, unique=True)
    bank_name = models.CharField(max_length=150)
    branch_name = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    swift_code = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "LC_BANK_MASTER"

    class UI_Meta:
        form = [
            {
                "label": "Bank Code",
                "decorator": "bank_code",
                "type": "textbox",
                "required": "true",
                "message": "Enter Bank Code",
                "id": "bank_code",
                "placeholder": "Please enter Bank Code",
                "disabled": False,
            },
            {
                "label": "Bank Name",
                "decorator": "bank_name",
                "type": "textbox",
                "required": "true",
                "message": "Enter Bank Name",
                "id": "bank_name",
                "placeholder": "Please enter Bank Name",
                "disabled": False,
            },
            {
                "label": "Branch Name",
                "decorator": "branch_name",
                "type": "textbox",
                "required": "false",
                "message": "",
                "id": "branch_name",
                "placeholder": "Enter Branch (optional)",
                "disabled": False,
            },
            {
                "label": "City",
                "decorator": "city",
                "type": "textbox",
                "required": "false",
                "message": "",
                "id": "city",
                "placeholder": "Enter City (optional)",
                "disabled": False,
            },
            {
                "label": "SWIFT Code",
                "decorator": "swift_code",
                "type": "textbox",
                "required": "false",
                "message": "",
                "id": "swift_code",
                "placeholder": "Enter SWIFT Code (optional)",
                "disabled": False,
            },
        ]
