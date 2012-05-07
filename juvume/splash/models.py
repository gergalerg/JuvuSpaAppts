from django.http import HttpResponse
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib import admin


class Emails(models.Model):
    email = models.EmailField(max_length=200)

    def __unicode__(self):
        return u'<"%s">' % self.email

admin.site.register(Emails)

def proc_email(email_addy, log):
    log.info('Processing: %r', email_addy)

    try:
        em = Emails.objects.get(email=email_addy)

    except Emails.DoesNotExist:
        log.info('New email: %r', email_addy)
        em = Emails(email=email_addy)
        try:
            em.clean_fields()
        except ValidationError:
            log.warning('Invalid address: %r', em)
        else:
            em.save()
            log.info('Created: %s', em)

    else:
        log.info('Duplicate email: %s', em)

    return HttpResponse(
        "%r, please." % (email_addy,),
        mimetype="text/plain"
        )
