#!/usr/bin/python
import subprocess as sp
import sys
import json

class SearchEngineLauncher:
    def __init__(self):
        self.user = sp.run("whoami", shell=True, capture_output=True, text=True).stdout.strip()
        with open(f"/home/{self.user}/.config/rofi/scripts/web_search.json", "r") as f:
            self.search_urls = json.load(f)

    def get_available_searches(self):
        available_searches = ""
        for key, val in self.search_urls.items():
            available_searches = f"""{available_searches}{key}: {val["name"]}\n"""
        available_searches = available_searches.strip()
        available_searches = f"""echo "{available_searches}" """
        return available_searches

    def get_rofi_input(self):
        available_searches = self.get_available_searches()
        print(f"""{available_searches} | rofi -dmenu normal""")
        rofi_search_input = sp.run(
            f"""{available_searches} | rofi -dmenu normal""", shell=True, capture_output=True, text=True, check=False
        )
        return rofi_search_input.stdout

    def open_search_url(self, search_input):
        search_url_key = search_input[:2]
        search_query = search_input[2:].strip().replace(" ", "+")
        if search_url_key in self.search_urls:
            sp.run(f"""xdg-open {self.search_urls[search_url_key]["url"]}{search_query}""", shell=True, check=False)
        else:
            sys.exit()

    def run(self):
        rofi_search = self.get_rofi_input()
        self.open_search_url(rofi_search)


if __name__ == "__main__":
    launcher = SearchEngineLauncher()
    launcher.run()
