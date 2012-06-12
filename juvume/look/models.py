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

class Treatment(models.Model):
    spa = models.ForeignKey(Spa)
    treatment = models.CharField(max_length=100)
    price = models.IntegerField()

    def __unicode__(self):
        return self.treatment

class Amenities(models.Model):
    spa = models.ManyToManyField(Spa)
    amenities = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Amenities"

    def __unicode__(self):
        return self.amenities



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
