from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('techs/', include('techs.urls')),
    # path('rest/', include('tech_api.urls')),
]
