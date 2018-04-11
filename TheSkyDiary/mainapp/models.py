from django.db import models

import os


# Create your models here.


class Skies(models.Model):
    diary_date = models.DateField()
    print_proof = models.ImageField(upload_to='images/')
    watermarked_proof = models.ImageField(upload_to='images/')
    purchases = models.IntegerField(default=0)  # might get rid of this

    def __str__(self):      # this is for the admin panel
        return str(self.diary_date)  # this will show up in the admin panel instead of "object skies"

    def proof_filename(self):
        return os.path.basename(self.watermarked_proof.name)


class Request(models.Model):
    email = models.CharField(max_length=40)
    diary_date = models.DateField()
    email_sent = models.BooleanField()


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=20)
    notes = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Orders(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    date = models.DateField()
    items = models.CharField(max_length=100) # is this correct?
    # invoice sent
    # invoice paid
    # order sent

    def __str__(self):
        return self.customer_id


class Order_items(models.Model):
    sky_id = models.CharField(max_length=20)
    order_number = models.ForeignKey(Orders, on_delete=models.PROTECT)
    # This should allow multiple skies to be ordered on one order.

    def __str__(self):
        return self.sky_id
