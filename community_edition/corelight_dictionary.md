**Conn Log Fields**

| Field Name | Type | Description |
| --- | --- | --- |
| `ts` | time | The timestamp at which the log entry was first written. |
| `uid` | string | A unique identifier of the connection over which this message was transmitted. |
| `id.orig_h` | addr | The originator’s IP address. |
| `id.orig_p` | port | The originator’s port number. |
| `id.resp_h` | addr | The responder’s IP address. |
| `id.resp_p` | port | The responder’s port number. |
| `proto` | enum | The transport protocol. Possible values are "tcp", "udp", "icmp", or "unknown". |
| `service` | string | The service detected on the connection. |
| `duration` | interval | The duration of the connection. |
| `orig_bytes` | count | The number of payload bytes the originator sent. |
| `resp_bytes` | count | The number of payload bytes the responder sent. |
| `conn_state` | string | The state of the connection. |
| `local_orig` | bool | Whether the connection is originated locally. |
| `local_resp` | bool | Whether the connection is responded to locally. |
| `missed_bytes` | count | The number of bytes missed by the packet filter. |
| `history` | string | The history of the connection. |
| `orig_pkts` | count | The number of packets the originator sent. |
| `orig_ip_bytes` | count | The number of IP-level bytes that the originator sent. |
| `resp_pkts` | count | The number of packets the responder sent. |
| `resp_ip_bytes` | count | The number of IP-level bytes that the responder sent. |
| `tunnel_parents` | set | If the session that this connection belongs to is tunneled, this field is a vector of the UID(s) of the tunnel(s) in which this session is encapsulated. |

**DNS Log Fields**

| Field Name | Type | Description |
|------------|------|-------------|
| `ts` | `time` | Time when the log line was written |
| `uid` | `string` | A unique identifier of the connection over which the DNS transaction occurred |
| `id.orig_h` | `addr` | The originator’s IP address |
| `id.orig_p` | `port` | The originator’s port number |
| `id.resp_h` | `addr` | The responder’s IP address |
| `id.resp_p` | `port` | The responder’s port number |
| `proto` | `enum` | The transport protocol. Currently tcp, udp, icmp, or unknown |
| `trans_id` | `count` | The DNS transaction ID |
| `rtt` | `interval` | Round trip time for the query and response |
| `query` | `string` | The requested name |
| `qclass` | `count` | The QCLASS value |
| `qclass_name` | `string` | The QCLASS name |
| `qtype` | `count` | The QTYPE value |
| `qtype_name` | `string` | The QTYPE name |
| `rcode` | `count` | The RCODE value |
| `rcode_name` | `string` | The RCODE name |
| `AA` | `bool` | The Authoritative Answer bit |
| `TC` | `bool` | The Truncation bit |
| `RD` | `bool` | The Recursion Desired bit |
| `RA` | `bool` | The Recursion Available bit |
| `Z` | `count` | The reserved Z bit |
| `answers` | `vector of string` | The set of resource descriptions in the answer section |
| `TTLs` | `vector of interval` | The TTLs of the answer RRs |
| `rejected` | `bool` | Whether the query was rejected due to the Zeek DNS policy |

**HTTP Log Fields**

| Field Name | Type | Description |
|------------|------|-------------|
| `ts` | `time` | Time when the log line was written |
| `uid` | `string` | A unique identifier of the connection over which the HTTP request was made |
| `id.orig_h` | `addr` | The originator’s IP address |
| `id.orig_p` | `port` | The originator’s port number |
| `id.resp_h` | `addr` | The responder’s IP address |
| `id.resp_p` | `port` | The responder’s port number |
| `trans_depth` | `count` | The depth into the connection of this request/response transaction |
| `method` | `string` | The HTTP method of the request |
| `host` | `string` | The value of the Host header in the request |
| `uri` | `string` | The URI used in the request |
| `referrer` | `string` | The Referrer header value |
| `version` | `string` | The HTTP version |
| `user_agent` | `string` | The User-Agent header value |
| `request_body_len` | `count` | The size of the HTTP request body |
| `response_body_len` | `count` | The size of the HTTP response body |
| `status_code` | `count` | The HTTP status code returned by the server |
| `status_msg` | `string` | The HTTP status message returned by the server |
| `info_code` | `count` | The HTTP info code |
| `info_msg` | `string` | The HTTP info message |
| `tags` | `vector of string` | Any tags set by the Zeek script layer |
| `username` | `string` | The username if HTTP Basic Authentication was performed |
| `password` | `string` | The password if HTTP Basic Authentication was performed |
| `proxied` | `vector of string` | All of the headers that are in the client request |
| `orig_fuids` | `vector of string` | The file unique IDs of any files that are part of the request |
| `orig_mime_types` | `vector of string` | The MIME types of any files that are part of the request |
| `resp_fuids` | `vector of string` | The file unique IDs of any files that are part of the response |
| `resp_mime_types` | `vector of string` | The MIME types of any files that are part of the response |

**SSL Log Fields**

| Field Name | Type | Description |
|------------|------|-------------|
| `ts` | `time` | Time when the log line was written |
| `uid` | `string` | A unique identifier of the connection that the SSL handshake was performed over |
| `id.orig_h` | `addr` | The originator’s IP address |
| `id.orig_p` | `port` | The originator’s port number |
| `id.resp_h` | `addr` | The responder’s IP address |
| `id.resp_p` | `port` | The responder’s port number |
| `version` | `string` | The SSL/TLS version that was negotiated |
| `cipher` | `string` | The SSL/TLS cipher suite that was negotiated |
| `server_name` | `string` | The server name offered by the client if the SSL/TLS Server Name Indication extension was included in the client hello |
| `resumed` | `bool` | Whether the SSL/TLS session was resumed |
| `established` | `bool` | Whether the SSL/TLS session was successfully established |
| `cert_chain_fuids` | `vector of string` | The file unique IDs of any certificate files associated with the session |
| `client_cert_chain_fuids` | `vector of string` | The file unique IDs of any client certificate files associated with the session |
| `subject` | `string` | The subject DN of the X.509 certificate offered by the server |
| `issuer` | `string` | The issuer DN of the X.509 certificate offered by the server |
| `client_subject` | `string` | The subject DN of the X.509 certificate offered by the client |
| `client_issuer` | `string` | The issuer DN of the X.509 certificate offered by the client |
| `validation_status` | `string` | The validation status of the server certificate |
| `ja3` | `string` | The JA3 fingerprint |
| `ja3s` | `string` | The JA3S fingerprint |

Here are the fields for the `x509.log`:

| Field Name | Type | Description |
| --- | --- | --- |
| `ts` | timestamp | The timestamp of the event. |
| `id` | string | The unique identifier for the event. |
| `certificate` | object | Contains the following fields: certificate_version, certificate_serial, certificate_subject, certificate_issuer, certificate_not_valid_before, certificate_not_valid_after, certificate_key_algorithm, certificate_signing_algorithm, certificate_key_type, certificate_key_length, certificate_exponent, certificate_curve. |
| `san` | object | Contains the following fields: san_dns, san_uri, san_email, san_ip. |
| `basic_constraints` | object | Contains the following fields: basic_constraints_ca, basic_constraints_path_length. |


**DHCP Log Fields**

| Field Name | Type | Description |
| --- | --- | --- |
| `ts` | time | The timestamp when the log line was generated. |
| `uid` | string | A unique identifier of the connection over which this message was transmitted. |
| `id.orig_h` | addr | The originator’s IP address. |
| `id.orig_p` | port | The originator’s port number. |
| `id.resp_h` | addr | The responder’s IP address. |
| `id.resp_p` | port | The responder’s port number. |
| `mac` | string | The MAC address of the client. |
| `assigned_ip` | addr | The IP address assigned to the client. |
| `lease_time` | interval | The lease time in seconds. |
| `trans_id` | count | The transaction ID. |

**DNP3 Log Fields**

| Field Name | Type | Description |
| --- | --- | --- |
| `ts` | time | The timestamp when the log line was generated. |
| `uid` | string | A unique identifier of the connection over which this message was transmitted. |
| `id.orig_h` | addr | The originator’s IP address. |
| `id.orig_p` | port | The originator’s port number. |
| `id.resp_h` | addr | The responder’s IP address. |
| `id.resp_p` | port | The responder’s port number. |
| `func` | string | The DNP3 function code. |
| `obj` | string | The DNP3 object. |
