import os

urls = [
    "https://free-proxy-list.net/",
    "https://www.proxyscrape.com/free-proxy-list",
    "https://www.proxy-list.download/HTTP"
]

convert = None
if os.name != 'nt': convert = False
else: convert = True

figlet_font = 'big'
