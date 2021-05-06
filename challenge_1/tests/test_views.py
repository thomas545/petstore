from datetime import timedelta
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from model_bakery import baker
from ..models import Pet, Auction, Bid


class TestBidAPIView(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="petstore", password="Pet@12Store")
        self.bidder = User.objects.create(username="petbidder", password="Pet@12Store")
        self.pet = baker.make(Pet, name="CAT", user=self.user)
        self.auction = baker.make(
            Auction,
            pet=self.pet,
            start_at=timezone.now(),
            end_at=timezone.now() + timedelta(days=3),
        )
        self.bids = baker.make(Bid, auction=self.auction, user=self.bidder, _quantity=5)

    def test_get_bids(self):
        url = reverse("all_bids", kwargs={"pk": self.pet.pk})
        self.client.force_authenticate(self.user)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), len(self.bids))

    def test_get_bids_with_bidder(self):
        url = reverse("all_bids", kwargs={"pk": self.pet.pk})
        self.client.force_authenticate(self.bidder)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.data.get("detail"), "Pet doen't belong to you.")

    def test_add_bid(self):
        url = reverse("all_bids", kwargs={"pk": self.pet.pk})
        self.client.force_authenticate(self.bidder)

        data = {"amount": 200}
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get("message"), "Your bid added successfully!")

    def test_add_bid_with_owner(self):
        url = reverse("all_bids", kwargs={"pk": self.pet.pk})
        self.client.force_authenticate(self.user)

        data = {"amount": 200}
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.data.get("detail"), "Pet is belong to you.")
