import whois

def whois_query(domain):
    w_creation_date_list = []

    w = whois.whois(domain)
    w_dict = dict(w)

    try:

        for i in w_dict["creation_date"]:
            w_creation_date_list.append(str(i))

    except TypeError:

        w_creation_date_list.append(str(w_dict["creation_date"]))

    try:
        whois_email = w_dict["emails"]
    except KeyError:
        whois_email = ""

    try:
        whois_name = w_dict["name"]
    except KeyError:
        whois_name = ""

    try:
        whois_name_servers = w_dict["name_servers"]
    except KeyError:
        whois_name_servers = ""

    try:
        whois_org = w_dict["org"]
    except KeyError:
        whois_org = ""

    try:
        whois_address = w_dict["address"]
    except KeyError:
        whois_address = ""

    try:
        whois_city = w_dict["city"]
    except KeyError:
        whois_city = ""

    try:
        whois_country = w_dict["country"]
    except KeyError:
        whois_country = ""

    try:
        whois_creation_date = w_creation_date_list
    except KeyError:
        whois_creation_date = ""

    try:
        whois_dnssec = w_dict["dnssec"]
    except KeyError:
        whois_dnssec = ""


    return whois_email, whois_name, whois_name_servers, whois_org,\
            whois_address, whois_city, whois_country, whois_creation_date, whois_dnssec