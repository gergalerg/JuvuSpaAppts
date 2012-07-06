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
            ('Therapeutic', 'Therapeutic'),
            ('Thai', 'Thai'),
            ('Hot Stone', 'Hot Stone'),
            ('Reflexology', 'Reflexology'),
            ('Facials', 'Facials'),
            ('Lash Extensions', 'Lash Extensions'),
            ('Lash Tinting', 'Lash Tinting'),
            ('Brow Tinting', 'Brow Tinting'),
            ('Microdermabrasion', 'Microdermabrasion'),
            ('Chemical Peels', 'Chemical Peels'),
            ('Facial Fillers', 'Facial Fillers'),
            ('Laser Facials', 'Laser Facials'),
            ('BOTOX', 'Botox'),
            ('Application', 'Make Up - Application'),
            ('Permanent', 'Make Up - Permanent Makeup'),
            ('Womens Cut', 'Womens Cut'),
            ('Conditioning Treatments', 'Conditioning Treatments'),
            ('Blowout', 'Blowout'),
            ('Updo', 'Updo'),
            ('Extensions', 'Extensions'),
            ('Straightening', 'Straightening'),
            ('Mens Cut', 'Mens Cut'),
            ('Brows/Face', 'Brows/Face'),
            ('Bikini/Brazilian', 'Bikini/Brazilian'),
            ('Body', 'Body'),
            ('Mens', 'Mens'),
            ('Laser', 'Laser'),
            ('Threading', 'Threading'),
            ('Sugaring', 'Sugaring'),
            ('Electrolysis', 'Electrolysis'),
            ('Pedicure', 'Pedicure'),
            ('Manicure', 'Manicure'),
            ('Mani/pedi', 'Mani/pedi'),
            ('Polish Change', 'Polish Change'),
            ('Gels', 'Gels'),
            ('Acrylics', 'Acrylics'),
            ('Yoga', 'Yoga'),
            ('Pilates', 'Pilates'),
            ('Cross Training Classes', 'Cross Training Classes'),
            ('Cycling Classes', 'Cycling Classes'),
            ('TRX', 'TRX'),
            ('Flexibility/Stretching Classes', 'Flexibility/Stretching Classes'),
            ('Outdoor Bootcamp', 'Outdoor Bootcamp'),
            ('Abs & Targeted Area Classes', 'Abs & Targeted Area Classes'),
            ('Personal Training', 'Personal Training'),
            ('Chiropractic', 'Chiropractic'),
            ('Acupuncture', 'Acupuncture'),
            ('Colonics', 'Colonics'),
            ('Weight Loss', 'Weight Loss'),
            ('Spray Tan', 'Tanning - Spray Tan'),
            ('Tanning Beds', 'Tanning - Tanning Beds'),
            ('Scrubs', 'Scrubs'),
            ('Wraps', 'Wraps'),
            ('Back Facials', 'Back Facials'),
            ('Cleaning', 'Dental - Cleaning'),
            ('Whitening', 'Dental - Whitening'),
            )
    category = models.CharField(max_length=50, choices=DECISION_TREE)

    class Meta:
        verbose_name_plural = "Category"

    def __unicode__(self):
        return self.category

class Procedure(models.Model):
    DECISION_TREE = (
            ('Therapeutic', 'Therapeutic'),
            ('Thai', 'Thai'),
            ('Hot Stone', 'Hot Stone'),
            ('Reflexology', 'Reflexology'),
            ('Facials', 'Facials'),
            ('Lash Extensions', 'Lash Extensions'),
            ('Lash Tinting', 'Lash Tinting'),
            ('Brow Tinting', 'Brow Tinting'),
            ('Microdermabrasion', 'Microdermabrasion'),
            ('Chemical Peels', 'Chemical Peels'),
            ('Facial Fillers', 'Facial Fillers'),
            ('Laser Facials', 'Laser Facials'),
            ('BOTOX', 'Botox'),
            ('Application', 'Make Up - Application'),
            ('Permanent', 'Make Up - Permanent Makeup'),
            ('Womens Cut', 'Womens Cut'),
            ('Conditioning Treatments', 'Conditioning Treatments'),
            ('Blowout', 'Blowout'),
            ('Updo', 'Updo'),
            ('Extensions', 'Extensions'),
            ('Straightening', 'Straightening'),
            ('Mens Cut', 'Mens Cut'),
            ('Brows/Face', 'Brows/Face'),
            ('Bikini/Brazilian', 'Bikini/Brazilian'),
            ('Body', 'Body'),
            ('Mens', 'Mens'),
            ('Laser', 'Laser'),
            ('Threading', 'Threading'),
            ('Sugaring', 'Sugaring'),
            ('Electrolysis', 'Electrolysis'),
            ('Pedicure', 'Pedicure'),
            ('Manicure', 'Manicure'),
            ('Mani/pedi', 'Mani/pedi'),
            ('Polish Change', 'Polish Change'),
            ('Gels', 'Gels'),
            ('Acrylics', 'Acrylics'),
            ('Yoga', 'Yoga'),
            ('Pilates', 'Pilates'),
            ('Cross Training Classes', 'Cross Training Classes'),
            ('Cycling Classes', 'Cycling Classes'),
            ('TRX', 'TRX'),
            ('Flexibility/Stretching Classes', 'Flexibility/Stretching Classes'),
            ('Outdoor Bootcamp', 'Outdoor Bootcamp'),
            ('Abs & Targeted Area Classes', 'Abs & Targeted Area Classes'),
            ('Personal Training', 'Personal Training'),
            ('Chiropractic', 'Chiropractic'),
            ('Acupuncture', 'Acupuncture'),
            ('Colonics', 'Colonics'),
            ('Weight Loss', 'Weight Loss'),
            ('Spray Tan', 'Tanning - Spray Tan'),
            ('Tanning Beds', 'Tanning - Tanning Beds'),
            ('Scrubs', 'Scrubs'),
            ('Wraps', 'Wraps'),
            ('Back Facials', 'Back Facials'),
            ('Cleaning', 'Dental - Cleaning'),
            ('Whitening', 'Dental - Whitening'),
            )

    category = models.CharField(max_length=50, choices=DECISION_TREE)
    spa = models.ForeignKey(Spa)
    procedure = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    #category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.procedure

class Availability(models.Model):

    STATUS =(
            (0,'Available'),
            (1,'Booked'),
            (2,'Completed'),
            (3,'No Show')
            )

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
    status = models.IntegerField(choices=STATUS) 
    base_price = models.IntegerField()
    proc_name = models.ForeignKey(Procedure, related_name='Procedure')
    create_date = models.DateField()
    staff_id = models.IntegerField()
    customer_id = models.IntegerField(default=0, null=True)
   
    class Meta:
        verbose_name_plural = "Availability"

