import json
from django.http import HttpResponse
from auth.models import Token


def json_response(response_dict, status=200):
    response = HttpResponse(json.dumps(response_dict), content_type="application/json", status=status)
    response['Access-Control-Allow-Origin'] = 'apimemorycms.moome.net memorycms.moome.net'
    # response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

def get_token(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', None)
    if auth_header is not None:
        tokens = auth_header.split(' ')
        if len(tokens) == 2 and tokens[0] == 'Token':
            token = tokens[1]
            return Token.objects.filter(token=token).first()


def token_required(func):
    def inner(request, *args, **kwargs):
        if request.method == 'OPTIONS':
            return func(request, *args, **kwargs)
        auth_header = request.META.get('HTTP_AUTHORIZATION', None)
        if auth_header is not None:
            tokens = auth_header.split(' ')
            if len(tokens) == 2 and tokens[0] == 'Token':
                token = tokens[1]
                token_obj = get_token(request)
                if token_obj:
                    request.token = token_obj
                    return func(request, *args, **kwargs)
                else:
                    return json_response({
                        'error': 'Token not found'
                    }, status=401)
        return json_response({
            'error': 'Invalid Header'
        }, status=401)

    return inner