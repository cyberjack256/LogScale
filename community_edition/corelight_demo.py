from faker import Faker
import random
import time

fake = Faker()

# List of fake IPs
ips = ["192.168.1.{}".format(i) for i in range(1, 256)]

# List of user agents
user_agents = ["Mozilla/5.0", "Chrome/73.0", "Safari/537.36"]

# List of HTTP methods
methods = ["GET", "POST", "PUT", "DELETE"]

# List of URLs
urls = ["/index.html", "/about.html", "/contact.html", "/profile.html", "/settings.html", "/login.html", "/signup.html"]

# List of protocols and their common ports
protocols_ports = {
    "tcp": list(range(1, 1024)),
    "udp": list(range(1, 1024)),
    "icmp": [0],
}

# Service-port mapping
services_ports = {
    "http": [80, 8080, 8000],
    "https": [443],
    "ssh": [22],
    "ftp": [20, 21],
    "dns": [53],
    "dhcp": [67, 68],
    "smtp": [25, 465, 587],
    "pop3": [110, 995],
    "imap": [143, 993],
    "telnet": [23],
    "rdp": [3389],
    # Add more mappings as needed
}

# Service-protocol mapping
service_protocol_mapping = {
    "http": "tcp",
    "https": "tcp",
    "ssh": "tcp",
    "ftp": "tcp",
    "dns": "udp",
    "dhcp": "udp",
    "smtp": "tcp",
    "pop3": "tcp",
    "imap": "tcp",
    "telnet": "tcp",
    "rdp": "tcp",
    # Add more mappings as needed
}

# List of connection states
conn_states = ["S0", "S1", "SF", "REJ", "S2", "S3", "RSTO", "RSTR", "RSTOS0", "RSTRH", "SH", "SHR", "OTH"]

# List of DNS queries
dns_queries = ["google.com", "facebook.com", "twitter.com", "faceclone.com"]

# List of DNS QCLASS names
dns_qclass_names = ["IN", "CH", "HS", "NONE", "ANY"]

# List of DNS QTYPE names
dns_qtype_names = ["A", "NS", "MD", "MF", "CNAME", "SOA", "MB", "MG", "MR", "NULL", "WKS", "PTR", "HINFO", "MINFO", "MX", "TXT", "RP", "AFSDB", "X25", "ISDN", "RT", "NSAP", "NSAP_PTR", "SIG", "KEY", "PX", "GPOS", "AAAA", "LOC", "NXT", "EID", "NIMLOC", "SRV", "ATMA", "NAPTR", "KX", "CERT", "A6", "DNAME", "SINK", "OPT", "APL", "DS", "SSHFP", "IPSECKEY", "RRSIG", "NSEC", "DNSKEY", "DHCID", "NSEC3", "NSEC3PARAM", "TLSA", "SMIMEA", "HIP", "NINFO", "RKEY", "TALINK", "CDS", "CDNSKEY", "OPENPGPKEY", "CSYNC", "ZONEMD", "SVCB", "HTTPS", "SPF", "UINFO", "UID", "GID", "UNSPEC", "NID", "L32", "L64", "LP", "EUI48", "EUI64", "TKEY", "TSIG", "IXFR", "AXFR", "MAILB", "MAILA", "ANY", "URI", "CAA", "AVC", "DOA", "AMTRELAY", "TA", "DLV"]

# List of DNS RCODE names
dns_rcode_names = ["NOERROR", "FORMERR", "SERVFAIL", "NXDOMAIN", "NOTIMP", "REFUSED", "YXDOMAIN", "YXRRSET", "NXRRSET", "NOTAUTH", "NOTZONE", "DSOTYPENI", "BADVERS", "BADKEY", "BADTIME", "BADMODE", "BADNAME", "BADALG", "BADTRUNC", "BADCOOKIE"]

# List of SSL versions
ssl_versions = ["SSLv2", "SSLv3", "TLSv1", "TLSv1.1", "TLSv1.2", "TLSv1.3"]

# List of SSL cipher suites
ssl_cipher_suites = ["TLS_AES_128_GCM_SHA256", "TLS_AES_256_GCM_SHA384", "TLS_CHACHA20_POLY1305_SHA256", "TLS_AES_128_CCM_SHA256", "TLS_AES_128_CCM_8_SHA256"]

# Malicious IP
malicious_ip = "192.168.1.100"

# Ongoing DNS queries
ongoing_dns_queries = {}

# Open the log files in write mode
with open("fake_conn.log", "w") as conn_f, open("fake_dns.log", "w") as dns_f, open("fake_http.log", "w") as http_f, open("fake_ssl.log", "w") as ssl_f:
    # Write the headers
    conn_f.write("#fields\tts\tuid\tid.orig_h\tid.orig_p\tid.resp_h\tid.resp_p\tproto\tservice\tduration\torig_bytes\tresp_bytes\tconn_state\tlocal_orig\tlocal_resp\tmissed_bytes\thistory\torig_pkts\torig_ip_bytes\tresp_pkts\tresp_ip_bytes\ttunnel_parents\n")
    dns_f.write("#fields\tts\tuid\tid.orig_h\tid.orig_p\tid.resp_h\tid.resp_p\tproto\ttrans_id\trtt\tquery\tqclass\tqclass_name\tqtype\tqtype_name\trcode\trcode_name\tAA\tTC\tRD\tRA\tZ\tanswers\tTTLs\trejected\n")
    http_f.write("#fields\tts\tuid\tid.orig_h\tid.orig_p\tid.resp_h\tid.resp_p\ttrans_depth\tmethod\thost\turi\treferrer\tversion\tuser_agent\trequest_body_len\tresponse_body_len\tstatus_code\tstatus_msg\tinfo_code\tinfo_msg\ttags\tusername\tpassword\tproxied\torig_fuids\torig_mime_types\tresp_fuids\tresp_mime_types\n")
    ssl_f.write("#fields\tts\tuid\tid.orig_h\tid.orig_p\tid.resp_h\tid.resp_p\tversion\tcipher\tserver_name\tresumed\testablished\tcert_chain_fuids\tclient_cert_chain_fuids\tsubject\tissuer\tclient_subject\tclient_issuer\tvalidation_status\tja3\tja3s\n")

    # Generate and write the fake logs
    for _ in range(1000):  # Generate 1000 logs for each type
        ts = time.time()
        uid = fake.uuid4()
        id_orig_h = random.choice(ips)
        id_resp_h = random.choice(ips)
        proto = random.choice(list(protocols_ports.keys()))
        id_orig_p = random.choice(protocols_ports[proto])
        service = random.choice(list(services_ports.keys()))
        id_resp_p = random.choice(services_ports[service])

        # Choose service and corresponding protocol
        service = random.choice(list(service_protocol_mapping.keys()))
        proto = service_protocol_mapping[service]

        # Insert malicious scenario randomly
        if random.random() < 0.01:  # 1% chance of malicious scenario
            id_orig_h = malicious_ip
            orig_bytes = random.randint(2000, 5000)  # Increase data transfer

        # Conn logs
        duration = random.uniform(0, 60)
        orig_bytes = random.randint(0, 2000)
        resp_bytes = random.randint(0, 2000)
        conn_state = random.choice(conn_states)
        local_orig = random.choice([True, False])
        local_resp = random.choice([True, False])
        missed_bytes = random.randint(0, 100)
        history = fake.bothify(text="????", letters="ASDF")
        orig_pkts = random.randint(0, 100)
        orig_ip_bytes = random.randint(0, 5000)
        resp_pkts = random.randint(0, 100)
        resp_ip_bytes = random.randint(0, 5000)
        tunnel_parents = "(empty)"

        conn_f.write(f"{ts}\t{uid}\t{id_orig_h}\t{id_orig_p}\t{id_resp_h}\t{id_resp_p}\t{proto}\t{service}\t{duration}\t{orig_bytes}\t{resp_bytes}\t{conn_state}\t{local_orig}\t{local_resp}\t{missed_bytes}\t{history}\t{orig_pkts}\t{orig_ip_bytes}\t{resp_pkts}\t{resp_ip_bytes}\t{tunnel_parents}\n")

        # If the service is DNS, generate DNS logs
        if service == "dns":
            # DNS query
            trans_id = random.randint(0, 65535)
            rtt = random.uniform(0, 1)
            query = random.choice(dns_queries)
            qclass = 1  # IN
            qclass_name = "IN"
            qtype = random.randint(1, 255)
            qtype_name = random.choice(dns_qtype_names)
            AA = random.choice([True, False])
            TC = random.choice([True, False])
            RD = random.choice([True, False])
            RA = random.choice([True, False])
            Z = 0
            answers = "(empty)"
            TTLs = "(empty)"
            rejected = random.choice([True, False])

            dns_f.write(f"{ts}\t{uid}\t{id_orig_h}\t{id_orig_p}\t{id_resp_h}\t{id_resp_p}\t{proto}\t{trans_id}\t{rtt}\t{query}\t{qclass}\t{qclass_name}\t{qtype}\t{qtype_name}\t{-1}\t-\t{AA}\t{TC}\t{RD}\t{RA}\t{Z}\t{answers}\t{TTLs}\t{rejected}\n")

            # Add the query to the ongoing DNS queries
            ongoing_dns_queries[uid] = {"ts": ts, "id_orig_h": id_orig_h, "id_orig_p": id_orig_p, "id_resp_h": id_resp_h, "id_resp_p": id_resp_p, "proto": proto, "trans_id": trans_id, "rtt": rtt, "query": query, "qclass": qclass, "qclass_name": qclass_name, "qtype": qtype, "qtype_name": qtype_name, "AA": AA, "TC": TC, "RD": RD, "RA": RA, "Z": Z, "answers": answers, "TTLs": TTLs, "rejected": rejected}

        # HTTP logs
        trans_depth = 1
        method = random.choice(methods)
        host = "www.faceclone.com"
        uri = random.choice(urls)
        referrer = "www.google.com"
        version = "1.1"
        user_agent = random.choice(user_agents)
        request_body_len = random.randint(0, 2000)
        response_body_len = random.randint(0, 2000)
        status_code = random.randint
        status_code = random.randint(200, 500)
        status_msg = "OK" if status_code == 200 else "Error"
        info_code = "-"
        info_msg = "-"
        tags = "(empty)"
        username = "-"
        password = "-"
        proxied = "-"
        orig_fuids = "(empty)"
        orig_mime_types = "(empty)"
        resp_fuids = "(empty)"
        resp_mime_types = "(empty)"

        http_f.write(f"{ts}\t{uid}\t{id_orig_h}\t{id_orig_p}\t{id_resp_h}\t{id_resp_p}\t{trans_depth}\t{method}\t{host}\t{uri}\t{referrer}\t{version}\t{user_agent}\t{request_body_len}\t{response_body_len}\t{status_code}\t{status_msg}\t{info_code}\t{info_msg}\t{tags}\t{username}\t{password}\t{proxied}\t{orig_fuids}\t{orig_mime_types}\t{resp_fuids}\t{resp_mime_types}\n")

        # SSL logs
        version = random.choice(ssl_versions)
        cipher = random.choice(ssl_cipher_suites)
        server_name = "www.faceclone.com"
        resumed = random.choice([True, False])
        established = random.choice([True, False])
        cert_chain_fuids = "(empty)"
        client_cert_chain_fuids = "(empty)"
        subject = "CN=www.faceclone.com"
        issuer = "CN=Faceclone Root CA"
        client_subject = "-"
        client_issuer = "-"
        validation_status = "ok"
        ja3 = fake.sha256()
        ja3s = fake.sha256()

        ssl_f.write(f"{ts}\t{uid}\t{id_orig_h}\t{id_orig_p}\t{id_resp_h}\t{id_resp_p}\t{version}\t{cipher}\t{server_name}\t{resumed}\t{established}\t{cert_chain_fuids}\t{client_cert_chain_fuids}\t{subject}\t{issuer}\t{client_subject}\t{client_issuer}\t{validation_status}\t{ja3}\t{ja3s}\n")
