from django.contrib import admin
from django.urls import path
from . import views
from .views import user_login, user_logout, signup
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.show_all, name='show_all'),
    path('search/<str:query>', views.searchquery, name='searchquery'),
    path('updateview/<int:Post_id>/', views.increaseviews, name='increaseview'),
    path('updatelike/<int:Post_id>/', views.increaselikes, name='increaselikes'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('save', views.save_csv_to_model, name='save'),
    path('visualization_all/', views.all_chart, name='all_chart'),
    path('company_chart/<str:company>', views.company_chart, name='company_chart')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)