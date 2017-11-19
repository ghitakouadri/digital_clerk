from django.conf.urls import url
from . import views

app_name = 'digitalclerk_app'

urlpatterns = [
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^admin_index$', views.admin_index, name='admin_index'),
    url(r'^dashboard/module_details/(?P<module_code>[0-9A-Za-z]+)$', views.module_details, name='module_details'),
    url(r'^add_office_hour$', views.add_office_hour, name='add_office_hour'),
    url(r'^delete_office_hour$', views.delete_office_hour, name='delete_office_hour'),
    url(r'^edit_office_hour$', views.edit_office_hour, name='edit_office_hour'),
    url(r'^office_hour_dashboard_student$', views.office_hour_dashboard_student, name='office_hour_dashboard_student'),
    url(r'^office_hour_dashboard$', views.office_hour_dashboard, name='office_hour_dashboard'),
    url(r'^add_request/(?P<office_hour_id>[0-9]+)/(?P<user_id>[0-9]+)/(?P<lecturer_id>[0-9]+)$', views.add_request, name='add_request'),
    url(r'^edit_request/(?P<office_hour_id>[0-9]+)/(?P<lecturer_id>[0-9]+)/(?P<help_request_id>[0-9]+)$', views.edit_request, name='edit_request'),
    url(r'^close_request/(?P<office_hour_id>[0-9]+)/(?P<lecturer_id>[0-9]+)/(?P<help_request_id>[0-9]+)$', views.close_request, name='close_request'),
    url(r'^close_interaction/(?P<office_hour_id>[0-9]+)/(?P<lecturer_id>[0-9]+)/(?P<help_request_id>[0-9]+)/(?P<interaction_id>[0-9]+)/(?P<status>[0-2])$', views.close_interaction, name='close_interaction'),
    url(r'^open_interaction/(?P<office_hour_id>[0-9]+)/(?P<lecturer_id>[0-9]+)/(?P<help_request_id>[0-9]+)/(?P<status>[0-2])$', views.open_interaction, name='open_interaction')

]