import requests
from bs4 import BeautifulSoup
from playsound import playsound
import time

# Function to check if the URL is accessible
def check_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        h1_tags = soup.find_all('h1')
        for tag in h1_tags:
            if "404, Page Not Found." in tag.text:
                return False  # If the specified text is found in any h1 tag, consider the page as unavailable
        return True  # If the text is not found in any h1 tag, consider the page as available
    except requests.RequestException:
        return False

# URL you want to check
url = "https://www.subber.xyz/midcoin/wallet-collection/3rd-mid-snapshot"  # Replace this with your URL

# Loop until the URL is available
while not check_url(url):
    print("URL is not available or contains a '404, Page Not Found.' message. Waiting for 5 seconds before checking again...")
    time.sleep(60)  # Wait for 5 seconds before checking again

# Once the URL is available, play the MP3 music
print("URL is available! Playing the music...")
playsound("02-chemical_brothers-it_began_in_afrika-ego.mp3")  # Replace this with the path to your MP3 audio file
