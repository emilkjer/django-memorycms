from core import models

def get_apps_content(apps):

    entities = []
    for app in apps:
        entities.append({
            'title': app.title,
            'id': app.pk,
        })
    data = {
        'apps': entities,
    }
    return data
        

def get_group_content(top_group):
    """
    Return the children of a group withouth
    iterating throug sub-groups
    """
    entities = []
    for entity in top_group.content.all():
        entity_data = {}
        for type in entity.entity_types.all():
            if type.is_group:
                entity_data['group'] = type.get_top_class().pk
                entity_data['id'] = type.get_top_class().pk
            entity_data['name'] = type.get_top_class().content

        entities.append(entity_data)

    group_entity = models.EntityBase.objects.get(entity_types=top_group)
    try:
        parent_group = models.EntityTypeEntityGroup.objects.get(content=group_entity)
    except models.EntityTypeEntityGroup.DoesNotExist:
        parent_group = None

    data = {
        'entities': entities,
        #TODO get name of current group
        # 'top_group_name': top_group.content,
        'top_group_id': top_group.pk,
    }
    if parent_group:
        #TODO Get name of parent group
        # data['parent_group_name'] = parent_group.content
        data['parent_group_id'] = parent_group.pk

    return data


def get_all_group_content(entity_base):
    data = {}
    for item in entity_base:
        di = {
            'id': item.pk,
            'is_group': item.is_group
        }
        di['entities'] = []
        for it in item.entity_types.all():
            if it.get_top_class().is_group:
                di['entities'].append('group')
                di['entities'].append(get_all_group_content(it.get_top_class().content.all()))
            else:
                di['entities'].append(str(it.get_top_class().content))
        data[item.pk] = di
    return data