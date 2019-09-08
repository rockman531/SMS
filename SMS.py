from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACab526c0a3da5f641ee6eb67c782cfd56"
# Your Auth Token from twilio.com/console
auth_token  = "1815beae03503d5caf82d1b64e46c9af"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+886956820214", 
    from_="+19199260109",
    body="寄簡訊囉")

print(message.sid)
