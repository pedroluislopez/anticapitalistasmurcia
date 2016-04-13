from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site


class Extended(models.Model):
    site = models.OneToOneField(Site, models.CASCADE, verbose_name=_("Site"),
                                editable=False, related_name='extended')
    email = models.EmailField()

    class Meta:
        db_table = 'django_site_extended'


class SocialNetwork(models.Model):
    extended_site = models.ForeignKey(Site, models.CASCADE, verbose_name=_("Site"),
                                      related_name='social_networks')
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    css_classes = models.CharField(_("CSS classes"), max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'django_site_social_network'
