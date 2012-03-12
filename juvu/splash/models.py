from django.http import HttpResponse
from django.db import models
from django.core.exceptions import ValidationError


class Emails(models.Model):
    email = models.EmailField(max_length=200)

    def __unicode__(self):
        return u'<"%s">' % self.email


def proc_email(email_addy):
    print 'Processing:', email_addy

    try:
        em = Emails.objects.get(email=email_addy)

    except Emails.DoesNotExist:
        print 'New email:', repr(email_addy)
        em = Emails(email=email_addy)
        try:
            em.clean_fields()
        except ValidationError:
            print 'Invalid address:', em
        else:
            em.save()
            print 'Created:', em

    else:
        print 'Duplicate email:', em

    return HttpResponse(
        "%r, please." % (email_addy,),
        mimetype="text/plain"
        )
