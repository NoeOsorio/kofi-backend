import firebase_admin
import os
from firebase_admin import credentials, firestore

print(os.getcwd())
dir_path = os.path.dirname(os.path.realpath(__file__))
cred_path = os.path.join(dir_path, 'firebase_settings.json')
print(cred_path)
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

db = firestore.client()
