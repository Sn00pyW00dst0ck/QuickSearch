import sys
import webbrowser

# Some constant values
CHROME_PATH='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
BASE_URL="https://www.google.com/search?q="
VALID_WEBSITES = [
    'reddit.com',
    'medium.com',
    'w3schools.com',
    'stackoverflow.com',
    'stackexchange.com',
    'docs.unity3d.com',
    'cppreference.com',
    'youtube.com'
]

def create_search_filter():
    filter = '('
    for index, website in enumerate(VALID_WEBSITES):
        filter += 'site:' + website
        if index == len(VALID_WEBSITES) - 1:
            filter += ')'
        else:
            filter += ' OR '
    return filter

def main():
    # Validate Command Line Args
    if len(sys.argv[1:]) == 0:
        print('Error: enter a valid search query')
        return -1

    # Generate Search URL
    query = ''.join(sys.argv[1:])
    final_search_url = BASE_URL + query + create_search_filter()

    # Open the Chrome Tab
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(CHROME_PATH))
    webbrowser.get('chrome').open_new_tab(final_search_url)

# Run main if not used as import
if __name__ == "__main__":
    main()