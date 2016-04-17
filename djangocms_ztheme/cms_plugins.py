from django.db import models
from .models import ZThemeSection, ZThemeColumn
from cms.plugin_base import CMSPluginBase
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from django.forms import TextInput


class ZThemeSectionPlugin(CMSPluginBase):
    module = 'Z Theme'
    model = ZThemeSection
    name = _("Section")
    render_template = "djangocms_ztheme/section_plugin.html"
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super(ZThemeSectionPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(ZThemeSectionPlugin)


class ZThemeRowPlugin(CMSPluginBase):
    module = 'Z Theme'
    model = CMSPlugin
    name = _("Row")
    render_template = "djangocms_ztheme/row_plugin.html"
    cache = False
    allow_children = True

plugin_pool.register_plugin(ZThemeRowPlugin)


class ZThemeColumnPlugin(CMSPluginBase):
    module = 'Z Theme'
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
    )

    formfield_overrides = {
        models.PositiveSmallIntegerField: {'widget': TextInput(attrs={'size': '10'})},
    }

    def render(self, context, instance, placeholder):
        context = super(ZThemeColumnPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(ZThemeColumnPlugin)
