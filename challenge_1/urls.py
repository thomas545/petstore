from django.urls import path, include
from . import views


urlpatterns = [
    path('<int:pk>/bids/', views.BidAPIView.as_view(), name="all_bids"),
    path('<int:pk>/bid/', views.BidAPIView.as_view(), name="add_bid"),
]
