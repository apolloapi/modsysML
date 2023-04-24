from django.contrib import admin

from apolloapi.integrations.models import Integration
from apolloapi.common.exceptions import IntegrationCreationError

import logging


logger = logging.getLogger(__name__)


@admin.register(Integration)
class IntegrationAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

    def save_model(self, request, obj, form, change):

        try:
            if not obj.user_id:
                obj.user = (
                    request.user
                )  # Set the user field to the currently logged-in user

            logger.info("Saving integration for user, %s", str(obj.user))
            obj.save()
        except Exception as err:
            logger.error(
                "There was an error saving the integration for the user, %s",
                str(obj.user),
            )
            raise IntegrationCreationError(err)
