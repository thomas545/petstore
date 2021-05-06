from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    user = models.ForeignKey(User, related_name="pets", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    photo_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Auction(models.Model):
    pet = models.ForeignKey(
        Pet, related_name="auctions", on_delete=models.CASCADE, blank=True, null=True
    )
    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.pet.name


class Bid(models.Model):
    user = models.ForeignKey(User, related_name="user_bids", on_delete=models.CASCADE)
    auction = models.ForeignKey(
        Auction, related_name="auction_bids", on_delete=models.CASCADE
    )
    amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
