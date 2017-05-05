from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.http import JsonResponse

class Home(generic.TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['value'] = "11231414"
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        age = request.POST['age']
        context = dict()
        context['name'] = "rkd"
        context['age'] = "Sherawat"
        return JsonResponse(context)
