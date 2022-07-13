import os
import hmac
import hashlib

import git
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from . import settings

@csrf_exempt
def update_repository(request: HttpRequest):
    if request.method == 'POST':
        x_hub_signature = request.headers.get('X-Hub-Signature')

        #if is_valid_signature(x_hub_signature, request.data, os.getenv('WEBHOOK_TOKEN')):
        git.Repo(settings.BASE_DIR).remotes.origin.pull()
        return HttpResponse('Web server updated!')
    else:
        return HttpResponse('Sorry, but you are not allowed!')


def is_valid_signature(x_hub_signature, data, private_key):
    # x_hub_signature and data are from the webhook payload
    # private key is your webhook secret
    hash_algorithm, github_signature = x_hub_signature.split('=', 1)
    algorithm = hashlib.__dict__.get(hash_algorithm)
    encoded_key = bytes(private_key, 'latin-1')
    mac = hmac.new(encoded_key, msg=data, digestmod=algorithm)
    return hmac.compare_digest(mac.hexdigest(), github_signature)