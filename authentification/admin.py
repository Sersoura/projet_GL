from django.contrib import admin


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

# Ajoutez ces classes pour personnaliser l'affichage dans l'interface d'administration
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_client', 'is_avocat', 'is_admin')}),
    )

class AdminAdmin(admin.ModelAdmin):
    # Ajoutez des configurations spécifiques à l'admin si nécessaire
    pass

class ClientAdmin(admin.ModelAdmin):
    # Ajoutez des configurations spécifiques au client si nécessaire
    pass

class AvocatAdmin(admin.ModelAdmin):
    # Ajoutez des configurations spécifiques à l'avocat si nécessaire
    pass

# Enregistrez les modèles
admin.site.register(User, UserAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Avocat, AvocatAdmin)
admin.site.register(Comment)