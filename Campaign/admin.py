"""
Campaign admin.py
"""
# pylint: disable=C0330,import-error
from django.contrib import admin
from django.contrib.admin.filters import AllValuesFieldListFilter

from EvalData.admin import BaseMetadataAdmin
from Campaign.models import (
    CampaignTeam, CampaignData, Campaign, TrustedUser
)


class DropdownFilter(AllValuesFieldListFilter):
    """
    Experimental dropdown filter.
    """
    template = 'Campaign/filter_select.html'


class CampaignTeamAdmin(BaseMetadataAdmin):
    """
    Model admin for CampaignTeam instances.
    """
    list_display = [
      'teamName', 'owner', 'teamMembers', 'requiredAnnotations',
      'requiredHours', 'completionStatus'
    ] + BaseMetadataAdmin.list_display
    list_filter = [
      'owner'
    ] + BaseMetadataAdmin.list_filter
    search_fields = [
      'teamName', 'owner__username', 'owner__first_name', 'owner__last_name'
    ] + BaseMetadataAdmin.search_fields

    filter_horizontal = ['members']

    fieldsets = (
      (None, {
        'fields': ('teamName', 'owner', 'members', 'requiredAnnotations',
          'requiredHours')
      }),
    ) + BaseMetadataAdmin.fieldsets


class CampaignDataAdmin(BaseMetadataAdmin):
    """
    Model admin for CampaignData instances.
    """
    list_display = [
      'dataName', 'market', 'metadata', 'dataValid', 'dataReady'
    ] + BaseMetadataAdmin.list_display
    list_filter = [
      'dataValid', 'dataReady'
    ] + BaseMetadataAdmin.list_filter
    search_fields = [
      # nothing model specific
    ] + BaseMetadataAdmin.search_fields

    fieldsets = (
      (None, {
        'fields': ('dataFile', 'market', 'metadata')
      }),
    ) + BaseMetadataAdmin.fieldsets



class CampaignAdmin(BaseMetadataAdmin):
    """
    Model admin for Campaign instances.
    """
    list_display = [
      'campaignName'
    ] + BaseMetadataAdmin.list_display
    list_filter = [
      # nothing model specific
    ] + BaseMetadataAdmin.list_filter
    search_fields = [
      # nothing model specific
    ] + BaseMetadataAdmin.search_fields

    filter_horizontal = ['batches']

    fieldsets = (
      (None, {
        'fields': ('campaignName', 'packageFile', 'teams', 'batches')
      }),
    ) + BaseMetadataAdmin.fieldsets


class TrustedUserAdmin(admin.ModelAdmin):
    """
    Model admin for Campaign instances.
    """
    list_display = [
      'user', 'campaign'
    ]
    list_filter = [
      ('campaign__campaignName', DropdownFilter),
#      'campaign'
    ]
    search_fields = [
      # nothing model specific
    ]

    fieldsets = (
      (None, {
        'fields': ('user', 'campaign')
      }),
    )

admin.site.register(CampaignTeam, CampaignTeamAdmin)
admin.site.register(CampaignData, CampaignDataAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(TrustedUser, TrustedUserAdmin)
