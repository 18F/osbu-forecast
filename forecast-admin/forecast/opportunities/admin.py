from django.contrib import admin

# Register your models here.
from .models import Award

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(AwardAdmin, self).get_queryset(request)
        if request.user.is_superuser:
        # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()