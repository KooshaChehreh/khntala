from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user_id",
        "state",
        "transaction_type",
        "amount",
        "gold_amount_gr",
        "note",
        "created_at",
        "updated_at",
    ]
    list_filter = [
        "created_at",
    ]
