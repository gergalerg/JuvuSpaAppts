from django.db import models

# Create your models here.

class Spa(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )

class Category(models.Model):
    DECISION_TREE = (
            ('massage', 'Massage'),
            ('face', 'Face'),
            ('hair', 'Hair'),
            ('hair_removal', 'Hair Removal'),
            ('nails', 'Nails'),
            ('fitness', 'Fitness'),
            ('alternative', 'Alternative'),
            ('body_treatments', 'Body Treatments'),
            ('dental', 'Dental'),
            )
    category = models.CharField(max_length=20, choices=DECISION_TREE)

    class Meta:
        verbose_name_plural = "Category"

    def __unicode__(self):
        return self.category

class Procedure(models.Model):
    spa = models.ForeignKey(Spa)
    procedure = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.procedure

class Availability(models.Model):
    TIMESLOTS = (
            (37, '9:00 am'),
            (38, '9:15 am'),
            (39, '9:30 am'),
            (40, '9:45 am'),
            (41, '10:00 am'),
            (42, '10:15 am'),
            (43, '10:30 am'),
            (44, '10:45 am'),
            (45, '11:00 am'),
            (46, '11:15 am'),
            (47, '11:30 am'),
            (48, '11:45 am'),
            (49, '12:00 pm'),
            (50, '12:15 pm'),
            (51, '12:30 pm'),
            (52, '12:45 pm'),
            (53, '1:00 pm'),
            (54, '1:15 pm'),
            (55, '1:30 pm'),
            (56, '1:45 pm'),
            (57, '2:00 pm'),
            (58, '2:15 pm'),
            (59, '2:30 pm'),
            (60, '2:45 pm'),
            (61, '3:00 pm'),
            (62, '3:15 pm'),
            (63, '3:30 pm'),
            (64, '3:45 pm'),
            (65, '4:00 pm'),
            (66, '4:15 pm'),
            (67, '4:30 pm'),
            (68, '4:45 pm'),
            (69, '5:00 pm'),
            (70, '5:15 pm'),
            (71, '5:30 pm'),
            (72, '5:45 pm'),
            (73, '6:00 pm'),
            (74, '6:15 pm'),
            (75, '6:30 pm'),
            (76, '6:45 pm'),
            (77, '7:00 pm'),
            (78, '7:15 pm'),
            (79, '7:30 pm'),
            (80, '7:45 pm'),
            (81, '8:00 pm'),
            (82, '8:15 pm'),
            (83, '8:30 pm'),
            (84, '8:45 pm'),
            )

            
    procedure = models.ForeignKey(Procedure)
    appt_date = models.DateField("Appointment Date")
    spa = models.ForeignKey(Spa)
    timeslot = models.IntegerField(choices=TIMESLOTS)
    duration = models.IntegerField()
    status = models.IntegerField() # "0" for available. "1" for booked.">1" ID
    base_price = models.IntegerField()
    proc_name = models.ForeignKey(Procedure, related_name='Procedure')
    create_date = models.DateField()
    staff_id = models.IntegerField()

    class Meta:
        verbose_name_plural = "Availability"

