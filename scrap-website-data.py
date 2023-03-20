from bs4 import BeautifulSoup
import requests

# Replace with the URL of the website you want to scrape
url = "https://example.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Vivaldi/1.8.770.50"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")
data = soup.get_text()

# Remove blank lines from the scraped data
data = "\n".join([line.strip() for line in data.split("\n") if line.strip()])

# Save the scraped data into a text file
with open("scraped_data.txt", "w") as file:
    file.write(data)

print("Data saved to scraped_data.txt")
