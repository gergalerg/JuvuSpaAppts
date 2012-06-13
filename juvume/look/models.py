from django.db import models
from datetime import datetime, timedelta


ONE_DAY = timedelta(days=1)
DATE_FORMAT = '%m/%d/%Y'
'05/15/2012'


class Spa(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
     
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Procedure(models.Model):
    spa = models.ForeignKey(Spa)
    procedure = models.CharField(max_length=100)
    price = models.IntegerField()

    def __unicode__(self):
        return self.procedure

class Amenities(models.Model):
    spa = models.ManyToManyField(Spa)
    amenities = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Amenities"

    def __unicode__(self):
        return self.amenities


class Availability(models.Model):
    TIMES = (
            ('900a', '9:00 am'),
            ('930a', '9:30 am'),
            ('1000a', '10:00 am'),
            ('1030a', '10:30 am'),
            ('1100a', '11:00 am'),
            ('1130a', '11:30 am'),
            ('1200p', '12:00 pm'),
            ('1230p', '12:30 pm'),
            ('100p', '1:00 pm'),
            ('130p', '1:30 pm'),
            ('200p', '2:00 pm'),
            ('230p', '2:30 pm'),
            ('300p', '3:00 pm'),
            ('330p', '3:30 pm'),
            ('400p', '4:00 pm'),
            ('430p', '4:30 pm'),
            ('500p', '5:00 pm'),
            ('530p', '5:30 pm'),
            ('600p', '6:00 pm'),
            ('630p', '6:30 pm'),
            ('700p', '7:00 pm'),
            ('730p', '7:30 pm'),
            ('800p', '8:00 pm'),
            ('830p', '8:30 pm'),
            ('900p', '9:00 pm'),
            )
    availability = models.CharField(max_length=10, choices = TIMES)
    procedure = models.ManyToManyField(Procedure)
    spa = models.ForeignKey(Spa)

    class Meta:
        verbose_name_plural = "Availability"


    
#def get_results(proc, from_date, to_date):
#    print 'get_results', proc, from_date, to_date
#    days = list(_get_days(from_date, to_date))
#    for d in days:
#        print '  ', d
#    print
#    return FAKE_RESULTS.values()[0]

def _get_days(from_date, to_date):
    if from_date:
        from_date = datetime.strptime(from_date, DATE_FORMAT)
    else:
        from_date = datetime.today()
    if to_date:
        to_date = datetime.strptime(to_date, DATE_FORMAT)
    else:
        to_date = from_date
    if to_date < from_date:
        to_date, from_date = from_date, to_date
    while from_date <= to_date:
        yield from_date
        from_date += ONE_DAY
