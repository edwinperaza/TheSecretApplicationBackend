from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel


class Objective(BaseModel):
    user = models.ForeignKey(
        'users.User',
        related_name='objectives',
        null=True,
        blank=False,
        verbose_name=_('user'),
        on_delete=models.SET_NULL,
    )
    title = models.CharField(
        _('title'),
        max_length=50,
    )
    description = models.TextField(
        _('description'),
    )
    until_date = models.DateField(
        _('until_date'),
    )

    def __str__(self):
        return self.title
