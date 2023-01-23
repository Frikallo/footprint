import dns.resolver
from footprint.utils.table import buildTable as table

def Lookup(email):
    lookup_temp_result = []
    splt = email.split('@')
    records = ["A", "AAAA", "NS", "MX", "TXT", "SOA"]
    for record in records:
        try:
            if record == "A":
                ipv4records = dns.resolver.resolve(splt[1], 'A')
                for rdata in ipv4records:
                    row = ["IPV4", str(rdata.address).strip()]
                    lookup_temp_result.append(row)
            elif record == "AAAA":
                ipv6records = dns.resolver.resolve(splt[1], 'AAAA')
                for rdata in ipv6records:
                    row = ["IPV6", str(rdata.address).strip()]
                    lookup_temp_result.append(row)
            elif record == "NS":
                nameserver = dns.resolver.resolve(splt[1], 'NS')
                for rdata in nameserver:
                    row = ["NS", str(rdata.target).strip()]
                    lookup_temp_result.append(row)
            elif record == "MX":
                mxrecords = dns.resolver.resolve(splt[1], 'MX')
                for rdata in mxrecords:
                    row = ["MX", str(rdata.exchange).strip()]
                    lookup_temp_result.append(row)
            elif record == "TXT":
                txtrecords = dns.resolver.resolve(splt[1], 'TXT')
                for rdata in txtrecords:
                    for TXT in rdata.strings:
                        text = TXT.decode('utf-8').strip()
                        row = ["TXT",text.split(' ')[0]]
                        lookup_temp_result.append(row)
                        for _ in text.split(' ')[1:]:
                            row = ["", _]
                            lookup_temp_result.append(row)
            elif record == "SOA":
                soarecords = dns.resolver.resolve(splt[1], 'SOA')
                for rdata in soarecords:
                    row = ["SOA", str(rdata.mname).strip()]
                    lookup_temp_result.append(row)
        except Exception:
            pass
    return lookup_temp_result

if __name__ == "__main__":
    email = "example@example.com"
    table(Lookup(email))