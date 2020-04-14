from django import forms
import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Contact Form
class ContactForm(forms.Form):
  def __init__(self, *args, **kwargs):
    super(ContactForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_id = 'id-exampleForm'
    self.helper.form_class = 'blueForms'
    self.helper.form_method = 'post'
    self.helper.form_action = 'submit_survey'

    self.helper.add_input(Submit('submit', 'Submit'))


  first_name = forms.CharField(
    label="First Name",
    max_length=80,
    required=True,
  )
  last_name = forms.CharField(
    label="Last Name",
    max_length=80,
    required=True,
  )
  birth_day = forms.DateField(
    label="Birth Day",
    initial=datetime.date.today
  )
  minor = forms.CharField(
    label="Minor",
    max_length=20,
    required=True
  )
  phone = forms.CharField(
    label="Phone",
    max_length=20,
    required=True
  )
  email = forms.CharField(
    label="Email",
    max_length=40,
    required=True
  )
  status = forms.CharField(
    label="Status",
    max_length=30,
    required=True
  )
  marketing = forms.CharField(
    label="Marketing",
    max_length=20,
    required=True
  )
  guardian_id = forms.CharField(
    label="GuardianID",
    max_length=20,
    required=True
  )
  address1 = forms.CharField(
    label="Address1",
    max_length=20,
    required=True
  )
  address2 = forms.CharField(
    label="Address2",
    max_length=20,
    required=True
  )
  city = forms.CharField(
    label="City",
    max_length=20,
    required=True
  )
  state = forms.CharField(
    label="State",
    max_length=20,
    required=True
  )     
  zip_code = forms.CharField(
    label="Zip",
    max_length=20,
    required=True
  )