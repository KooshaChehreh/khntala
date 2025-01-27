from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from rest_framework.response import Response
from exceptions import *
from rest_framework import status

class Transaction(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    STATE_SUCCESS = 'S'
    STATAE_PENDING = 'P'
    STATE_FAILED = 'F'

    TRANSACTION_STATUS_CHOICES = [
    (STATE_SUCCESS, 'موفق'),
    (STATAE_PENDING, 'در حال انجام'),
    (STATE_FAILED, 'ناموفق'),
    ]

    state = models.CharField(
        max_length=1,
        choices=TRANSACTION_STATUS_CHOICES,
        default=STATAE_PENDING,
        verbose_name="وضعیت",
    )
    TRANSACTION_TYPE_BUY = 'B'
    TRANSACTION_TYPE_SELL = 'S'

    TRANSACTION_TYPES = [
    (TRANSACTION_TYPE_BUY, 'خرید'),
    (TRANSACTION_TYPE_SELL, 'فروش'),
    ]
    transaction_type = models.CharField(
    max_length=1,
    choices=TRANSACTION_TYPES,
    verbose_name='نوع تراکنش')

    amount_rial = models.PositiveBigIntegerField(default=0, verbose_name="مبلغ")
    gold_weight_gram = models.DecimalField(max_digits=12, decimal_places=4, default=0.0)
    price_per_gram = models.DecimalField(max_digits=12, decimal_places=4, default=settings.PRICE_PER_GRAM_RIALS)
    note = models.CharField(
        max_length=256, blank=True, null=True, verbose_name="یادداشت"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
        

    class Meta:
        verbose_name = "تراکنش"
        verbose_name_plural = "تراکنش‌ها"
        ordering = ["-id"]
