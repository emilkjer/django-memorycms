import json

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from core import models
from core import utils

def apps(request):
    """Return a list of all apps"""
    apps = models.App.objects.all()
    data = utils.get_apps_content(apps)
    return HttpResponse(json.dumps(data), content_type="application/json")

def get_app_content(request, app_id):
    """Return a list of the content of a given app"""
    app = get_object_or_404(models.App, pk=app_id)

    # we always have a group so get [0]
    top_group = app.top_entity.entity_types.filter(
        is_group=True)[0].get_top_class()

    data = utils.get_group_content(top_group)
    
    return HttpResponse(json.dumps(data), content_type="application/json")

def get_group_content(request, group_id):
    """Return a list of content of a given group"""
    top_group = get_object_or_404(models.EntityTypeEntityGroup, pk=group_id)
    data = utils.get_group_content(top_group)
    return HttpResponse(json.dumps(data), content_type="application/json")



#### TEST FUNCTIONS ####
def test(request):
    return HttpResponse(json.dumps({}), content_type="application/json")

def entity_base_all(request):
    data = {}
    content = models.EntityBase.objects.all()
    data = utils.get_all_group_content(content)
    return HttpResponse(json.dumps(data), content_type="application/json")
