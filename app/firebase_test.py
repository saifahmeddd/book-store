import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(
    "../credentials/firebase-service-account.json"
)

firebase_admin.initialize_app(cred)
db=firestore.client()

print("Firebase connected successfully!")

book_ref = db.collection("books").add({
    "title": "Clean Code",
    "price": 30
})

print("Book created!")
print(book_ref)