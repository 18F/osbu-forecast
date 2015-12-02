# Forecast

The  MVP of a better version of http://www.gsa.gov/portal/content/101163 for the GSA Office of Small Business Utilization.

## Planned Architecture

The 18F team envisions that this site will involve three components:

1. An interface for administrators/staff to add new oppportunities (Django admin interface).
2. A read-only REST API (probably, Django-REST) available at  https://github.com/18F/osbu-forecast-api.
3. A static site using d3 and/or datatables.

# Front Site Organization

## What's displayed on front and is filterable
* GSA Organization
* Region
* Award Status
* Product or Service Description
* Place of Performance (City)
* Place of Performance (State)
* Primary NAICS Code
* Estimated Award Fiscal Year and Quarter
* Socioeconomic Category

## What should be available on click-through
* Contract Type
* Procurement Method
* Competition Strategy
* From (Min)  To (Max)
* Delivery Order Value
* Incumbent Contractor Name (if applicable)
* Contract/Order Number (if applicable)
* New Requirement or Exercise of Option or Recompete
* Estimated Solicitation Date
* Link to Solicitation in FedBizOpps (if available) 
* Point of Contact (Name)
* Point of Contact (Email Address)
* OSBU Small Business Technical Advisor (SBTA)  
* Additional Information

#Forecast Disclaimer
All projected procurements are subject to revision or cancellation. Final decisions on the extent of competition, small business participation, estimated value, or any aspect of the procurement action will not be made until each procurement is posted to Federal Business Opportunities (FEDBIZOPPS). Forecast data is for planning purposes only and is not a commitment by the government to purchase the described products and services.
