import os

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import URLResolver, URLPattern

PROJECT = __import__(os.environ.get('project_name')+".settings")
REQUEST_METHODS = ['get','post','put','delete','patch']
DISPLAY_MODELS = PROJECT.settings.DISPLAY_MODELS
PROJECT_APPS = PROJECT.settings.PROJECT_APPS
print("DISPLAY_MODELS found: {}".format(len(DISPLAY_MODELS.keys())))
EXTRA_USER_META = PROJECT.settings.EXTRA_USER_META
print("EXTRA_USER_META found: {}".format(len(EXTRA_USER_META)))

views = []
for each in PROJECT_APPS:
    try:
        import pyclbr
        print(each)
        module = pyclbr.readmodule('{}.views'.format(each))
        for item in module.values():
            views.append(item.name.lower())
    except Exception as e:
        print(e)

print("TOTAL_VIEWS found: {}".format(len(views)))


model_permissions_created_count = 0
section_permissions_created_count = 0
subsection_permissions_created_count = 0
view_permissions_created_count = 0

for model in DISPLAY_MODELS.keys():
    content_type = ContentType.objects.filter(model__iexact=model)
    if not content_type.exists():
      print("ContentType not found for: {}".format(model))
      continue
    else:
      content_type=content_type.first()
    if not Permission.objects.filter(content_type=content_type,codename='view_{}'.format(model)).exists():
        view_permission = Permission.objects.create(name='Can View {}'.format(model),
                                                           content_type=content_type,
                                                           codename='view_{}'.format(model))
        model_permissions_created_count+=1
    if not Permission.objects.filter(content_type=content_type,codename='add_{}'.format(model)).exists():
        add_permission = Permission.objects.create(name='Can Add {}'.format(model),
                                                           content_type=content_type,
                                                           codename='add_{}'.format(model))
        model_permissions_created_count+=1
    if not Permission.objects.filter(content_type=content_type,codename='change_{}'.format(model)).exists():
        change_permission = Permission.objects.create(name='Can Change {}'.format(model),
                                                           content_type=content_type,
                                                           codename='change_{}'.format(model))
        model_permissions_created_count+=1
    if not Permission.objects.filter(content_type=content_type,codename='delete_{}'.format(model)).exists():
        delete_permission = Permission.objects.create(name='Can Delete {}'.format(model),
                                                           content_type=content_type,
                                                           codename='delete_{}'.format(model))
        model_permissions_created_count+=1

if not ContentType.objects.filter(app_label=os.environ.get('project_name'), model="none").exists():
    content_type=ContentType.objects.create(app_label=os.environ.get('project_name'), model="none")
else:
    content_type=ContentType.objects.get(app_label=os.environ.get('project_name'), model="none")

for section in EXTRA_USER_META.keys():
    if not Permission.objects.filter(codename='view_{}'.format(section.lower())).exists():
        section_permission = Permission.objects.create(name='Can View {} Section'.format(section),
                                                               content_type=content_type,
                                                               codename='view_{}'.format(section.lower()))
        section_permissions_created_count+=1

for section, subsections  in EXTRA_USER_META.items():
    for subsection in subsections:
        if 'screen' in subsection.keys():
            if not Permission.objects.filter(codename='view_{}'.format(subsection['screen'].lower())).exists():
                sub_section_permission = Permission.objects.create(name='Can View {} Subsection'.format(subsection['screen']),
                                                                       content_type=content_type,
                                                                       codename='view_{}'.format(subsection['screen'].lower()))
                subsection_permissions_created_count+=1

if not ContentType.objects.filter(app_label=os.environ.get('project_name'), model="none").exists():
    content_type=ContentType.objects.create(app_label=os.environ.get('project_name'), model="none")
else:
    content_type=ContentType.objects.get(app_label=os.environ.get('project_name'), model="none")

for view in views:
    for method in REQUEST_METHODS:
        if not Permission.objects.filter(codename='{}_{}_view'.format(method, view)).exists():
            view_permission = Permission.objects.create(name='Can {} {} View'.format(method, view),
                                                                content_type=content_type,
                                                                codename='{}_{}_view'.format(method, view))
            view_permissions_created_count+=1



print("--------------------------------------------------------------------")
print("{} Model permissions created".format(model_permissions_created_count))
print("{} Section permissions created".format(section_permissions_created_count))
print("{} Subsection permissions created".format(subsection_permissions_created_count))
print("{} View permissions created".format(view_permissions_created_count))