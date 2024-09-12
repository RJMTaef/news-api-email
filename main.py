import requests
from send_email import send_email

topic = "tesla"

api = "4cff20706e5f453aa5d376eb35f88618"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-08-11&sortBy=publishedAt&apiKey=4cff" \
      "20706e5f453aa5d376eb35f88618&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary
content = request.json()

body = ""
# Access the article titles and description
for article in content["articles"][:20]:
    if article["title"] is  not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + \
               article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)