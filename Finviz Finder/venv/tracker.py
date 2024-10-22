import requests_html
import requests








url = 'https://discord.com/api/webhooks/777926340464607242/R65q3AwLzi7_S6jzi0-emTfyq6y_yHQ52szyH9p2Hs2AXcZ3SAiVIfFzBxqw3s3VXl2i'
values = {
    'username': 'StockBot',
    'content': 'Test'
}

requests.post(url,data=values)


