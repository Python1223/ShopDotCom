from django.contrib import admin
from ProfileManagement.models import ProfileModel

# Register your models here.
class ProfileModelAdmin(admin.ModelAdmin):
    list_display= ['profileId','userIns','profileType']

admin.site.register(ProfileModel, ProfileModelAdmin)