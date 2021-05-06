from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from model_bakery import baker
from ..models import Pet, Auction, Bid


class TestAPI(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="petstore", password="Pet@12Store")
        self.bidder = User.objects.create(username="petbidder", password="Pet@12Store")


class TestPet(TestAPI):
    def test_create_pet(self):
        name = "Cat"
        pet = baker.make(Pet, name=name, user=self.user)
        self.assertEqual(pet.__str__(), name)


class TestAuction(TestAPI):
    def test_create_auction(self):
        name = "Cat"
        pet = baker.make(Pet, name=name, user=self.user)
        auction = baker.make(Auction, pet=pet)
        self.assertEqual(auction.__str__(), name)


class TestBid(TestAPI):
    def test_create_Bid(self):
        name = "Cat"
        pet = baker.make(Pet, name=name, user=self.user)
        auction = baker.make(Auction, pet=pet)
        bid = baker.make(Bid, auction=auction, user=self.bidder)
        self.assertEqual(bid.__str__(), self.bidder.username)
