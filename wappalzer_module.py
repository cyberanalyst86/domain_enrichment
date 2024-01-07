from Wappalyzer import Wappalyzer, WebPage
from requests.exceptions import RequestException
import requests

def wappalzer_query(domain):
    try:
        url = "https" + "://" + str(domain)

        response = requests.get(url, timeout=3)

        if response.status_code == 200:

            wappalyzer = Wappalyzer.latest()
            webpage = WebPage.new_from_url(url)
            wap_tech = wappalyzer.analyze(webpage)
            wap_tech_cat = wappalyzer.analyze_with_categories(webpage)
            wap_tech_cat_ver = wappalyzer.analyze_with_versions_and_categories(webpage)

        else:

            wap_tech = "ConnectError"
            wap_tech_cat = "ConnectError"
            wap_tech_cat_ver = "ConnectError"

    except RequestException:

        try:

            url = "http" + "://" + str(domain)

            response = requests.get(url, timeout=3)

            if response.status_code == 200:

                wappalyzer = Wappalyzer.latest()
                webpage = WebPage.new_from_url(url)
                wap_tech = wappalyzer.analyze(webpage)
                wap_tech_cat = wappalyzer.analyze_with_categories(webpage)
                wap_tech_cat_ver = wappalyzer.analyze_with_versions_and_categories(webpage)

            else:

                wap_tech = "ConnectError"
                wap_tech_cat = "ConnectError"
                wap_tech_cat_ver = "ConnectError"

        except RequestException:

            wap_tech = "ConnectError"
            wap_tech_cat = "ConnectError"
            wap_tech_cat_ver = "ConnectError"


    return wap_tech, wap_tech_cat, wap_tech_cat_ver