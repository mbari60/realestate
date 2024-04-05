from django.urls import path
from . import views, users,appartments , communityforum , lands , bnbs , maintenance , inquiry , booking , cleaners , transport


urlpatterns = [
    path('login/', users.login_view), 
    path('logout/', users.logout_view), 
    path('signup/', users.signup), 
    path('amenities/', views.amenities), 
    path('amenities/<int:id>/', views.amenities),
    path('apartments/', appartments.apartments),
    path('apartments/<int:id>/', appartments.apartments),
    path('lands/', lands.lands),
    path('lands/<int:id>/', lands.lands),
    path('airbnbs/', bnbs.airbnbs),
    path('airbnbs/<int:id>/', bnbs.airbnbs),
    path('maintenance/', maintenance.maintenance_requests),
    path('maintenance/<int:id>/', maintenance.maintenance_requests),
    path('inquiries/', inquiry.inquiries),
    path('inquiries/<int:id>/', inquiry.inquiries),
    path('appartment_bookings/', booking.appartment_bookings),
    path('appartment_bookings/<int:id>/', booking.appartment_bookings),
    path('cleaners/', cleaners.cleaners),
    path('cleaners/<int:id>/', cleaners.cleaners),
    path('transport/', transport.transport_services),
    path('transport/<int:id>/', transport.transport_services),
    path('community/', communityforum.community_forum_posts),
    path('community/<int:id>/', communityforum.community_forum_posts),
]
