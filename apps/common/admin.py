from django.contrib import admin

from .models import Currency

# admin page name
admin.site.site_header = 'Ombor'
admin.site.site_title = 'Admin panel'
admin.site.index_title = 'Ombor'

admin.site.register(Currency)
