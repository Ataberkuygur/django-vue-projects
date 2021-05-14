from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('auth-token/', obtain_auth_token, name='auth-token'),
    path('', include('Auth.urls')),
    path('', include('Category.urls')),
    path('', include('Habit.urls')),
    path('', include('Day.urls')),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
