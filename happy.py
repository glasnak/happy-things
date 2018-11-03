#!/usr/bin/env python

from lxml import html, etree
import requests

WEBPAGE = 'https://www.thingstobehappyabout.com/neighborhood/calendar.php'
# FIXME: this is ambiguous at best:
XPATH='//li/parent::ul/li/text()'

def main():
    page = requests.get(WEBPAGE)
    tree = html.fromstring(page.content)
    items = tree.xpath(XPATH, pretty_print=True, encoding="unicode")
    for item in items:
        print(item)

if __name__ == "__main__":
    main()
