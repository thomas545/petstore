from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from model_bakery import baker
from ..models import Pet, Auction, Bid
from ..serializers import BidSerializer


class TestBidSerializer(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="petstore", password="Pet@12Store")
        self.bidder = User.objects.create(username="petbidder", password="Pet@12Store")

    def test_bid_serializer(self):
        name = "Cat"
        pet = baker.make(Pet, name=name, user=self.user)
        auction = baker.make(Auction, pet=pet)
        bid = baker.make(Bid, auction=auction, user=self.bidder)
        serializer = BidSerializer(instance=bid)

        self.assertNotEqual(serializer.data, {})
        self.assertEqual(serializer.data.get("auction"), auction.id)
        self.assertEqual(serializer.data.get("amount"), bid.amount)
