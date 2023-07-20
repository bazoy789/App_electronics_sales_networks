from django.contrib import admin
from django.contrib.auth.models import Group

from retail.models import Factory, RetailNetwork, IndividualEntrepreneur

admin.site.unregister(Group)


@admin.action(description='Delete arrears')
def make_published(modeladmin, request, queryset):
    queryset.update(arrears=0)


class BaseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "contacts", 'supplier', "arrears")
    search_fields = ["title"]
    list_filter = ["contacts__city"]
    readonly_fields = ("id", "title", "contacts", 'supplier', "products")
    actions = [make_published]


@admin.register(Factory, RetailNetwork, IndividualEntrepreneur)
class AllNetworkAdmin(BaseAdmin):
    pass

