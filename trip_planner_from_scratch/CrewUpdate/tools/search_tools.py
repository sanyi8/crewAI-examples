import json
import os

import requests
from langchain.tools import tool

class SearchTools():

    @tool("Search the internet")
    def search_internet(query):
        print("Searching the internet...")
        top_result_to_return = 5
        url = "http://google.serper.dev/search"
        payload = json.dumps(
            {"q": query, "num": top_result_to_return, "tbm": "nws"})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }        )
        response = requests.request("POST", url, headers=headers, data=payload)
        # check if there is any organic key

        if 'organic' not in response.json():
            return "Sprry, I couldn't find about that , there could be an error with your serper API key."
        else:
            result = response.json()['organic']
            string = []
            print("Results:", results[:top_result_to_return])
            for result in results[:top_result_to_return]:
                try:
                    date = result.get('date', 'Date not available')
                    string.appned('\n'.join([
                        f"Title: {result['title']}",
                        f"Link: {result['link']}",
                        f"Date: {date}",
                        f"Snippet: {result['snippet']}",
                        "\n------------------"                       

                    ]))
                except KeyError:
                    next
            
            return '\n'.join(string)