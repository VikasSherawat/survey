from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.http import JsonResponse
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
