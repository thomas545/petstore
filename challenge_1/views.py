from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import views, permissions, status
from rest_framework.exceptions import NotAcceptable
from rest_framework.response import Response

from .models import Auction, Bid, Pet
from challenge_1.serializers import BidSerializer
from .utils import get_create_auction


class BidAPIView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, *args, **kwargs):
        # get all bids for owner
        current_user = request.user
        pet = get_object_or_404(Pet, pk=pk)

        if pet.user != current_user:
            raise NotAcceptable("Pet doen't belong to you.")

        auction = pet.auctions.filter(end_at__gte=timezone.now())
        bids = auction.first().auction_bids
        serializer = BidSerializer(instance=bids, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk, *args, **kwargs):
        current_user = request.user
        pet = get_object_or_404(Pet, pk=pk)

        if pet.user == current_user:
            raise NotAcceptable("Pet is belong to you.")

        auction = get_create_auction(pet)
        serializer = BidSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=current_user, auction=auction)

        return Response(
            {"message": "Your bid added successfully!"}, status=status.HTTP_201_CREATED
        )
