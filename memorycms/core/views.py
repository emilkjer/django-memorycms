from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404, redirect

from . import models
from . import forms

class PartialGroupView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PartialGroupView, self).get_context_data(**kwargs)
        # update the context
        return context

def apps_show(request):
    apps = models.App.objects.all()
    return render(request, 'core/show_apps.html', {'apps': apps})

def app_show(request, app_id):
    app = get_object_or_404(models.App, pk=app_id)
    if request.POST:
        form = forms.TopGroupForm(request.POST)
        if form.is_valid():
            entity = models.EntityBase.objects.create()
            group_type = models.EntityTypeEntityGroup.objects.create()

            group_name = models.EntityTypeString.objects.create(
                content=form.cleaned_data.get('name',''))
            entity.entity_types.add(group_name)
            entity.entity_types.add(group_type)
            entity.save()
            app.top_entity = entity
            app.save()
    else:
        form = forms.TopGroupForm()

    # we always have a group
    top_group = app.top_entity.entity_types.filter(
        is_group=True)[0].get_top_class()

    entities = []
    for entity in top_group.content.all():
        entity_data = {}
        for type in entity.entity_types.all():
            if type.is_group:
                entity_data['group'] = type.get_top_class()
            entity_data['name'] = type.get_top_class().content

        entities.append(entity_data)

    data = {
        'app': app,
        'form': form,
        'entities': entities,
        'top_group': top_group,
    }
    return render(request, 'core/show_app.html', data)


#### SHOW #####
def entity_show_group(request, group_id):
    group = get_object_or_404(models.EntityTypeEntityGroup, pk=group_id)
    entities = []
    for entity in group.content.all():
        entity_data = {}
        for type in entity.entity_types.all():
            if type.is_group:
                entity_data['group'] = type.get_top_class()
            entity_data['name'] = type.get_top_class().content

        entities.append(entity_data)


    group_entity = models.EntityBase.objects.get(entity_types=group)
    try:
        parent_group = models.EntityTypeEntityGroup.objects.get(content=group_entity)
    except models.EntityTypeEntityGroup.DoesNotExist:
        parent_group = None
    data = {
        'group': group,
        'parent_group': parent_group,
        'entities': entities,
    }
    return render(request, 'core/entity_show_group.html', data)


#### ADD #####
def app_add(request):
    if request.POST:
        form = forms.AppAddForm(request.POST)
        if form.is_valid():

            app = models.App.objects.create(
                title=form.cleaned_data.get('title',''))
            entity = models.EntityBase.objects.create()
            group_type = models.EntityTypeEntityGroup.objects.create()

            group_name = models.EntityTypeString.objects.create(
                content=form.cleaned_data.get('title',''))
            entity.entity_types.add(group_name)
            entity.entity_types.add(group_type)
            entity.save()
            app.top_entity = entity
            app.save()
            return redirect('app-show', app_id=app.pk)
    else:
        form = forms.AppAddForm()
    data = {
        'form': form,
    }
    return render(request, 'core/app_add.html', data)

def entity_add_group(request, group_id):
    group = get_object_or_404(models.EntityTypeEntityGroup, pk=group_id)
    message = None
    if request.POST:
        form = forms.EntityTypeGroupForm(request.POST)
        if form.is_valid():
            entity = models.EntityBase.objects.create()
            group_type = models.EntityTypeEntityGroup.objects.create()

            group_name = models.EntityTypeString.objects.create(
                content=form.cleaned_data.get('name',''))
            entity.entity_types.add(group_name)
            entity.entity_types.add(group_type)
            entity.save()
            group.content.add(entity)
            # group.save() #TODO is this needed?
    else:
        form = forms.EntityTypeGroupForm()
    data = {
        'form': form,
        'message': message,
        'group': group,
        'reference_url': 'entity-add-group',
    }
    return render(request, 'core/entity_type_add_base.html', data)

def entity_add_string(request, group_id):
    group = get_object_or_404(models.EntityTypeEntityGroup, pk=group_id)
    message = None
    if request.POST:
        form = forms.EntityTypeStringForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content', '')
            message = "Added string: %s to group %s" % (content, group_id)
            et = models.EntityBase.objects.create()
            ets = models.EntityTypeString.objects.create(content=content)
            et.entity_types.add(ets)
            group.content.add(et)
    else:
        form = forms.EntityTypeStringForm()
    data = {
        'form': form,
        'message': message,
        'group': group,
        'reference_url': 'entity-add-string',
    }
    return render(request, 'core/entity_type_add_base.html', data)


def entity_add_text(request, group_id):
    group = get_object_or_404(models.EntityTypeEntityGroup, pk=group_id)
    message = None
    if request.POST:
        form = forms.EntityTypeTextForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content', '')
            message = "Added text: %s to group %s" % (content, group_id)
            et = models.EntityBase.objects.create()
            ets = models.EntityTypeText.objects.create(content=content)
            et.entity_types.add(ets)
            group.content.add(et)
    else:
        form = forms.EntityTypeTextForm()
    data = {
        'form': form,
        'message': message,
        'group': group,
        'reference_url': 'entity-add-text',
    }
    return render(request, 'core/entity_type_add_base.html', data)


# def entity_title(entity_base):
#     try:
#         title = entity_base.filter(is_group=False)[0] #assume always a title
#         return title.content
#     except IndexError:
#         return None