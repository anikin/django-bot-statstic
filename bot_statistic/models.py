from django.db import models
from django.utils.translation import ugettext_lazy as _

BOTS = (
    ('y', 'yandex'),
    ('g', 'google')
)


class LogItem(models.Model):

    bot = models.CharField(_(u'bot'), max_length=1, choices=BOTS)
    log_date = models.DateTimeField(_('log date'))
    url = models.CharField(_(u'url'), max_length=255)

    def __unicode__(self):
        return self.bot

    class Meta:
        verbose_name = _(u'log item')
        verbose_name_plural = _(u'log items')
        ordering = ['-log_date']
