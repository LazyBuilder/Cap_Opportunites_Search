import requests

from local_utils import op_fnc
from local_utils import scrapping_fnc
from local_utils import gemini_fnc

import os

print(os.getcwd())

op_fnc.write_log("Starting new instance")

op_fnc.write_log("Starting new instance")

company = "logility-voyager-solutions"
url = "https://www.capterra.ca/reviews/172888/" + company + "?page="
i = 1

op_fnc.write_log("Getting data for " + company)

while True:
    final_url = url + str(i)
    
    print("Scrapping : " + final_url)
    
    op_fnc.write_log(final_url)
    
    len_reviews, output_content = scrapping_fnc.process_page_response(final_url)
    
    opportunity = ""
    
    if len_reviews>0:
        print("Scrapping successful.")
        op_fnc.write_log("Scrape success : " + str(len_reviews))
        for index, element in enumerate(output_content):
            print("Processing review : ",(index + 1))
            opportunity += str(index + 1) + " - " + gemini_fnc.get_opportunity(element.text.strip())
        
    else:
        print(output_content)
        break
    
    i += 1
    