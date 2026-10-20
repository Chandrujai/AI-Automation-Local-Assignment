import requests
from bs4 import BeautifulSoup

# 1. Target URL for BBC News
url = "https://www.bbc.com/news"

# 2. Add realistic browser headers so BBC doesn't block the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("Fetching BBC News homepage...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # 3. Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # 4. BBC frequently puts main headings inside h2 or h3 tags
    # Let's search for h2 tags which typically hold major story headlines on BBC
    headline_tags = soup.find_all("h2")

    print("\n--- Top BBC News Headlines ---")
    count = 0
    
    for tag in headline_tags:
        text = tag.get_text().strip()
        # Filter out empty strings or short UI menu labels
        if len(text) > 20: 
            count += 1
            print(f"{count}. {text}")
            if count >= 5:  # Stop after getting top 5
                break
                
    if count == 0:
        print("No headlines found. The website layout might have changed.")
else:
    print(f"Failed to access BBC. Status code: {response.status_code}")