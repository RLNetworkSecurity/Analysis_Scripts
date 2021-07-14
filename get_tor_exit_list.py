#! /usr/bin/env python
"""
Simple python script to get TOR exit list
IP addresses and output as a list file type.
Author: RLNetworkSecurity - RLNetworkSecurity.co.uk
"""

import os
from urllib.request import urlopen
import re

TOR_URL = "https://check.torproject.org/torbulkexitlist"

def main():

    page = urlopen(TOR_URL)
    data = page.read().decode("utf-8")
    tor_ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', data)
    print(tor_ip)

if __name__ == "__main__":
    main()
