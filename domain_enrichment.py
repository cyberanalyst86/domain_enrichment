import pandas as pd
import re
import datetime
from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
from whois_module import *
from wappalzer_module import *
from urlscan_module import *

def get_api_key():

    with open(
            "otx_api.yaml") as f:
        conf = yaml.load(f, Loader=SafeLoader)

    apikey = conf['otx_api']['api_key']
    return apikey

def is_valid_domain(domain):
    # Regular expression pattern for a simple domain format
    pattern = re.compile(r'^([a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$')

    return bool(pattern.match(domain))

def otx_query(domain):
    otx = OTXv2(get_api_key())
    otx_get = otx.get_indicator_details_full(IndicatorTypes.URL, domain)

    return otx_get["general"]["whois"]

def main():

    # -------------------------Declaration-------------------------------#

    otx_whoislink_list = []

    whois_email_list = []
    whois_name_list = []
    whois_name_servers_list = []
    whois_org_list = []
    whois_address_list = []
    whois_city_list = []
    whois_country_list = []
    whois_creation_date_list = []
    whois_dnssec_list = []

    wap_tech_list = []
    wap_tech_cat_list = []
    wap_tech_cat_ver_list = []

    urlscan_uuid_list = []
    urlscan_url_list = []
    urlscan_domain_list = []
    urlscan_country_list = []
    urlscan_city_list = []
    urlscan_server_list = []
    urlscan_ip_list = []
    urlscan_asn_list = []
    urlscan_asnname_list = []
    urlscan_app_list = []
    urlscan_reporturl_list = []
    urlscan_screenshoturl_list = []
    urlscan_domurl_list = []

    domain_input = input("Enter excel file path: ")

    df = pd.read_csv(domain_input)

    domain_list = df["domain"].tolist()

    for domain in domain_list:

        if is_valid_domain(domain):

            print(domain)

            otx_whoislink = otx_query(domain)

            print(otx_whoislink)

            print("-------------------whois------------------")

            whois_email, whois_name, whois_name_servers, whois_org, \
                whois_address, whois_city, whois_country, whois_creation_date, whois_dnssec = whois_query(domain)

            print(whois_email)
            print(whois_name)
            print(whois_name_servers)
            print(whois_org)
            print(whois_address)
            print(whois_city)
            print(whois_country)
            print(whois_creation_date)
            print(whois_dnssec)

            print("-------------------wappalyzer------------------")

            wap_tech, wap_tech_cat, wap_tech_cat_ver = wappalzer_query(domain)

            print(wap_tech)
            print(wap_tech_cat)
            print(wap_tech_cat_ver)

            print("-------------------urlscan------------------")

            urlscan_uuid, urlscan_url, urlscan_domain, urlscan_country, urlscan_city \
                , urlscan_server, urlscan_ip, urlscan_asn, urlscan_asnname \
                , urlscan_app, urlscan_reporturl, urlscan_screenshoturl \
                , urlscan_domurl = get_urlscan_result(domain)

            print(urlscan_uuid)
            print(urlscan_url)
            print(urlscan_domain)
            print(urlscan_country)
            print(urlscan_city)
            print(urlscan_server)
            print(urlscan_ip)
            print(urlscan_asn)
            print(urlscan_asnname)
            print(urlscan_app)
            print(urlscan_reporturl)
            print(urlscan_screenshoturl)
            print(urlscan_domurl)


            otx_whoislink_list.append(otx_whoislink)

            whois_email_list.append(whois_email)
            whois_name_list.append(whois_name)
            whois_name_servers_list.append(whois_name_servers)
            whois_org_list.append(whois_org)
            whois_address_list.append(whois_address)
            whois_city_list.append(whois_city)
            whois_country_list.append(whois_country)
            whois_creation_date_list.append(whois_creation_date)
            whois_dnssec_list.append(whois_dnssec)

            wap_tech_list.append(wap_tech)
            wap_tech_cat_list.append(wap_tech_cat)
            wap_tech_cat_ver_list.append(wap_tech_cat_ver)

            urlscan_uuid_list.append(urlscan_uuid)
            urlscan_url_list.append(urlscan_url)
            urlscan_domain_list.append(urlscan_domain)
            urlscan_country_list.append(urlscan_country)
            urlscan_city_list.append(urlscan_city)
            urlscan_server_list.append(urlscan_server)
            urlscan_ip_list.append(urlscan_ip)
            urlscan_asn_list.append(urlscan_asn)
            urlscan_asnname_list.append(urlscan_asnname)
            urlscan_app_list.append(urlscan_app)
            urlscan_reporturl_list.append(urlscan_reporturl)
            urlscan_screenshoturl_list.append(urlscan_screenshoturl)
            urlscan_domurl_list.append(urlscan_domurl)


        else:

            whois_email_list.append("invalid domain")
            whois_name_list.append("invalid domain")
            whois_name_servers_list.append("invalid domain")
            whois_org_list.append("invalid domain")
            whois_address_list.append("invalid domain")
            whois_city_list.append("invalid domain")
            whois_country_list.append("invalid domain")
            whois_creation_date_list.append("invalid domain")
            whois_dnssec_list.append("invalid domain")

            wap_tech_list.append("invalid domain")
            wap_tech_cat_list.append("invalid domain")
            wap_tech_cat_ver_list.append("invalid domain")

            urlscan_uuid_list.append("invalid domain")
            urlscan_url_list.append("invalid domain")
            urlscan_domain_list.append("invalid domain")
            urlscan_country_list.append("invalid domain")
            urlscan_city_list.append("invalid domain")
            urlscan_server_list.append("invalid domain")
            urlscan_ip_list.append("invalid domain")
            urlscan_asn_list.append("invalid domain")
            urlscan_asnname_list.append("invalid domain")
            urlscan_app_list.append("invalid domain")
            urlscan_reporturl_list.append("invalid domain")
            urlscan_screenshoturl_list.append("invalid domain")
            urlscan_domurl_list.append("invalid domain")

            print(domain)
            print("invalid domain")


    df["domain"] = domain_list
    df["otx whoislink"] = otx_whoislink_list
    df["w_emails"] = whois_email_list
    df["w_name"] = whois_name_list
    df["w_name_servers"] = whois_name_servers_list
    df["w_org"] = whois_org_list
    df["w_address"] = whois_city_list
    df["w_city"] = whois_city_list
    df["w_country"] = whois_country_list
    df["w_creation_date"] = whois_creation_date_list
    df["w_dnssec"] = whois_dnssec_list
    df["wap tech"] = wap_tech_list
    df["wap tech category"] = wap_tech_cat_list
    df["wap tech category version"] = wap_tech_cat_ver_list
    df["urlscan_uuid"] = urlscan_uuid_list
    df["urlscan_url"] = urlscan_url_list
    df["urlscan_domain"] = urlscan_domain_list
    df["urlscan_country"] = urlscan_country_list
    df["urlscan_city"] = urlscan_city_list
    df["urlscan_server"] = urlscan_server_list
    df["urlscan_ip"] = urlscan_ip_list
    df["urlscan_asn"] = urlscan_asn_list
    df["urlscan_asnname"] = urlscan_asnname_list
    df["urlscan_app"] = urlscan_app_list
    df["urlscan_reporturl"] = urlscan_reporturl_list
    df["urlscan_screenshoturl"] = urlscan_screenshoturl_list
    df["urlscan_domurl"] = urlscan_domurl_list

    df.to_csv("sample_enrichment.csv", index=False)

    print("Domain enrichment completed...")

if __name__ == "__main__":
    main()