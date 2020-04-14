from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.http import JsonResponse 
from django.views.generic import TemplateView
from .forms import ContactForm
from .models import Contact, Waiver, SignedWaiver

# Landing Page
class LandingPageView(TemplateView):
  template_name="landing.html"

  def get_context_data(self, **kwargs):
    return { 'data': '' }

# New Waiver Page including Waiver form
class NewWavierPageView(TemplateView):
  template_name="new_waiver.html"
  contact_form = ContactForm

  def get_context_data(self, **kwargs):
    context = {}
    context['contact_form'] = self.contact_form
    return context

# Success Page indicating that the operation is successfully done
class SuccessPageView(TemplateView):
  template_name="success.html"

  def get_context_data(self, **kwargs):
    return { 'data': '' }

# Error Page indicating that some error happened.
class ErrorPageView(TemplateView):
  template_name="error.html"

  def get_context_data(self, **kwargs):
    return { 'data': '' }

'''
Create a new Contact.
in case GET, new Contact Page including Contact form.
in case POST, saving a new Contact. and then, redirect to whether success or error page.
'''
@csrf_exempt
def create_waiver(request):
  if request.method == 'GET':
    return NewWavierPageView.as_view()(request)
  elif request.method == 'POST':
    current_date = datetime.date.today() # as default, SignedWaiver's completed_date equals to current date.
    all_data = request.POST # get all data from the Contact Form
    # Check if the Contact already exists.
    try:
      already_exists = Contact.objects.get(email= all_data.get('email'))
      if already_exists:
        print('that waiver already exists')
        return redirect('/error')
    except Exception as e:
      pass
    try:
      # Create if it is a new Contact
      contact_data = Contact.objects.create(
        first_name=all_data.get('first_name', '0'),
        last_name=all_data.get('last_name', '0'),
        birth_day=all_data.get('birth_day', '0'),
        minor=all_data.get('minor', '0'),
        phone=all_data.get('phone', '0'),
        email=all_data.get('email', '0'),
        status=all_data.get('status', '0'),
        marketing=all_data.get('marketing', '0'),
        guardian_id=all_data.get('guardian_id', '0'),
        address1=all_data.get('address1', '0'),
        address2=all_data.get('address2', '0'),
        city=all_data.get('city', '0'),
        state=all_data.get('state', '0'),
        zip_code=all_data.get('zip_code', '0'),
      )
      contact_data.save()
      contact_ref = Contact.objects.get(email=all_data.get('email', '0'))
      # Create a new standard Waiver, if no exist.
      if not Waiver.objects.filter(id=1):
        Waiver.objects.create(
          name="Standard Waiver",
        ).save()
      waiver_ref = Waiver.objects.get(id=1)
      # Create a new SignedWaiver with newly created Contact and standard waiver
      signed_waiver = SignedWaiver.objects.create(waiver=waiver_ref, contact=contact_ref, completed_date=current_date)
      signed_waiver.save()
      return redirect('/success')
    except Exception as e:
      print('error = ', e)
      return redirect('/error')
