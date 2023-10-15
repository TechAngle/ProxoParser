from colorama import init, Fore
import pyfiglet
import datetime
from parse import Parse
import os
import config

init(convert=config.convert, autoreset=True)

"""
ProxoParser by TechAngle
Author Github: github.com/TechAngle
Contact: rect4ngle@programmer.net

I hope this will help you to find proxies for personal use
"""


class ProxoParser:
    """
    Main class of all script

    There are all "magic" of parser
    """
    def __init__(self):
        self.app_name = "ProxoParser"
        self.output_file = f"proxies{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        self.dir = "parsed"

    def banner(self):
        _ = pyfiglet.Figlet(config.figlet_font).renderText(self.app_name)

        return _

    def create_proxy_dir(self):
        """
        Creates directory "parsed" if it not exists

        :return: bool
        """
        if not os.path.exists(self.dir):
            try:
                os.mkdir(self.dir)
                return False

            except Exception as e:
                print(Fore.RED + "An error occurred while creating directory for parsed proxies:", e)
        else:
            return True

    def parsing(self):
        print(Fore.LIGHTYELLOW_EX + "Parsing proxies...")
        try:
            proxies = Parse().parse()

            if proxies == 0:
                return False

            with open(self.dir+"/"+self.output_file, 'a') as f:
                f.write(__class__.banner(self))
                f.close()
            for proxy in proxies:
                try:
                    file = open(self.dir+r"/"+self.output_file, 'a')
                    write_string = f"{proxy['proxy']}:{proxy['port']}\n"
                    file.write(write_string)

                except Exception as e:
                    print(Fore.RED + "An error occurred while opening file: " + str(e))

            return True
        except Exception as e:
            print(e.__annotations__)
            print(Fore.RED + "An error occurred while parsing proxies!", e)
            return False


if __name__ == "__main__":
    parser = ProxoParser()
    print(Fore.LIGHTYELLOW_EX + "Starting script...")

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print(ProxoParser().banner())

    # Creating directory(or its unnecessary)
    parser.create_proxy_dir()

    # Getting result about parsing
    result = parser.parsing()
    if result:
        print(Fore.LIGHTGREEN_EX + "Proxies was successfully saved to", parser.dir)

    else:
        print(Fore.RED + "Something gone wrong")
