Currently set to test for JESUS coin. 

# MAKE EXPORT ENVIRONMENTALS
#twilio
account_sid = X
auth_token = X
#twilio pohone
from_number = X
to_number = X

from requests import Request, Session
import json
from twilio.rest import Client

def getInfo():  # Function to get the info
    # coinmarketcap
    #Make Environmental
    coinmarketkey = X

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'  # Coinmarketcap API url
    #SET TO JESUS COIN CURRENTLY
    parameters = {'slug': 'jesus',
                  'convert': 'USD'}  # API parameters to pass in for retrieving specific cryptocurrency data

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': coinmarketkey
    }  # Replace 'YOUR_API_KEY' with the API key you have recieved in the previous step

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)

    info = json.loads(response.text)
    json_object = json.dumps(info)
    print(json_object)
    jesus_coin = info["data"]["25526"]["quote"]["USD"]["price"]
    twentyfourhour = info["data"]["25526"]["quote"]["USD"]["percent_change_24h"]
    return float(jesus_coin), float(abs(twentyfourhour)), float(twentyfourhour)


# Retrieving info from getInfo() function
coin_info, twentyfourhourinfoabs, twentyfourhourinfo = getInfo()

# Removing scientific notation
suppressedNum = f"{coin_info:.20f}"

# Indicate Positive/Negative percentage change of coin
if twentyfourhourinfo >= 0:
    marker = "🔺"
else:
    marker = "🔻"

# Set and test correct message body for text
body_text = f"The price of JESUS coin is ${coin_info}, or ${suppressedNum}." \
            f" The 24 hour change is {marker}{twentyfourhourinfoabs}%"
print(body_text)

# # USE ENVIRONMENTALS. Phone call from twilio. Commented out for test purposes.
# client = Client(account_sid, auth_token)
# message = client.messages \
#     .create(
#     body=body_text,
#     from_=from_number,
#     to=to_number,
# )
#
# # Check twilio text status
# print(message.status)
