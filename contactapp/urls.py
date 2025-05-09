from django.urls import path
from.import views


urlpatterns=[
    path("",views.contact_read,name="contact_read"),
    path("/create",views.contact_create,name="contact_create"),
    path("/update/<int:id>/",views.contact_update,name="contact_update"),
    path("/delete/<int:id>/",views.contact_delete,name="contact_delete"),
    path("/view/<int:id>/",views.contact_view,name="contact_view"),
    #path('/auth',include('rest_framework.urls',name='rest_framework')),
]