from django.db import models

from apolloapi.integrations import choices

# Mixin for firebase integration
class FirebaseIntegrationMixin(models.Model):
    firebase_project_id = models.CharField(
        max_length=200, help_text="Firebase project id", null=True, blank=True
    )
    firebase_database_url = models.CharField(
        max_length=200, help_text="firebase database url", null=True, blank=True
    )
    firebase_service_account_key = models.TextField(
        help_text="service account key", null=True, blank=True
    )

    class Meta:
        abstract = True


# Mixin for Postgres Integration
class DatabaseIntegrationMixin(models.Model):
    connection_string = models.CharField(max_length=200, blank=True, null=True)
    engine = models.CharField(default="", null=True, blank=True, max_length=200)

    class Meta:
        abstract = True


# Mixin for Restful api
class RestfulIntegrationMixin(models.Model):
    apiRequestType = models.CharField(
        max_length=200, choices=choices.RESTType.choices, null=True, blank=True
    )
    queryParam = models.TextField(default="", null=True, blank=True)
    header = models.TextField(default="", null=True, blank=True)
    authType = models.CharField(
        max_length=200, default="none", choices=choices.APIAuthType.choices
    )
    auth = models.TextField(default="", null=True, blank=True)
    base_url = models.TextField(default="", null=True, blank=True)
    jsonBody = models.TextField(default="", null=True, blank=True)
    actionType = models.CharField(
        max_length=200, null=True, blank=True, default=""
    )

    class Meta:
        abstract = True
