from django.contrib import admin
from .models import Post,Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.sites.AdminSite.site_header = "پنل ادمینی"
admin.sites.AdminSite.site_title = "پنل ادمین"