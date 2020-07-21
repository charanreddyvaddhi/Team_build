from django.urls import path, include, re_path
from .import views
urlpatterns=[
    path('',views.page1,name="index"),
    path('Resources/',views.MembersListView.as_view(),name="resources"),
    path('Resource/<int:pk>', views.MembersDetailView.as_view(), name='Resource-detail'),
    path('Technologies/',views.TechnologiesListView.as_view(),name="technologies"),

    #re_path(r'^member/(?P<pk>\d+)$', views.MembersDetailView.as_view(), name='member-detail')
]