from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client()

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+15005550006'

client.messages.create(body='HI THERE, this is to let you know that we have recognized your face and launched an ec2 instance',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
