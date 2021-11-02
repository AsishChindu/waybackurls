import argparse
import requests
 
 
# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-u", "--url", help = "Domain to scan")
parser.add_argument("-k", "--keywords", help = "Keywords to search in wayurls list")
 
# Read arguments from command line
args = parser.parse_args()

page = requests.get("https://web.archive.org/cdx/search/cdx?url="+args.url+"/*&output=text&fl=original&collapse=urlkey")

content = page.content.decode('utf-8')

waybackurls = content.splitlines()

prev_url = ""

for url in waybackurls:
    if url != prev_url:
        current_page = requests.get(url)
        if current_page.status_code == 200:
            if args.keywords:
                keywords = args.keywords.split(',')
                for keyword in keywords:
                    if keyword in url:
                            print(url)
                            break
            else:
                print(url)
    
    prev_url = url