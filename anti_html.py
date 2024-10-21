import requests
from bs4 import BeautifulSoup
import sys

def download_and_strip_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        stripped_text = soup.get_text(separator='\n')  
        print(stripped_text)
        
    except Exception as e:
        print(f"Error fetching the URL: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python anti_html.py <URL>")
    else:
        url = sys.argv[1]
        download_and_strip_html(url)
