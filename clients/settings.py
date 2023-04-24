from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

POSTGRES_CLIENT_CLASS = os.environ.get(
    "POSTGRES_CLIENT_CLASS", "clients.postgresql.PostgresClient"
)

FIREBASE_CLIENT_CLASS = os.environ.get(
    "FIREBASE_CLIENT_CLASS", "clients.firebase.FirebaseClient"
)

API_CLIENT_CLASS = os.environ.get("API_CLIENT_CLASS", "clients.service.APIClient")
