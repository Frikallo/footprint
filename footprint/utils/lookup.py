import socket
import dns.resolver
from footprint.utils.table import buildTable as table

def Lookup(email):
    lookup_temp_result = []
    splt = email.split('@')
    try:
        ipv4records = ["IP", socket.gethostbyname(splt[1])]
        ipv6records = ["IP", list(socket.getaddrinfo(splt[1], 0, socket.AF_INET6))[0][4][0]]
        lookup_temp_result.append(ipv4records)
        lookup_temp_result.append(ipv6records)
        nameserver = dns.resolver.resolve(splt[1], 'NS')
        for rdata in nameserver:
            row = ["NS", str(rdata.target).strip()]
            lookup_temp_result.append(row)
        mxrecords = dns.resolver.resolve(splt[1], 'MX')
        for rdata in mxrecords:
            row = ["MX", str(rdata.exchange).strip()]
            lookup_temp_result.append(row)
        txtrecords = dns.resolver.resolve(splt[1], 'TXT')
        for rdata in txtrecords:
            for TXT in rdata.strings:
                text = TXT.decode('utf-8').strip()
                row = ["TXT",text.split(' ')[0]]
                lookup_temp_result.append(row)
                for _ in text.split(' ')[1:]:
                    row = ["", _]
                    lookup_temp_result.append(row)
    except Exception as e:
        print("Error: Unable to resolve domain records. Please check your internet connection and try again.")
        print(e)
        exit(0)
    return lookup_temp_result

if __name__ == "__main__":
    email = "noahskay@icloud.com"
    table(Lookup(email))