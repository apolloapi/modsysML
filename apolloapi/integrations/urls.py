# from django.urls import path

# from core.integrations.database.views import (
#     IntegrationDatabasePostgresView,
#     IntegrationDatabaseFirebaseView,
# )
# from core.integrations.service.views import IntegrationRestfulView
# from core.integrations.views import IntegrationDetailView, IntegrationView

# urlpatterns = [
#     path("integrations/", IntegrationView.as_view(), name="integrations"),
#     path("integrations/<uuid:pk>/", IntegrationDetailView.as_view()),
#     path("integrations/new/postgresql/", IntegrationDatabasePostgresView.as_view()),
#     path("integrations/new/firebase/", IntegrationDatabaseFirebaseView.as_view()),
#     path("integrations/new/rest_api/", IntegrationRestfulView.as_view()),
# ]
