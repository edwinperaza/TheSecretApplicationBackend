from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel


class Language(BaseModel):
    name = models.CharField(
        _('name'),
        max_length=50,
    )

    def __str__(self):
        return self.name
