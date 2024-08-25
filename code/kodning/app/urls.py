from django.urls import path
from django.conf import settings
from .views import Index, Python, Django, Deploy, Terminals
from django.views import View
from django.conf.urls.static import static

urlpatterns = [
  path('', Index.as_view(), name='index'),
  path('python/', Python.as_view(), name='python'),
  path('django/', Django.as_view(), name='django'),
  path('deploy/', Deploy.as_view(), name='deploy'),
  path('terminals/', Terminals.as_view(), name='terminals'),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)