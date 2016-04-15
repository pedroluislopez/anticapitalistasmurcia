from .models import SiteExtra, SiteSocialNetwork
from django.contrib.sites.admin import SiteAdmin
from django.contrib.sites.models import Site
from django.contrib import admin


class SiteExtraAdmin(admin.StackedInline):
    model = SiteExtra
    can_delete = False


class SiteSocialNetworkAdmin(admin.TabularInline):
    model = SiteSocialNetwork

SiteAdmin.inlines.append(SiteExtraAdmin)
SiteAdmin.inlines.append(SiteSocialNetworkAdmin)
admin.site.unregister(Site)
admin.site.register(Site, SiteAdmin)
