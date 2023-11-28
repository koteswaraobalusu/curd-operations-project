from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.mainpage,name='mainpage'),
    path('createaccount',views.createaccount,name='createaccount'),
    path('update/<id>',views.update,name='update'),
    path('update_data/<id>',views.update_data,name='update_data'),
    path('delete/<id>',views.delete,name='delete'),
]
if settings.DEBUG:
    urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
