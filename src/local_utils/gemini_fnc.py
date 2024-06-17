import google.generativeai as genai
import time

genai.configure(api_key="AIzaSyBwqb5jULNdM_DbHsv3lHAB6BkB2ZmwAOw")

print("Gemini functions loaded")


def get_opportunity(review):
    time.sleep(31)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("As a entreprenure and business founder, what is the best business opportunity you can find from this text. " + review + ". Write the output in just 30 words.")
    return response.text