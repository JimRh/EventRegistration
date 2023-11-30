from django.urls import path
from .views import *

urlpatterns = [
    path('createevent',create_event),
    path('registerevent/<int:eventid>',register_event),
    path('unregisterevent/<int:eventid>',unregister_event),
    path('eventlist',event_list),
    path('regeventlist',reg_event_list),
    path('alleventlist',all_event_list),
]