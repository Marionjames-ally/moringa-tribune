from django.conf.urls import include
from django.urls import path,re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[  
    path('', views.welcome, name = 'welcome'),
    path('today/',views.news_of_day,name='newsToday'),
    path('archives/<past_date>',views.past_days_news,name='pastNews'),
    path('search/',views.search_results, name ='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
