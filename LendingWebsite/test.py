from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACc4152bd9de2f520ae656332a28bd392d'
auth_token = 'bb4a0a679dfa26f78e666a997a105066'
client = Client(account_sid, auth_token)

account = client.api.accounts.create()

print(account.subresource_uris)