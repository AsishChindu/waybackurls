import argparse
import requests
 
 
# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-u", "--url", help = "Domain to scan")
parser.add_argument("-k", "--keywords", help = "Keywords to search in wayurls list")
 
# Read arguments from command line
args = parser.parse_args()

if args.keywords:
    keywords = args.keywords.split(',')

page = requests.get("https://web.archive.org/cdx/search/cdx?url="+args.url+"/*&output=text&fl=original&collapse=urlkey")

content = page.content.decode('utf-8')

waybackurls = content.splitlines()

for url in waybackurls:
    for keyword in keywords:
        if keyword in url:
            print(url)
