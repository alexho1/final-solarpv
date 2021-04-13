from django.contrib import admin
from .models import User, Certificate, Company


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    exclude = ()


class CertificateAdmin(admin.ModelAdmin):
    exclude = ()


class CompanyAdmin(admin.ModelAdmin):
    exclude = ()


admin.site.register(User, UserAdmin)
admin.site.register(Certificate, UserAdmin)
admin.site.register(Company, UserAdmin)
