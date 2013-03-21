from django.db import models

# Create your models here.

class Spa(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Procedure(models.Model):
    spa = models.ForeignKey(Spa)
    procedure = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()

    def __unicode__(self):
        return self.procedure

class Availibility(models.Model):
    procedure = models.ForeignKey(Procedure)
    spa = models.ForeignKey(Spa)
    date = models.DateField()

    class Meta:
        verbose_name_plural = "Availability"
