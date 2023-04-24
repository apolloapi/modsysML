from django.db import models


class ContentTypesType(models.TextChoices):
    STRING = "String"
    FLOAT = "Float"
    INTEGER = "Integer"
    IMAGE = "Image"
    AUDIO = "Audio"
    VIDEO = "Video"
