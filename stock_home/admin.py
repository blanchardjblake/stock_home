"""Admin."""
from django.contrib import admin

from stock_home.models import Company, Position, Transaction

admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Transaction)
