from datetime import timedelta
from django.utils import timezone
from challenge_1.models import Auction


def get_create_auction(pet):
    start_at = timezone.now()
    end_at = start_at + timedelta(days=3)
    auction = Auction.objects.filter(pet=pet, end_at__date__gte=timezone.now().date())
    if not auction.exists():
        auction = Auction.objects.create(pet=pet, start_at=start_at, end_at=end_at)
    else:
        auction = auction.first()
    return auction
