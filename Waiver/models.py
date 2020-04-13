from django.db import models

# start TimeStamp #
class TimeStamp(models.Model):
    """Base class containing all models common information."""

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Define Model as abstract."""
        abstract = True
# end TimeStamp #

# Contact Table
class Contact(TimeStamp):
  first_name = models.CharField(max_length=30, default='', null=True)
  last_name = models.CharField(max_length=30, default='', null=True)
  birth_day = models.DateField(max_length=20, default='', null=True)
  minor = models.CharField(max_length=20, default='', null=True)
  phone = models.CharField(max_length=20, default='', null=True)
  email = models.CharField(max_length=40, default='', null=True)
  status = models.CharField(max_length=30, default='', null=True)
  marketing = models.CharField(max_length=20, default='', null=True)
  guardian_id = models.CharField(max_length=20, default='', null=True)
  address1 = models.CharField(max_length=20, default='', null=True)
  address2 = models.CharField(max_length=20, default='', null=True)
  city = models.CharField(max_length=20, default='', null=True)
  state = models.CharField(max_length=20, default='', null=True)     
  zip_code = models.CharField(max_length=20, default='', null=True)

  def save(self, **kwargs):
    super(Contact, self).save()
  
  class Meta:
    db_table = 'contact'


# Waiver Table
class Waiver(TimeStamp):
  name = models.CharField(max_length=50, default='', null=True)

  def save(self, **kwargs):
    super(Waiver, self).save()
  
  class Meta:
    db_table = 'waiver'


# SignedWaiver Table
class SignedWaiver(TimeStamp):
  completed_date = models.DateField(max_length=20, default='', null=True)
  contact = models.ForeignKey(Contact, on_delete=models.CASCADE, default='', null=True)
  waiver = models.ForeignKey(Waiver, on_delete=models.CASCADE, default='', null=True)

  def save(self, **kwargs):
    super(SignedWaiver, self).save()
  
  class Meta:
    db_table = 'signed_waiver'