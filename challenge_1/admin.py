from django.contrib import admin
from .models import Pet, Auction, Bid


admin.site.register(Pet)
admin.site.register(Auction)
admin.site.register(Bid)
