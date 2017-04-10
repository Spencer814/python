from twilio.rest import TwilioRestClient

account_sid = "AC96c0b802992d6be252d7eea92c12f816"
auth_token = "cd0c3314c7335f7584b16c3f947f47cb"

client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    to="+17576204752",
    from_="+17576376692",
    body="This is the ship that made the Kessel Run in fourteen parsecs?",
    media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg")
    
print message.sid