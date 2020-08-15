from django.db import models
from django.db.models import Q

class AliasManager(models.Manager):
    def get_by_natural_key(self, alias):
        return self.get(alias=alias)

    def get_safe(self, *args, **kwargs):
        try:
            if args and isinstance(args[0], Q):
                query = args[0]
                return self.get(query)
            if kwargs:
                return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None


class AbstractAuditDatesModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True,
                                       verbose_name="Date/Time when the record has been created")
    update_date = models.DateTimeField(auto_now=True,
                                       verbose_name="Last Date/Time when the record has been updated")

    class Meta:
        """Meta option."""
        abstract = True
        get_latest_by = 'create_date'
        ordering = ['-create_date', '-update_date']


class AliasSlugFieldModel(models.Model):
    alias = models.CharField(max_length=50, unique=True, null=False, blank=False,
                             verbose_name="Unique alias for the record.")

    objects = AliasManager()

    class Meta:
        """Meta option."""
        abstract = True

    def natural_key(self):
        return (
            self.alias,
        )

    def __str__(self):
        return self.alias
