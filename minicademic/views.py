import os
import hmac
import hashlib

from django.http import HttpResponse, HttpResponseNotAllowed


def update_repository(request):
    x_hub_signature = request.headers.get('X-Hub-Signature')

    if is_valid_signature(x_hub_signature, request.data, os.getenv('WEBHOOK_TOKEN')):
        return HttpResponse('Web server updated!')
    else:
        return HttpResponseNotAllowed('Sorry, but you are not allowed!')


def is_valid_signature(x_hub_signature, data, private_key):
    # x_hub_signature and data are from the webhook payload
    # private key is your webhook secret
    hash_algorithm, github_signature = x_hub_signature.split('=', 1)
    algorithm = hashlib.__dict__.get(hash_algorithm)
    encoded_key = bytes(private_key, 'latin-1')
    mac = hmac.new(encoded_key, msg=data, digestmod=algorithm)
    return hmac.compare_digest(mac.hexdigest(), github_signature)