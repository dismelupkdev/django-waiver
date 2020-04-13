from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.http import JsonResponse 
from django.views.generic import TemplateView
from .forms import ContactForm

class LandingPageView(TemplateView):
  template_name="landing.html"

  def get_context_data(self, **kwargs):
    return { 'data': '' }


class NewWavierPageView(TemplateView):
  template_name="new_waiver.html"
  contact_form = ContactForm

  def get_context_data(self, **kwargs):
    context = {}
    context['contact_form'] = self.contact_form
    return context
