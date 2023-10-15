# Parser logic

import requests
import fake_useragent
from colorama import init, Fore
from bs4 import BeautifulSoup

import config
from config import convert

init(autoreset=True, convert=convert)


class Parse:
    def __init__(self):
        self.proxy_urls = config.urls
        self.agent = fake_useragent.UserAgent().random

    @staticmethod
    def formatting(value: str):
        """
        This function "washing" proxies, because there are often strings like:
        "\n                 xxx.xxx.xxx.xxx             \n"
        So it need to be clear

        :return: str
        """
        string = value.replace("\n", "")
        string = string.replace(" ", "")
        return string

    def parse(self):
        print(Fore.BLUE + "User-Agent: ", self.agent)
        headers = {"User-Agent": self.agent}
        proxy_list = []

        for proxy_url in self.proxy_urls:
            proxy_list.append({'proxy': proxy_url, 'port': ''})
            r = requests.get(proxy_url, headers=headers)  # Sending request to get content of website
            content = r.content

            soup = BeautifulSoup(content, 'html.parser')
            tbody = soup.find_all('tbody')
            if tbody:
                elements = tbody[0].find_all('tr')
                for tr in elements:
                    # Getting first elements in tr
                    td_elements = tr.find_all('td')[:2]
                    if len(td_elements) >= 2:
                        # Taking out values
                        value1 = str(td_elements[0].get_text())
                        # print(value1)  # This is for Debug!
                        proxy_ip = __class__.formatting(value1)

                        value2 = td_elements[1].get_text()
                        port = __class__.formatting(value2)
                        proxy = {
                            "proxy": proxy_ip,
                            "port": port
                        }
                        # print(proxy)
                        proxy_list.append(proxy)
                proxy_list.append({'proxy': ":"+"-" * 25, 'port': '\n'})

            else:
                try:
                    next_url = self.proxy_urls[self.proxy_urls.index(proxy_url) + 1]
                except Exception as e:
                    next_url = "none"


                print(Fore.RED + "Url", proxy_url, "returned empty urls, going to next url ({})...".format(next_url))
        # print(proxy_list)  # This is for Debug!
        return proxy_list
