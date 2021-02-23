from django.urls import path, re_path, register_converter
from . import views
from .converters import YearConverter, MonthConverter, DayConverter

register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

app_name = 'instagram'


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    # path('archives/<int:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year),
    # path('archives/<year:year>/', views.archives_year),
    # re_path(r'(?P<pk>\d+)/$', views.post_detail),

    path('archive/', views.post_archive, name='post_archive'),
    path('archives/<year:year>/', views.post_archives_year, name='post_archives_year'),
    # path('archives/<year:year>/<month:month>', views.post_archives_month, name='post_archives_month'),
    # path('archives/<year:year>/<month:month>/<day:day>', views.post_archives_day, name='post_archives_day'),
]