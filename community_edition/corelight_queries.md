# Corelight Queries by Log Type

1. **conn.log**
   - Query: `src_ip == 10.0.0.1 && dst_port == 22 && service == "ssh"`
   - Description: This query is looking for SSH connections from the source IP 10.0.0.1.

2. **dns.log**
   - Query: `query == "*.exe" || query == "*.dll"`
   - Description: This query is looking for DNS requests for .exe or .dll files, which could indicate malicious activity.

3. **http.log**
   - Query: `status_code >= 400`
   - Description: This query is looking for HTTP requests that returned a status code of 400 or higher, indicating an error.

4. **files.log**
   - Query: `fuid == "F2Lk1a4G3ZunZiIlH7" && mime_type == "application/x-dosexec"`
   - Description: This query is looking for a specific file with a unique identifier and a MIME type of "application/x-dosexec", which could indicate a Windows executable.

5. **ssl.log**
   - Query: `validation_status == "certificate expired"`
   - Description: This query is looking for SSL connections where the certificate has expired.

6. **notice.log**
   - Query: `note == "Scan::Port_Scan" && src_ip == 10.0.0.1`
   - Description: This query is looking for notices of a port scan originating from the source IP 10.0.0.1.

7. **conn.log**
   - Query: `duration > 1h && service == "ssh"`
   - Description: This query is looking for SSH connections that lasted longer than 1 hour.

8. **http.log**
   - Query: `method == "POST" && uri == "/login"`
   - Description: This query is looking for HTTP POST requests to a /login URI, which could indicate a login attempt.

9. **dns.log**
   - Query: `answer == "192.168.1.1" && rcode == "NOERROR"`
   - Description: This query is looking for DNS responses that returned the IP address 192.168.1.1 and a response code of "NOERROR".

10. **files.log**
    - Query: `seen_bytes > 1000000 && mime_type == "application/pdf"`
    - Description: This query is looking for PDF files that are larger than 1MB.


11. **HTTP Logs (`http.log`):**

   - Identify the most common user agents:
     ```
     groupBy(user_agent, function=count(user_agent), limit=10)
     ```

   - Identify the most common HTTP methods:
     ```
     groupBy(method, function=count(method), limit=10)
     ```

12. **Connection Logs (`conn.log`):**

   - Identify the most common source IP addresses:
     ```
     groupBy(id.orig_h, function=count(id.orig_h), limit=10)
     ```

   - Identify the most common destination ports:
     ```
     groupBy(id.resp_p, function=count(id.resp_p), limit=10)
     ```

13. **DNS Logs (`dns.log`):**

   - Identify the most common DNS queries:
     ```
     groupBy(query, function=count(query), limit=10)
     ```

   - Identify the most common DNS answers:
     ```
     groupBy(answer, function=count(answer), limit=10)
     ```

14. **SSL Logs (`ssl.log`):**

   - Identify the most common server names:
     ```
     groupBy(server_name, function=count(server_name), limit=10)
     ```

   - Identify the most common SSL versions:
     ```
     groupBy(version, function=count(version), limit=10)
     ```

15. **Files Logs (`files.log`):**

   - Identify the most common MIME types:
     ```
     groupBy(mime_type, function=count(mime_type), limit=10)
     ```

   - Identify the most common file names:
     ```
     groupBy(filename, function=count(filename), limit=10)
     ```

16. **HTTP Logs (`http.log`):**

   - Identify all HTTP GET requests to a specific domain and group them by user agent:
     ```
     method == "GET" && domain == "suspicious.com" | groupBy(user_agent, function=count(user_agent), limit=10)
     ```

17. **Connection Logs (`conn.log`):**

   - Identify all connections from a specific IP address and group them by destination port:
     ```
     id.orig_h == "192.0.2.0" | groupBy(id.resp_p, function=count(id.resp_p), limit=10)
     ```

18. **DNS Logs (`dns.log`):**

   - Identify all DNS queries for a specific domain and group them by query type:
     ```
     query == "suspicious.com" | groupBy(qtype_name, function=count(qtype_name), limit=10)
     ```

19. **SSL Logs (`ssl.log`):**

   - Identify all SSL connections to a specific server and group them by SSL version:
     ```
     server_name == "secure.example.com" | groupBy(version, function=count(version), limit=10)
     ```

20. **Files Logs (`files.log`):**

   - Identify all files of a specific MIME type and group them by file name:
     ```
     mime_type == "application/pdf" | groupBy(filename, function=count(filename), limit=10)
     ```

