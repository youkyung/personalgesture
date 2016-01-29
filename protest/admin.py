from django.contrib import admin
from protest.models import Protest, User, Participation, Donation, DonationState
# Register your models here.


class ProtestAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

class UserAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'email']
    list_display_links = ['nickname']

class ParticipationAdmin(admin.ModelAdmin):
    list_display = ['protest', 'user']
    list_display_links = ['protest']

class DonationAdmin(admin.ModelAdmin):
    list_display = ['protest', 'amount', 'account_number']
    list_display_links = ['protest']

class DonationStateAdmin(admin.ModelAdmin):
    list_display = ['protest', 'user']
    list_display_links = ['protest', 'user']


admin.site.register(Protest,ProtestAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Participation,ParticipationAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(DonationState, DonationStateAdmin)