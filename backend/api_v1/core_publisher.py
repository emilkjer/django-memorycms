import json

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from core import models
from core import utils
from token_auth.utils import json_response, token_required, get_token


@token_required
def apps(request):
    """Return a list of all apps"""

    token = get_token(request)
    if not token:    
    # if not request.user.is_authenticated():
        data = {'login': 0}
        return json_response(data)

    apps = models.App.objects.all()
    data = utils.get_apps_content(apps)
    data['login'] = 1
    return json_response(data)

@token_required
def get_app_content(request, app_id):
    """Return a list of the content of a given app"""
    app = get_object_or_404(models.App, pk=app_id)

    # we always have a group so get [0]
    top_group = app.top_entity.entity_types.filter(
        is_group=True)[0].get_top_class()
    data = utils.get_group_content(top_group)
    data['app'] = {
        'title': app.title,
        'id': app.id,
    }
    return json_response(data)

@token_required
def get_group_content(request, group_id):
    """Return a list of content of a given group"""
    top_group = get_object_or_404(models.EntityTypeEntityGroup, pk=group_id)
    data = utils.get_group_content(top_group)
    return json_response(data)





###### OLD STUFF ########



def add_text(request, group_id):
    top_group = get_object_or_404(models.EntityTypeEntityGroup, pk=group_id)
    data = {}
    if request.is_ajax():
        request_data = json.loads(request.body)
        content = request_data.get('content','')
        if len(content):
            et = models.EntityBase.objects.create()
            ets = models.EntityTypeText.objects.create(content=content)
            et.entity_types.add(ets)
            top_group.content.add(et)
            data['message'] = 'Content added'
            data['STATUS'] = '1'
        else:
            data['message'] = 'Missing data'
            data['STATUS'] = '0'
    return HttpResponse(json.dumps(data), content_type="application/json")

def add_string(request, group_id):
    top_group = get_object_or_404(models.EntityTypeEntityGroup, pk=group_id)
    data = {}
    if request.is_ajax():
        request_data = json.loads(request.body)
        content = request_data.get('content','')
        if len(content):
            et = models.EntityBase.objects.create()
            ets = models.EntityTypeString.objects.create(content=content)
            et.entity_types.add(ets)
            top_group.content.add(et)
            data['message'] = 'Content added'
            data['STATUS'] = '1'
        else:
            data['message'] = 'Missing data'
            data['STATUS'] = '0'
    return HttpResponse(json.dumps(data), content_type="application/json")

def add_group(request, group_id):
    top_group = get_object_or_404(models.EntityTypeEntityGroup, pk=group_id)
    data = {}
    if request.is_ajax():
        request_data = json.loads(request.body)
        content = request_data.get('content','')
        if len(content):
            entity = models.EntityBase.objects.create()
            group_type = models.EntityTypeEntityGroup.objects.create()
            group_name = models.EntityTypeString.objects.create(
                content=content)
            entity.entity_types.add(group_name)
            entity.entity_types.add(group_type)
            entity.save()
            top_group.content.add(entity)

            data['message'] = 'Group added'
            data['STATUS'] = '1'
        else:
            data['message'] = 'Invalid data'
            data['STATUS'] = '0'
    return HttpResponse(json.dumps(data), content_type="application/json")

def auth_login(request):
    data = {
        'message': 'Missing data',
        'STATUS': 0,
    }
    if request.is_ajax():
        request_data = json.loads(request.body)
        print request_data
        username = request_data.get('username','')
        password = request_data.get('password','')
        if len(username) and len(password):
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    data['message'] = 'Logged in'
                    data['STATUS'] = '1'
                else:
                    # Return a 'disabled account' error message
                    data['message'] = 'Disabled account'
                    
            else:
                # Return an 'invalid login' error message.
                data['message'] = 'Invalid login'
    return HttpResponse(json.dumps(data), content_type="application/json")

def auth_logout(request):
    print "hello"
    logout(request)
    data = {
        'message': 'logged out',
        'login': 0,
    }

    return HttpResponse(json.dumps(data), content_type="application/json")

#### TEST FUNCTIONS ####
def test(request):
    return HttpResponse(json.dumps({}), content_type="application/json")

def entity_base_all(request):
    data = {}
    content = models.EntityBase.objects.all()
    data = utils.get_all_group_content(content)
    return HttpResponse(json.dumps(data), content_type="application/json")


