from django.contrib import admin
from .models import *


# Register your models here.


admin.site.site_header = "Medico-Experts Admin"
admin.site.site_title = "Medico-Experts"
admin.site.index_title = "Welcome to Medico-Experts Dashboard"

#admin.site.register(Doctor)

admin.site.register(tbl_Medicalshop)
admin.site.register(tbl_Medicine)
admin.site.register(shop)