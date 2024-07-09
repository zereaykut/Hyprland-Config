#!/usr/bin/python
import subprocess as sp
import sys

class SearchEngineLauncher:
    def __init__(self):
        self.search_urls = {
            "dd": "https://duckduckgo.com/?q=",
            "bb": "https://search.brave.com/search?q=",
            "rr": "https://www.reddit.com/search/?q=",
            "ww": "https://en.wikipedia.org/w/index.php?search=",
            "pp": "https://docs.python.org/3/search.html?q=",
            "gg": "https://www.google.com/search?q=",
            "yu": "https://www.youtube.com/results?search_query=",
            "yt": "https://yts.mx/browse-movies/"
        }

    def get_rofi_input(self):
        rofi_search_input = sp.run(
            """rofi -dmenu""", shell=True, capture_output=True, text=True, check=False
        )
        return rofi_search_input.stdout

    def open_search_url(self, search_input):
        search_url_key = search_input[:2]
        search_query = search_input[2:].strip().replace(" ", "+")
        if search_url_key in self.search_urls:
            sp.run(f"""xdg-open {self.search_urls[search_url_key]}{search_query}""", shell=True, check=False)
        else:
            sys.exit()

    def run(self):
        rofi_search = self.get_rofi_input()
        self.open_search_url(rofi_search)


if __name__ == "__main__":
    launcher = SearchEngineLauncher()
    launcher.run()
