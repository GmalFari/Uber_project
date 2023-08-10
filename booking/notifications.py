import firebase_admin
from firebase_admin import messaging, credentials
from base_site import settings


cred = credentials.Certificate(settings.cred_path)
firebase_admin.initialize_app(cred)

def sendnotifications(trip_type,pickup_location,drop_location):
    message = messaging.MulticastMessage(
        notification=messaging.Notification(trip_type=trip_type, pickup_location=pickup_location)
    )

    response = messaging.send_multicast(message)
    print("Notification sent", response)
