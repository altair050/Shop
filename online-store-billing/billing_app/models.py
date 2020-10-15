from django.db import models
import uuid


class Billing(models.Model):
    CARD = 'Card'
    CASH = 'Cash'
    PAYMENT_METHOD = [
        (CARD, 'Card'),
        (CASH, 'Cash')
    ]
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_method = models.CharField(choices=PAYMENT_METHOD, default=CASH, max_length=4)
    address = models.CharField(default='', blank=False, max_length=150)
    telephone_number = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return f'{self.uuid}, payment_method: {self.payment_method}, address: {self.address} \
               , telephone_number: {self.telephone_number}'
