import requests
import json
import time
import yaml
from yaml.loader import SafeLoader
import pandas as pd

def get_api_key():

    with open("urlscan_api.yaml") as f:
        conf = yaml.load(f, Loader=SafeLoader)

    apikey = conf['urlscan_api']['api_key']
    return apikey

def get_urlscan_uuid(domain):

    # Define the API endpoint and your API key
    api_endpoint = "https://urlscan.io/api/v1/scan/"
    api_key = get_api_key()  # Replace with your actual API key

    # Prepare the headers with the API key
    headers = {
        "API-Key": api_key,
        "Content-Type": "application/json",
    }

    #print("domain" + "\t" + "uuid")

    # Prepare the payload (URL to scan)
    data = {
        "url": domain, "visibility": "public"
    }

    # Send a POST request to submit the URL for scanning
    response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
        #print(str(domain) + "\t" + str(result['uuid']))
        uuid = result['uuid']

    else:
        #print(str(domain) + "\t" + str(response.status_code))
        uuid = "error"

    return uuid

def get_urlscan_result(domain):

    urlscan_uuid = get_urlscan_uuid(domain)

    time.sleep(20) #adjust if urlscan produces error

    # Define the API endpoint and your API key
    api_endpoint = "https://urlscan.io/api/v1/scan/"
    api_key = get_api_key()   # Replace with your actual API key

    # Prepare the headers with the API key
    headers = {
        "API-Key": api_key,
        "Content-Type": "application/json",
    }

    #print("domain" + "\t" + "uuid" + "\t"+ "url" + "\t" + "urlscan_domain" + "\t" + "country" + "\t" + "city" + "\t" + "server" + "\t" + "ip" + "\t" + "asn"
    #      + "\t" + "asnname" + "\t" + "app" + "\t" + "reporturl" + "\t" + "screenshoturl" + "\t" + "domurl")


    if urlscan_uuid != "error":

        url = "https://urlscan.io/api/v1/result/" + str(urlscan_uuid) + "/"

        response = requests.get(url, headers=headers)

        if response.status_code == 200:

            urlscan = response.json()

            try:
                df = pd.DataFrame.from_dict(urlscan["meta"]["processors"]["wappa"])

                urlscan_app_list = []

                for index, row in df.iterrows():
                    urlscan_app_list.append(row["data"]["app"])

            except KeyError:
                urlscan_app_list = []

            try:
                urlscan_url = urlscan["page"]["url"]

            except KeyError:
                urlscan_url = ""

            try:
                urlscan_domain = urlscan["page"]["domain"]

            except KeyError:
                urlscan_domain = ""

            try:
                urlscan_country = urlscan["page"]["country"]

            except KeyError:
                urlscan_country = ""

            try:
                urlscan_city = urlscan["city"]
            except KeyError:
                urlscan_city = ""

            try:
                urlscan_server = urlscan["page"]["server"]
            except KeyError:
                urlscan_server = ""

            try:
                urlscan_ip = urlscan["page"]["ip"]
            except KeyError:
                urlscan_ip = ""

            try:
                urlscan_asn = urlscan["page"]["asn"]
            except KeyError:
                urlscan_asn = ""

            try:
                urlscan_asnname = urlscan["page"]["asnname"]
            except KeyError:
                urlscan_asnname = ""

            try:
                urlscan_app = urlscan_app_list
            except KeyError:
                urlscan_app = ""

            try:
                urlscan_reporturl = urlscan["task"]["reportURL"]
            except KeyError:
                urlscan_reporturl = ""

            try:
                urlscan_screenshoturl = urlscan["task"]["screenshotURL"]
            except KeyError:
                urlscan_screenshoturl = ""

            try:
                urlscan_domurl = urlscan["task"]["domURL"]
            except KeyError:
                urlscan_domurl = ""


        #    print(str(domain) + "\t" + str(uuid) + "\t" +
        #              str(urlscan_url) + "\t" + str(urlscan_domain) + "\t" +
        #              str(urlscan_country) + "\t" + str(urlscan_city) + "\t" +
        #              str(urlscan_server) + "\t" +
        #              str(urlscan_ip) + "\t" +
        #              str(urlscan_asn) + "\t" +
        #              str(urlscan_asnname) + "\t" +
        #              str(urlscan_app) + "\t" +
        #              str(urlscan_reporturl) + "\t" +
        #              str(urlscan_screenshoturl) + "\t" +
        #              str(urlscan_domurl))

    else:
        urlscan_url = ""
        urlscan_domain = ""
        urlscan_country = ""
        urlscan_city = ""
        urlscan_server = ""
        urlscan_ip = ""
        urlscan_asn = ""
        urlscan_asnname = ""
        urlscan_app = ""
        urlscan_reporturl = ""
        urlscan_screenshoturl = ""
        urlscan_domurl = ""

        #print(str(domain) + "\t" + str(uuid) + "\t" +
        #      str(urlscan_url) + "\t" + str(urlscan_domain) + "\t" +
        #      str(urlscan_country) + "\t" + str(urlscan_city) + "\t" +
        #      str(urlscan_server) + "\t" +
        #      str(urlscan_ip) + "\t" +
        #      str(urlscan_asn) + "\t" +
        #      str(urlscan_asnname) + "\t" +
        #      str(urlscan_app) + "\t" +
        #      str(urlscan_reporturl) + "\t" +
        #      str(urlscan_screenshoturl) + "\t" +
        #      str(urlscan_domurl))


    return urlscan_uuid, urlscan_url, urlscan_domain, urlscan_country,urlscan_city\
        ,urlscan_server, urlscan_ip, urlscan_asn, urlscan_asnname\
        , urlscan_app, urlscan_reporturl, urlscan_screenshoturl\
        , urlscan_domurl
