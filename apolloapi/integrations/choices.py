from django.db import models


class IntegrationType(models.TextChoices):
    POSTGRES = "Postgres"
    FIREBASE = "Firebase"
    REST = "Rest"


class RESTType(models.TextChoices):
    POST = "Post"
    PATCH = "Patch"
    PUT = "Put"
    DELETE = "Delete"
    GET = "Get"


class APIAuthType(models.TextChoices):
    NONE = "None"
    BASIC = "Basic_auth"


class IntegrationPrefix(models.TextChoices):
    CLI="CLI"
