from django.db import models
from .models import ZThemeSection, ZThemeRow, ZThemeColumn, ZThemeSectionCallTo, ZThemeSectionFeature
from cms.plugin_base import CMSPluginBase
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from django.forms import TextInput


class ZThemeSectionPlugin(CMSPluginBase):
    module = 'Z Theme style'
    model = ZThemeSection
    name = _("Section")
    render_template = "djangocms_ztheme/section_plugin.html"
    cache = False
    allow_children = True

    fieldsets = (
        (None, {
            'fields': ('name', ('top', 'xs', 'sm', 'md', 'lg')),
        }),
        (_("More"), {
            'classes': ('collapse',),
            'fields': ('extra_css_classes',),
        }),
    )

    def render(self, context, instance, placeholder):
        context = super(ZThemeSectionPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(ZThemeSectionPlugin)


class ZThemeRowPlugin(CMSPluginBase):
    module = 'Z Theme style'
    model = ZThemeRow
    name = _("Row")
    render_template = "djangocms_ztheme/row_plugin.html"
    cache = False
    allow_children = True

    fieldsets = (
        (_("More"), {
            'classes': ('collapse',),
            'fields': ('extra_css_classes',),
        }),
    )

    def render(self, context, instance, placeholder):
        context = super(ZThemeRowPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(ZThemeRowPlugin)


class ZThemeColumnPlugin(CMSPluginBase):
    module = 'Z Theme style'
    model = ZThemeColumn
    name = _("Column")
    render_template = "djangocms_ztheme/column_plugin.html"
    cache = False
    allow_children = True
    parent_classes = ['ZThemeRowPlugin']

    fieldsets = (
        (None, {
            'fields': (),
            'description': 'Visit <a href="http://getbootstrap.com/css/#grid" target="blank">'
                           'http://getbootstrap.com/css/#grid</a> about bootstrap grid system.'
        }),
        (_("Extra small devices"), {
            'fields': (('xs_columns', 'xs_offset', 'xs_push', 'xs_pull'),)
        }),
        (_("Small devices"), {
            'fields': (('sm_columns', 'sm_offset', 'sm_push', 'sm_pull'),)
        }),
        (_("Medium devices"), {
            'fields': (('md_columns', 'md_offset', 'md_push', 'md_pull'),)
        }),
        (_("Large devices"), {
            'fields': (('lg_columns', 'lg_offset', 'lg_push', 'lg_pull'),)
        }),
        (_("More"), {
            'classes': ('collapse',),
            'fields': ('extra_css_classes',),
        }),
    )

    formfield_overrides = {
        models.PositiveSmallIntegerField: {'widget': TextInput(attrs={'size': '10'})},
    }

    def render(self, context, instance, placeholder):
        context = super(ZThemeColumnPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(ZThemeColumnPlugin)


class ZThemeSocialNetworksListPlugin(CMSPluginBase):
    module = 'Z Theme contents'
    model = CMSPlugin
    name = _("Social Networks List")
    render_template = "djangocms_ztheme/social_networks_list_plugin.html"
    cache = False

plugin_pool.register_plugin(ZThemeSocialNetworksListPlugin)


class ZThemeSectionCallToPlugin(CMSPluginBase):
    module = 'Z Theme sections'
    model = ZThemeSectionCallTo
    name = _("Call To")
    render_template = "djangocms_ztheme/section_callto_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(ZThemeSectionCallToPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(ZThemeSectionCallToPlugin)


class ZThemeSectionFeaturesPlugin(CMSPluginBase):
    module = 'Z Theme sections'
    model = CMSPlugin
    name = _("Features")
    render_template = "djangocms_ztheme/section_features_plugin.html"
    cache = False
    allow_children = True
    child_classes = ['ZThemeSectionFeaturePlugin']

plugin_pool.register_plugin(ZThemeSectionFeaturesPlugin)


class ZThemeSectionFeaturePlugin(CMSPluginBase):
    module = 'Z Theme sections'
    model = ZThemeSectionFeature
    name = _("Feature")
    render_template = "djangocms_ztheme/section_feature_plugin.html"
    cache = False
    parent_classes = ['ZThemeSectionFeaturesPlugin']

    def render(self, context, instance, placeholder):
        context = super(ZThemeSectionFeaturePlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(ZThemeSectionFeaturePlugin)
