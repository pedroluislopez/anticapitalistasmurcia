from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from cms.models.pluginmodel import CMSPlugin
from django.core.validators import MaxValueValidator


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
    site = models.ForeignKey(Site, models.CASCADE, verbose_name=_("Site"), related_name='social_networks')
    name = models.CharField(_("name"), max_length=255, help_text=_("Name is used for CSS classes."))
    url = models.CharField(_("url"), max_length=2048)
    top_menu = models.BooleanField(_("top menu"), default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'djangocms_ztheme_site_social_network'


class ZThemeSection(CMSPlugin):
    name = models.CharField(_("name"), max_length=255)
    top = models.BooleanField(_("top"), default=False)
    xs = models.BooleanField(_("extra small devices"), default=False)
    sm = models.BooleanField(_("small devices"), default=False)
    md = models.BooleanField(_("medium devices"), default=False)
    lg = models.BooleanField(_("large devices"), default=False)
    extra_css_classes = models.CharField(_("extra css classes"), max_length=255, blank=True, null=True,
                                         help_text=_("Extra CSS classes for HTML tag."))

    def __str__(self):
        return self.name + ': ' + self.css_classes()

    def css_classes(self):
        css_classes = 'section section-' + str(self.name)
        if self.top:
            css_classes += ' section-top'
        if self.xs:
            css_classes += ' section-xs'
        if self.sm:
            css_classes += ' section-sm'
        if self.md:
            css_classes += ' section-md'
        if self.lg:
            css_classes += ' section-lg'
        if self.extra_css_classes:
            css_classes += ' ' + str(self.extra_css_classes)
        return css_classes

    class Meta:
        db_table = 'djangocms_ztheme_section'


class ZThemeRow(CMSPlugin):
    extra_css_classes = models.CharField(_("extra css classes"), max_length=255, blank=True, null=True,
                                         help_text=_("Extra CSS classes for HTML tag."))

    def __str__(self):
        return self.css_classes()

    def css_classes(self):
        css_classes = 'row'

        if self.extra_css_classes:
            css_classes += ' ' + str(self.extra_css_classes)

        return css_classes

    class Meta:
        db_table = 'djangocms_ztheme_row'


class ZThemeColumn(CMSPlugin):
    xs_columns = models.PositiveSmallIntegerField(_("columns"), blank=True, null=True,
                                                  validators=[MaxValueValidator(12)])
    xs_offset = models.PositiveSmallIntegerField(_("offset"), blank=True, null=True,
                                                 validators=[MaxValueValidator(12)])
    xs_push = models.PositiveSmallIntegerField(_("push"), blank=True, null=True,
                                               validators=[MaxValueValidator(12)])
    xs_pull = models.PositiveSmallIntegerField(_("pull"), blank=True, null=True,
                                               validators=[MaxValueValidator(12)])
    sm_columns = models.PositiveSmallIntegerField(_("columns"), blank=True, null=True,
                                                  validators=[MaxValueValidator(12)])
    sm_offset = models.PositiveSmallIntegerField(_("offset"), blank=True, null=True,
                                                 validators=[MaxValueValidator(12)])
    sm_push = models.PositiveSmallIntegerField(_("push"), blank=True, null=True,
                                               validators=[MaxValueValidator(12)])
    sm_pull = models.PositiveSmallIntegerField(_("pull"), blank=True, null=True,
                                               validators=[MaxValueValidator(12)])
    md_columns = models.PositiveSmallIntegerField(_("columns"), blank=True, null=True,
                                                  validators=[MaxValueValidator(12)])
    md_offset = models.PositiveSmallIntegerField(_("offset"), blank=True, null=True,
                                                 validators=[MaxValueValidator(12)])
    md_push = models.PositiveSmallIntegerField(_("push"), blank=True, null=True,
                                               validators=[MaxValueValidator(12)])
    md_pull = models.PositiveSmallIntegerField(_("pull"), blank=True, null=True,
                                               validators=[MaxValueValidator(12)])
    lg_columns = models.PositiveSmallIntegerField(_("columns"), blank=True, null=True,
                                                  validators=[MaxValueValidator(12)])
    lg_offset = models.PositiveSmallIntegerField(_("offset"), blank=True, null=True,
                                                 validators=[MaxValueValidator(12)])
    lg_push = models.PositiveSmallIntegerField(_("push"), blank=True, null=True,
                                               validators=[MaxValueValidator(12)])
    lg_pull = models.PositiveSmallIntegerField(_("pull"), blank=True, null=True,
                                               validators=[MaxValueValidator(12)])
    extra_css_classes = models.CharField(_("extra css classes"), max_length=255, blank=True, null=True,
                                         help_text=_("Extra CSS classes for HTML tag."))

    def __str__(self):
        return self.css_classes()

    def css_classes(self):
        css_classes = ''
        if self.xs_columns is not None:
            css_classes += ' col-xs-' + str(self.xs_columns)
        if self.xs_offset is not None:
            css_classes += ' col-xs-offset-' + str(self.xs_offset)
        if self.xs_push is not None:
            css_classes += ' col-xs-push-' + str(self.xs_push)
        if self.xs_pull is not None:
            css_classes += ' col-xs-pull-' + str(self.xs_pull)
        if self.sm_columns is not None:
            css_classes += ' col-sm-' + str(self.sm_columns)
        if self.sm_offset is not None:
            css_classes += ' col-sm-offset-' + str(self.sm_offset)
        if self.sm_push is not None:
            css_classes += ' col-sm-push-' + str(self.sm_push)
        if self.sm_pull is not None:
            css_classes += ' col-sm-pull-' + str(self.sm_pull)
        if self.md_columns is not None:
            css_classes += ' col-md-' + str(self.md_columns)
        if self.md_offset is not None:
            css_classes += ' col-md-offset-' + str(self.md_offset)
        if self.md_push is not None:
            css_classes += ' col-md-push-' + str(self.md_push)
        if self.md_pull is not None:
            css_classes += ' col-md-pull-' + str(self.md_pull)
        if self.lg_columns is not None:
            css_classes += ' col-lg-' + str(self.lg_columns)
        if self.lg_offset is not None:
            css_classes += ' col-lg-offset-' + str(self.lg_offset)
        if self.lg_push is not None:
            css_classes += ' col-lg-push-' + str(self.lg_push)
        if self.lg_pull is not None:
            css_classes += ' col-lg-pull-' + str(self.lg_pull)
        if self.extra_css_classes:
            css_classes += ' ' + str(self.extra_css_classes)

        if len(css_classes) > 0:
            return css_classes[1:]
        return css_classes

    class Meta:
        db_table = 'djangocms_ztheme_column'


class ZThemeSectionCallTo(CMSPlugin):
    title = models.CharField(_("title"), max_length=255)
    fa_icon = models.CharField(_("font awesome icon"), max_length=255)
    link_text = models.CharField(_("link text"), max_length=255)
    url = models.CharField(_("url"), max_length=2048)
    extra_css_classes = models.CharField(_("extra css classes"), max_length=255, blank=True, null=True,
                                         help_text=_("Extra CSS classes for HTML tag."))

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'djangocms_ztheme_section_callto'


class ZThemeSectionFeatures(CMSPlugin):
    extra_css_classes = models.CharField(_("extra css classes"), max_length=255, blank=True, null=True,
                                         help_text=_("Extra CSS classes for HTML tag."))

    class Meta:
        db_table = 'djangocms_ztheme_section_features'


class ZThemeSectionFeature(CMSPlugin):
    title = models.CharField(_("title"), max_length=255)
    fa_icon = models.CharField(_("font awesome icon"), max_length=255)
    description = models.TextField(_("description"), max_length=2048, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'djangocms_ztheme_section_feature'
