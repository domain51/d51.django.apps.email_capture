from d51.django.apps.email_capture import models
from django.http import HttpResponse, HttpResponseNotAllowed

def store(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['GET', ])

    email = email_for(request)
    return HttpResponse()

def email_for(request):
    user = not request.user.is_anonymous() and request.user or None
    return models.EmailAddress.objects.create(
        email=request.POST['email'],
        user=user
    )
