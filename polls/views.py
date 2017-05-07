from django.views import generic
# Create your views here.
from django.views import generic
from oauth2client import client
from polls import settings
from django.urls import reverse
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import render
import json

class Home(generic.TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = dict()
        context['name'] = "rkd"
        context['age'] = "Sherawat"
        context['values'] = [['foo', 32], ['bar', 64], ['baz', 96]]
        return JsonResponse(context)
        #return self.render_to_response(json.dump(context))


def googlelogin(request):
    print("Inside GoogleLogin method")
    flow = client.OAuth2WebServerFlow(client_id=settings.SOCIAL_AUTH_GOOGLE_KEY,
                client_secret=settings.SOCIAL_AUTH_GOOGLE_SECRET,
                scope='email',
                redirect_uri='http://localhost:8000/googlelogin',
                _external=True
                )
    flow.params["include_granted_scopes"] = "true"
    flow.params["access_type"] = 'offline'
    print("Reached here")
    if "code" not in request.GET:
        print("Inside if block")
        auth_uri = flow.step1_get_authorize_url()
        print("AUth URI is :"+auth_uri)
        return HttpResponseRedirect(auth_uri)
    else:
        print("Inside else block")
        auth_code = request.GET["code"]
        print(auth_code)
        credentials = flow.step2_exchange(auth_code)
        credentials = json.loads(credentials.to_json())
        email = credentials["id_token"]["email"]
        print("Email is"+email)
    return HttpResponseRedirect(reverse('polls:index'))#request, 'createpolls/createpoll.html')