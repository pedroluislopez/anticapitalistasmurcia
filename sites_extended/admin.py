from .models import Extended, SocialNetwork
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.admin import SiteAdmin
from django.contrib.sites.models import Site
from django.contrib import admin


class ExtendedAdmin(admin.StackedInline):
    model = Extended
    verbose_name = _('Extras')
    verbose_name_plural = _('Extras')
    can_delete = False


class SocialNetworkAdmin(admin.TabularInline):
    model = SocialNetwork

SiteAdmin.inlines.append(ExtendedAdmin)
SiteAdmin.inlines.append(SocialNetworkAdmin)
admin.site.unregister(Site)
admin.site.register(Site, SiteAdmin)
