import firebase_admin
from firebase_admin import credentials, firestore


def create_firestore_client():

    cred = credentials.Certificate(
        "credentials/firebase-service-account.json"
    )

    firebase_admin.initialize_app(cred)

    return firestore.client()