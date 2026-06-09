"""lawfirm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lawapp import views
from lawyerapp import views as l
from clientapp import views as c
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # main urls
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('attorney/', views.attorney, name="attorney"),
    path('client_registration/', views.client_registration, name="client_registration"),
    path('client_reg/', views.client_reg, name="client_reg"),
    path('client_login/', views.client_login, name="client_login"),
    path('lawyer_registration/', views.lawyer_registration, name="lawyer_registration"),
    path('lawyer_reg/', views.lawyer_reg, name="lawyer_reg"),
    path('lawyer_login/', views.lawyer_login, name="lawyer_login"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_home', views.admin_home, name="admin_home"),
    path('admin_view_lawyer', views.admin_view_lawyer, name="admin_view_lawyer"),
    path('admin_view_client', views.admin_view_client, name="admin_view_client"),
    path('admin_change_password', views.admin_change_password, name="admin_change_password"),
    path('admin_logout', views.admin_logout, name="admin_logout"),
    path('admin_add_notification', views.admin_add_notification, name="admin_add_notification"),
    path('admin_view_notification', views.admin_view_notification, name="admin_view_notification"),
    path("del_notifications/<int:id>", views.del_notifications, name="del_notifications"),

    path('accept_client/<str:email>', views.accept_client, name="accept_client"),
    path('reject_client/<str:email>', views.reject_client, name="reject_client"),
    path('accept_lawyer/<str:email>', views.accept_lawyer, name="accept_lawyer"),
    path('reject_lawyer/<str:email>', views.reject_lawyer, name="reject_lawyer"),

    # client
    path('client_home/', c.client_home, name="client_home"),
    path('client_details/', c.client_details, name="client_details"),
    path('client_change_password/', c.client_change_password, name="client_change_password"),
    path('client_logout/', c.client_logout, name="client_logout"),
    path('client_edit/<str:email>', c.client_edit, name="client_edit"),
    path('client_delete/<str:email>', c.client_delete, name="client_delete"),
    path('client_update/', c.client_update, name="client_update"),
    path('clients_view_feedbacks/<str:pk>', c.clients_view_feedbacks, name="clients_view_feedbacks"),
    path('book_lawyer/<str:pk>', c.book_lawyer, name="book_lawyer"),
    path('client_lawyers/', c.client_lawyers, name="client_lawyers"),
    path('booked/', c.booked, name="booked"),
    path('feedback/<int:id>', c.feedback, name="feedback"),
    path('client_view_notification', c.client_view_notification, name="client_view_notification"),
    path('client_view_services/<str:pk>', c.client_view_services, name="client_view_services"),

    path('book_services/<int:id>', c.book_services, name="book_services"),
    path('clients_view_bookings_services', c.clients_view_bookings_services, name="clients_view_bookings_services"),
    path('add_feedback/<int:id>', c.add_feedback, name="add_feedback"),
    path('clients_services_view_feedbacks/<int:id>', c.clients_services_view_feedbacks, name="clients_services_view_feedbacks"),
    path('add_queries/<str:pk>', c.add_queries,name="add_queries"),
    path('my_quries/', c.my_quries, name="my_quries"),
    path('manage_clients/<int:id>', c.manage_clients, name="manage_clients"),
    path('manage_files_clients/<int:id>', c.manage_files_clients, name="manage_files_clients"),

    path('delete_files_clients/<int:id>', c.delete_files_clients, name="delete_files_clients"),
    # lawyer
    path('lawyer_home/', l.lawyer_home, name="lawyer_home"),
    path('lawyer_details/', l.lawyer_details, name="lawyer_details"),
    path('lawyer_change_password/', l.lawyer_change_password, name="lawyer_change_password"),
    path('lawyer_logout/', l.lawyer_logout, name="lawyer_logout"),
    path('lawyer_edit/<str:email>',l.lawyer_edit, name="lawyer_edit"),
    path('lawyer_delete/<str:email>', l.lawyer_delete, name="lawyer_delete"),
    path('lawyer_update/', l.lawyer_update, name="lawyer_update"),
    path('view_booking/', l.view_booking, name="view_booking"),
    path('booking_approve/<int:id>', l.booking_approve, name="booking_approve"),
    path('manage/<int:id>', l.manage, name="manage"),

    path('manage_files/<int:id>', l.manage_files, name="manage_files"),
    path('delete_files/<int:id>', l.delete_files, name="delete_files"),
    path('booking_reject/<str:book_id>', l.booking_reject, name="booking_reject"),
    path('client_feedback/', l.client_feedback, name="client_feedback"),
    path('lawyer_view_notification', l.lawyer_view_notification, name="lawyer_view_notification"),
    path('add_services', l.add_services, name="add_services"),
    path('my_services', l.my_services, name="my_services"),

    path('view_bookings_services/<int:id>', l.view_bookings_services, name="view_bookings_services"),
    path('bookings_services_approve/<int:id>', l.bookings_services_approve, name="bookings_services_approve"),
    path('bookings_services_reject/<int:id>', l.bookings_services_reject, name="bookings_services_reject"),
    path('view_services_feedbacks/<int:id>', l.view_services_feedbacks, name="view_services_feedbacks"),

    path('view_quries', l.view_quries, name="view_quries"),
    path('lawyer_replies/<int:id>', l.lawyer_replies, name="lawyer_replies"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 5W5DH19QHEKUYFEDDJ4GCEPK
