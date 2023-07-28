## Conn Logs
```
| parseCSV("ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,proto,service,duration,orig_bytes,resp_bytes,conn_state,local_orig,local_resp,missed_bytes,history,orig_pkts,orig_ip_bytes,resp_pkts,resp_ip_bytes,tunnel_parents", ",")
```
## DNS Logs
```
| parseCSV("ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,proto,trans_id,rtt,query,qclass,qclass_name,qtype,qtype_name,rcode,rcode_name,AA,TC,RD,RA,Z,answers,TTLs,rejected", ",")
```
## HTTP Logs
```
| parseCSV("ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,trans_depth,method,host,uri,referrer,version,user_agent,request_body_len,response_body_len,status_code,status_msg,info_code,info_msg,tags,username,password,proxied,orig_fuids,orig_mime_types,resp_fuids,resp_mime_types", ",")
```
## SSL Logs
```
| parseCSV("ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,version,cipher,server_name,resumed,established,cert_chain_fuids,client_cert_chain_fuids,subject,issuer,client_subject,client_issuer,validation_status,ja3,ja3s", ",")
```
