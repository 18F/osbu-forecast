from django.db import models
from localflavor.us.models import USStateField, PhoneNumberField

# Create your models here.
class Office(models.Model):
  organization = models.CharField(max_length=30)
  region = models.CharField(max_length=30)

class Award(models.Model):
  AWARD_STATUS_CHOICES = (
    ('Pending', 'Award Pending'),
    ('Awarded','Awarded')
  )
  award_status = models.CharField(max_length=50, choices=AWARD_STATUS_CHOICES)
  description = models.CharField("Product or Service Description", max_length=200, blank=True, null=True)
  place_of_performance_city = models.CharField(max_length=100, default="Washington")
  place_of_performance_state = USStateField(default="DC")
  naics = models.CharField("Primary NAICS Code", max_length=20, blank=True, null=True)
  socioeconomic = models.CharField("Socioeconomic Category", max_length=50, blank=True, null=True)
  procurement_method = models.CharField("Procurement Method", max_length=200, blank=True, null=True)
  competition_strategy = models.CharField(max_length=200, blank=True, null=True)
  price_min = models.CharField(max_length=200, blank=True, null=True)
  price_max = models.CharField(max_length=200, blank=True, null=True)
  delivery_order_value = models.CharField(max_length=200, blank=True, null=True)
  incumbent_name = models.CharField("Incumbent Contractor Name", max_length=200, blank=True, null=True)
  new_requirement = models.CharField(max_length=200, blank=True, null=True)
  funding_agency = models.CharField(max_length=200, blank=True, null=True)  #Note: GSA Funded or Not-GSA-Funded
  estimated_solicitation_date = models.DateField(blank=True, null=True)
  fedbizopps_link = models.CharField(max_length=200, blank=True, null=True)
  estimated_fiscal_year = models.CharField(max_length=200, blank=True, null=True)
  estimated_fiscal_year_quarter = models.CharField(max_length=200, blank=True, null=True)
  point_of_contact_name = models.CharField(max_length=200, blank=True, null=True)
  point_of_contact_email = models.EmailField(max_length=200, blank=True, null=True)
  point_of_contact_phone = PhoneNumberField(blank=True, null=True)
  osbu_advisor_name = models.CharField(max_length=200, blank=True, null=True)
  osbu_advisor_email = models.EmailField(max_length=200, blank=True, null=True)
  osbu_advisor_phone = PhoneNumberField(blank=True, null=True)
  additional_information = models.TextField(blank=True, null=True)
