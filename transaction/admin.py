from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user_id",
        "state",
        "transaction_type",
        "amount_rial",
        "gold_weight_gram",
        "price_per_gram",
        "note",
        "created_at",
        "updated_at",
    ]
    list_filter = [
        "created_at",
    ]
