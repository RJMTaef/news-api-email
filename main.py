import requests

api = "4cff20706e5f453aa5d376eb35f88618"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024" \
      "-08-11&sortBy=publishedAt&apiKey=4cff" \
      "20706e5f453aa5d376eb35f88618"

# Make request
request = requests.get(url)

# Get a dictionary
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])