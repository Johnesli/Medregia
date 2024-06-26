from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,StateModel, DistrictModel, Person,Notification,ConnectMedicals,RegisterMedicals
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

class CustomUserAdmin(UserAdmin):
    def get_queryset(self, request):
        # Return all users without any filtering
        return super().get_queryset(request)
    
    model = CustomUser
    list_display = ('username', 'email', 'phone_num', 'store_type', 'other_value', 'is_staff', 'groups_display','position')
    search_fields = ('username', 'phone_num', 'email', 'pin', 'store_type', 'other_value','position')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),  # Include custom fields
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom Fields', {'fields': ('phone_num', 'pin', 'store_type', 'other_value','position')}),
    )

    def groups_display(self, obj):
        return ', '.join([group.name for group in obj.groups.all()])
    groups_display.short_description = 'Groups'


class StateModelAdmin(admin.ModelAdmin):
    model = StateModel
    list_display = [
        'Pid',
        'Pname',
    ]

class DistrictModelAdmin(admin.ModelAdmin):
    model = DistrictModel
    list_display = [
        'id',
        'Pid',
        'districtname',
    ]

class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = [
        'user',
        'MedicalShopName',
        'ProprietaryName',
        'UniqueId',
        'temporaryNo',
    ]
    
class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    list_display = ('sender','receiver','message','timestamp','is_read','request_status')
    
class ConnectMedicalsAdmin(admin.ModelAdmin):
    model = ConnectMedicals
    list_display = ('request_sender','request_receiver','is_read','accept_status','timestamp')
    

class RegisterMedicalsAdmin(admin.ModelAdmin):
    model = RegisterMedicals
    list_display = ('Medical_name','dl_number1','dl_number2','medical_timestamp')
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(StateModel, StateModelAdmin)
admin.site.register(DistrictModel, DistrictModelAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(ConnectMedicals, ConnectMedicalsAdmin)
admin.site.register(RegisterMedicals, RegisterMedicalsAdmin)
