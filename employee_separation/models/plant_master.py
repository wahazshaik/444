from django.db import models
import reversion


@reversion.register()
class PlantMaster(models.Model):
    id = models.AutoField(primary_key=True)
    plant_code = models.CharField(max_length=10, unique=True)
    plant_name = models.CharField(max_length=150)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "LC_PLANT_MASTER"

    class UI_Meta:
        form = [
            {
                "label": "Plant Code",
                "decorator": "plant_code",
                "type": "textbox",
                "required": "true",
                "message": "Enter Plant Code",
                "id": "plant_code",
                "placeholder": "Please enter Plant Code",
                "disabled": False,
            },
            {
                "label": "Plant Name",
                "decorator": "plant_name",
                "type": "textbox",
                "required": "true",
                "message": "Enter Plant Name",
                "id": "plant_name",
                "placeholder": "Please enter Plant Name",
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
