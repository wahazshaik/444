from django.db import models
import reversion


@reversion.register()
class LCDocumentTypeMaster(models.Model):
    id = models.AutoField(primary_key=True)
    doc_code = models.CharField(max_length=10, unique=True)
    doc_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_mandatory = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "LC_DOCUMENT_TYPE_MASTER"

    class UI_Meta:
        form = [
            {
                "label": "Document Code",
                "decorator": "doc_code",
                "type": "textbox",
                "required": "true",
                "message": "Enter Document Code",
                "id": "doc_code",
                "placeholder": "e.g. INV, PL, BL",
                "disabled": False,
            },
            {
                "label": "Document Name",
                "decorator": "doc_name",
                "type": "textbox",
                "required": "true",
                "message": "Enter Document Name",
                "id": "doc_name",
                "placeholder": "e.g. Invoice, Packing List, Bill of Lading",
                "disabled": False,
            },
            {
                "label": "Description",
                "decorator": "description",
                "type": "textbox",
                "required": "false",
                "message": "",
                "id": "description",
                "placeholder": "Optional description",
                "disabled": False,
            },
        ]
