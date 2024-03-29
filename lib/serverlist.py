######## Host port mapping
########
#### URL Monitoring ---> add new entry in existing server 
######## format ---> "url<anything>":"a url without http( localhost or ip )"
#
### Process Monitoring ---> add new entry in existing server
####### format ---> "process_<exact name of process to grep>":"<count of that process>"
###
#### Port Monitoring ---> anything else not in format of URL and Process is considered port entry

papyrus= {
"uk1py01tsb":{"19050":"IPAM","19051":"DC","19049":"NODE01"},
"uk1py03tsb":{"19021":"NODE01_pocx3knl","19022":"NODE02_pocx3knl","19023":"NODE03_pocx3knl","19024":"NODE04_pocx3knl","80":"HTTP","666":"HTTP","443":"HTTPS","1930":"pocx3htp","1931":"pocx3htp","1932":"pocx3htp","1933":"pocx3htp","url5":"10.184.54.151/ok.html","url1":"127.0.0.1:1930/GDC0001.html","url2":"127.0.0.1:1931/GDC0001.html","url3":"127.0.0.1:1932/GDC0001.html","url4":"127.0.0.1:1933/GDC0001.html","process_pocx3htp":"4","process_pdex3":"24","process_pocx3knl":"4"},
"uk1py05tsb":{"19025":"NODE05_pocx3knl","19026":"NODE06_pocx3knl","19027":"NODE07_pocx3knl","19028":"NODE08_pocx3knl","80":"HTTP","666":"HTTP","443":"HTTPS","1934":"pocxhtp","1935":"pocxhtp","1936":"pocxhtp","1937":"pocxhtp","url5":"10.184.54.153/ok.html","url1":"127.0.0.1:1934/GDC0001.html","url2":"127.0.0.1:1935/GDC0001.html","url3":"127.0.0.1:1936/GDC0001.html","url4":"127.0.0.1:1937/GDC0001.html","process_pocx3htp":"4","process_pdex3":"24","process_pocx3knl":"4"},
"uk1py07tsb":{"19029":"NODE09_pocx3knl","19030":"NODE10_pocx3knl","19031":"NODE11_pocx3knl","80":"HTTP","666":"HTTP","443":"HTTPS","1938":"pocxhtp","1939":"pocxhtp","1940":"pocxhtp","url4":"10.184.54.155/ok.html","url1":"127.0.0.1:1938/GDC0001.html","url2":"127.0.0.1:1939/GDC0001.html","url3":"127.0.0.1:1940/GDC0001.html","process_pocx3htp":"3","process_pdex3":"18","process_pocx3knl":"3"},
"uk2py01tsb":{"19050":"IPAM","19051":"DC","19049":"NODE01"},
"uk2py03tsb":{"19021":"NODE01_pocx3knl","19022":"NODE02_pocx3knl","19023":"NODE03_pocx3knl","19024":"NODE04","80":"HTTP","666":"HTTP","443":"HTTPS","1930":"pocx3htp","1931":"pocx3htp","1932":"pocx3htp","1933":"pocx3htp","url5":"10.185.54.149/ok.html","url1":"127.0.0.1:1930/GDC0001.html","url2":"127.0.0.1:1931/GDC0001.html","url3":"127.0.0.1:1932/GDC0001.html","url4":"127.0.0.1:1933/GDC0001.html","process_pocx3htp":"4","process_pdex3":"24","process_pocx3knl":"4"},
"uk2py05tsb":{"19025":"NODE05_pocx3knl","19026":"NODE06_pocx3knl","19027":"NODE07_pocx3knl","19028":"NODE08_pocx3knl","80":"HTTP","666":"HTTP","443":"HTTPS","1934":"pocxhtp","1935":"pocxhtp","1936":"pocxhtp","1937":"pocxhtp","url5":"10.185.54.151/ok.html","url1":"127.0.0.1:1934/GDC0001.html","url2":"127.0.0.1:1935/GDC0001.html","url3":"127.0.0.1:1936/GDC0001.html","url4":"127.0.0.1:1937/GDC0001.html","process_pocx3htp":"4","process_pdex3":"24","process_pocx3knl":"4"},
"uk2py07tsb":{"19029":"NODE09_pocx3knl","19030":"NODE10_pocx3knl","19031":"NODE11_pocx3knl","80":"HTTP","666":"HTTP","443":"HTTPS","1938":"pocxhtp","1939":"pocxhtp","1940":"pocxhtp","url4":"10.185.54.153/ok.html","url1":"127.0.0.1:1938/GDC0001.html","url2":"127.0.0.1:1939/GDC0001.html","url3":"127.0.0.1:1940/GDC0001.html","process_pocx3htp":"3","process_pdex3":"18","process_pocx3knl":"3"},
}


ondemand={
"uk1od01tsb":{"9080":"server1","9081":"server2","9082":"server3","80":"HTTP","url1":"http://localhost:9080/navigator","url3":"http://localhost:9080/samlsps/","url2":"http://localhost:9080/tsbSSOPlugin/sso.properties","url4":"http://localhost:9081/gdOnDemand/servlet/gdOnDemand","url5":"http://localhost:9082/docGeneration/","process_server1":"3"},
"uk1od11tsb":{"9080":"server1","9081":"server2","9082":"server3","url1":"http://localhost:9080/navigator","url4":"http://localhost:9081/gdOnDemand/servlet/gdOnDemand","url5":"http://localhost:9082/docGeneration/","process_server1":"3"},
"uk2od01tsb":{"9080":"server1","9081":"server2","9082":"server3","80":"HTTP","url1":"http://localhost:9080/navigator","url3":"http://localhost:9080/samlsps/","url2":"http://localhost:9080/tsbSSOPlugin/sso.properties","url4":"http://localhost:9081/gdOnDemand/servlet/gdOnDemand","url5":"http://localhost:9082/docGeneration/","process_server1":"3"}
}


jboss={
"es4jb04bsab":{"4448":"JBoss", "3873":"JBoss", "3528":"JBoss", "8009":"JBoss", "4457":"JBoss", "1098":"JBoss", "1099":"JBoss", "1100":"JBoss", "1101":"JBoss", "8083":"JBoss", "8565":"JBoss", "7900":"JBoss", "4444":"JBoss", "4445":"JBoss", "4446":"JBoss", "4447":"JBoss","process_deritsb":"2","process_deriuattsb":"2"},
}


treasury={
"uk1ti01tsb":{"1416":"MQMGR QMPRO"},
"uk1ti11tsb":{"1416":"MQMGR QMTSBGOS"}
}

