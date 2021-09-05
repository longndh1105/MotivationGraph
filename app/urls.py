from django.urls import path
from . import views

urlpatterns = [
    path('creategraph', views.creategraph, name='creategraph'),
    path('motivationgraph', views.motivation, name='motivation'),
    path('motivationgraph/vi', views.motivation_vi, name='motivationvi'),
    path('motivationgraph/ja', views.motivation_ja, name='motivationja')
]