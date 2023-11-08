from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Company)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Post_tag)
admin.site.register(Company_Tag)