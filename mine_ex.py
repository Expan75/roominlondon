# Script for prototyping data flow
from bs4 import BeautifulSoup
import requests

# Set up base info
BASE_URL_PREFIX = "https://www.spareroom.co.uk/flatshare/?offset="
BASE_URL_SUFFIX = "&search_id=962193229&sort_by=age&mode=list"

# Utility function for formatting url
def getFormedURL(prefix, suffix, page_index):
    return prefix + str(page_index) + suffix


# Set up request and BS object
url = getFormedURL(BASE_URL_PREFIX, BASE_URL_SUFFIX, 0)
res = requests.get(url).text
soup = BeautifulSoup(res, "html.parser")


# Get articles for page
def getPageListings(soup):
    return soup.find_all("li", class_="listing-result")


listings = getPageListings(soup)

# THINGS WE WANT TO PARSE PER LISTING
parseKeys = [
    "data-listing-id",
    "data-listing-title",
    "data-listing-available",
    "data-listing-status",
    "data-listing-days-old",
    "data-listing-neighbourhood",
    "data-listing-property-type",
    "data-listing-rooms-in-property",
    "data-listing-advertiser-role",
    "data-default-payment",
    "data-price-per-month",
    "data-price-per-week",
]

from functools import reduce


def parseListing(listing, keys):
    res = {}
    for key in keys:
        try:
            res[key] = listing[key]
        except:
            continue
    print(res)
    return res


def parseListings(listings, keys):
    return list(map(lambda listing: parseListing(listing, keys)))


data = parseListing(listings, parseKeys)


print(data)
