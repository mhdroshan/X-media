from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# import xadmin # Temporarily commented out due to NameError in xadmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MasterEntry.urls')),
    path('user/', include('User.urls')),
    path('posts/', include('Posts.urls')),
    path('tags/', include('Tags.urls')),
    path('tagauthor/', include('TagAuthor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
