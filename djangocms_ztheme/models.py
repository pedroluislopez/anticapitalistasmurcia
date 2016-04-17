from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site


class SiteExtra(models.Model):
    site = models.OneToOneField(Site, models.CASCADE, verbose_name=_("Site"),
                                editable=False, related_name='extra')
    email = models.EmailField(_("email"))
    default_meta_description = models.TextField(_("default description"), max_length=255, blank=True, null=True,
                                                help_text=_("The default text displayed in search engines."))
    copyright = models.TextField(_("copyright"), max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'djangocms_ztheme_site_extra'


class SiteSocialNetwork(models.Model):
    site = models.ForeignKey(Site, models.CASCADE, verbose_name=_("Site"),
                                      related_name='social_networks')
    name = models.CharField(_("email"), max_length=255)
    url = models.CharField(_("url"), max_length=2048)
    css_classes = models.CharField(_("css classes"), max_length=255, blank=True, null=True,
                                   help_text=_("Extra CSS classes for <a> HTML tag."))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'djangocms_ztheme_site_social_network'
