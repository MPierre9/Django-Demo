
from . import views 
from django.conf.urls import url
from polls.views import ListView, ListViewAjax

urlpatterns = [ 
        # /polls/
        url(r'^$', views.polls, name='index'),

        # /polls/5/ 
        url(r'^(?P<employee_id>[0-9]+)/$', views.detail, name='detail'),

        # /polls/5/vote/
        url(r'^(?P<employee_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
        # /polls/list/
        url(r'^list/$', ListView.as_view(), name='list'),

        # /polls/list/ajax
        url(r'^list/ajax$', ListViewAjax.as_view(), name='list-ajax'),

        # /polls/create/
        url(r'^create/$', views.create, name='create'),
                
        # /polls/delete/2
        url(r'^delete/(?P<employee_id>[0-9]+)/$', views.delete, name='delete'),

        # /polls/update/4 
        url(r'^update/(?P<employee_id>[0-9]+)/$', views.update, name='update'),
        
        # /polls/ajax/delete
        url(r'^polls/ajax/delete/$', views.deleteEmpAjax, name='deleteAjax'),

        # /polls/ajax/create
        url(r'^polls/ajax/create/$', views.createEmpAjax, name='createAjax'),

        
        # /polls/ajax/edit
        url(r'^polls/ajax/edit/$', views.editEmpAjax, name='editAjax'),




]