import firebase_admin
from firebase_admin import credentials, firestore

def initialize_firebase():

    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred)

    return firestore.client()

db = initialize_firebase()
