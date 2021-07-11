from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('jinsung3/', views.jinsung3, name='jinsung3'),
    path('동아장왼쪽/', views.dongajangL, name='동아장왼쪽'),
    path('동아장왼쪽/<str:mdname>', views.dongajangLclick),
    path('editdajL/', views.editdajL),
    path('동아장오른쪽/', views.dongajangR, name='동아장오른쪽'),
    path('동아장오른쪽/<str:mdname>', views.dongajangRclick),
    path('editdajR/', views.editdajR),
]
