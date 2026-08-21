"""Central application configuration.

Keep Firebase's public project configuration here as requested. Private admin
credentials must be supplied by the hosting provider as environment variables.
"""

import os


class Config:
    SECRET_KEY = os.getenv("SESSION_SECRET", "change-this-in-production")

    # Replace these values with the Firebase Web App configuration for your
    # project. Do not put private service-account JSON or passwords in Git.
    FIREBASE_CONFIG = {
        "apiKey": os.getenv("FIREBASE_API_KEY", "replace-me"),
        "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN", "replace-me.firebaseapp.com"),
        "projectId": os.getenv("FIREBASE_PROJECT_ID", "replace-me"),
        "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET", "replace-me.appspot.com"),
        "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID", "replace-me"),
        "appId": os.getenv("FIREBASE_APP_ID", "replace-me"),
        "databaseURL": os.getenv("FIREBASE_DATABASE_URL", ""),
    }

    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024
