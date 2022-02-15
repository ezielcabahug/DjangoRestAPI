from django.urls import path
from . import views
from .constants import *

urlpatterns = [
    path(URL_LIST_ALL, views.list_all),
    path(URL_CREATE, views.create),
    path(URL_UPDATE + '/<int:car_id>', views.update),
    path(URL_FIND, views.find),
    path(URL_DELETE + '/<int:car_id>', views.delete),
]
