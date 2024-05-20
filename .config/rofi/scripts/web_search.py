import subprocess as sp
import sys

search_urls = {
    "dd": "https://duckduckgo.com/?q=",
    "bb": "https://search.brave.com/search?q=",
    "rr": "https://www.reddit.com/search/?q=",
    "ww": "https://en.wikipedia.org/w/index.php?search=",
    "pp": "https://docs.python.org/3/search.html?q=",
    "gg": "https://www.google.com/search?q=",
}

# Send created string to rof and get selected rofi output
rofi_search_input = sp.run(
    """rofi -dmenu""", shell=True, capture_output=True, text=True, check=False
)
rofi_search = rofi_search_input.stdout

search_url = rofi_search[:2]
search = rofi_search[1:].strip().replace(" ", "+")
if search_url in search_urls.keys():
    sp.run(f"""xdg-open {search_urls[search_url]}{search}""", shell=True, check=False)
else:
    sys.exit()
