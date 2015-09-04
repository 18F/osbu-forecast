# Forecast

A MVP of a better version of http://www.gsa.gov/portal/content/101163.

## Planned Architecture

I currently envision the site to involve three components:

1. An interface for administrators/staff to add new oppportunities (probably, Django admin interface).
2. Either a read-only REST API (probably, Django-REST), or more likely, a pipeline to publishing static files in S3.
3. A static site using d3 and/or datatables.