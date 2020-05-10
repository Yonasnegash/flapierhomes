from django.urls import path, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register("listingsapi", views.ListingAPI)

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('', include(router.urls))
]