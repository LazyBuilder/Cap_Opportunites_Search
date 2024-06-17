

from bs4 import BeautifulSoup  # For parsing HTML content (optional)
import requests

print("Scrapping functions loaded")


def process_page_response(final_url):
    
    rsp = requests.get(final_url)
    
    if rsp.status_code == 200:
        soup = BeautifulSoup(rsp.content, "html.parser")
        data_elements = soup.find_all("div", class_="review-card") 
        print("# of Reviews Found : " + str(len(data_elements)))
        return len(data_elements),data_elements
    else:
        return 0, "Error: Scrapping failed"





