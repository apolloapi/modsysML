from django.db import models
from django.utils import timezone

# from apolloapi.api import mixins
# from apolloapi.api.models import Organization, User
from apolloapi.common.utils import str_uid
from apolloapi.integrations import choices, mixins


class Integration(
    mixins.FirebaseIntegrationMixin,
    mixins.DatabaseIntegrationMixin,
    mixins.RestfulIntegrationMixin,
    models.Model,
):
    id = models.UUIDField(
        primary_key=True, unique=True, default=str_uid, editable=False
    )
    # organization = models.ForeignKey(
    #     to=Organization, on_delete=models.CASCADE, editable=False
    # )
    # user = models.ForeignKey(to=User, on_delete=models.CASCADE, editable=False)
    resourceName = models.CharField(max_length=100, unique=True, null=False)
    resourceType = models.CharField(
        max_length=100, choices=choices.IntegrationType.choices
    )
    resourcePrefix = models.CharField(
        max_length=100, choices=choices.IntegrationPrefix.choices
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.resourcePrefix} Integration: {self.resourceName}, {self.resourceType}, {self.created_at}"

    def save(self, *args, **kwargs):
        super(Integration, self).save(*args, **kwargs)
