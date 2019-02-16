###################################
# O365-select.py
# EN : this script is a customization of the microsoft script, it allows to extract the IP of some services of microsoft to integrate them in a file txt for feeds / dynamic ip list. it can be started by a task scheduled to be up to date.
# FR: ce script est une personnalisatin du script de microsoft , il permet extraire les IP  de certains services de microsoft  pour les integrer dans un fichier txt  pour des feeds / dynamic ip list . il peut etre lancé par une tache planifié  pour etre a jour . 
# 
# for start script :python3  O365-select.py
#
# pre-requis/ Pre-requisites : python 3
#
#
#by Macpav   - 16/02/2019
####################################
import json
import os
import urllib
from urllib.request import urlopen
import uuid
# helper to call the webservice and parse the response
def webApiGet(methodName, instanceName, clientRequestId):
    ws = "https://endpoints.office.com"
    requestPath = ws + '/' + methodName + '/' + instanceName + '?clientRequestId=' + clientRequestId
    request = urllib.request.Request(requestPath)
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode())
#####################################
# champs de recherche pour extraire les IP / pattern for extract all IP 
ndd_extract='*.mail.protection.outlook.com'
# repertoire et ou fichier pour creer le fichier txt ( stockage de parametre aussi ) / directory and or file to create the txt file (parameter storage too)
datapath = 'mail_protection_outlook_com.txt'
# 1 pour voir l'execution du script O pour ne rien voir  / 1 to see the execution of the script O to see nothing
show = '0'
#####################################
# fetch client ID and version if data exists; otherwise create new file
if os.path.exists(datapath):
    with open(datapath, 'r') as fin:
        for line in fin:
            if line.startswith( '####version=' ) :
                line = line.replace("####version=", "")
                latestVersion =line
            if line.startswith( '####RequestId=' ) :
                line = line.replace("####RequestId=", "")
                clientRequestId =line
else:
    clientRequestId = str(uuid.uuid4())
    latestVersion = '0000000000'
    file = open(datapath,"w") 
    file.write('####version='+latestVersion+'\n####RequestId='+clientRequestId+'\n')
# call version method to check the latest version, and pull new data if version number is different
version = webApiGet('version', 'Worldwide', clientRequestId)
if version['latest'] > latestVersion:
    if show == '1' :    print('New version of Office 365 worldwide commercial service instance endpoints detected')
    # write the new version number to the data file
    file = open(datapath,"w") 
    file.write('####version='+version['latest']+'\n####RequestId='+clientRequestId+'\n')
    # invoke endpoints method to get the new data
    endpointSets = webApiGet('endpoints', 'Worldwide', clientRequestId)
    # filter results for Allow and Optimize endpoints, and transform these into tuples with port and category
    flatUrls2 = []
    flatIps2 = []
    for endpointSet in endpointSets:
        if endpointSet['category'] in ('Optimize', 'Allow'):
            category = endpointSet['category']
            urls = endpointSet['urls'] if 'urls' in endpointSet else []
            index=str(urls).find(ndd_extract)
            ips = endpointSet['ips'] if 'ips' in endpointSet else []
            ip4s = [ip for ip in ips if '.' in ip]
            if index == -1 :
                urls =''
                ip4s =''
            tcpPorts = endpointSet['tcpPorts'] if 'tcpPorts' in endpointSet else ''
            udpPorts = endpointSet['udpPorts'] if 'udpPorts' in endpointSet else ''
            flatUrls2.extend([(category, url, tcpPorts, udpPorts) for url in urls])
            flatIps2.extend([(category, ip, tcpPorts, udpPorts) for ip in ip4s])
    if show == '1' :    print('URLs2 for Proxy Server')
    if show == '1' :    print(','.join(sorted(set([url for (category, url, tcpPorts, udpPorts) in flatUrls2]))))
    if show == '1' :    print('IPv4 Firewall IP Address Ranges')
    file.write('\n' .join(sorted(set([ip for (category, ip, tcpPorts, udpPorts) in flatIps2])))) 
    file.close() 
    if show == '1' :    print(','.join(sorted(set([ip for (category, ip, tcpPorts, udpPorts) in flatIps2]))))
    # TODO send mail (e.g. with smtplib/email modules) with new endpoints data
else:
    print('Office 365 worldwide commercial service instance endpoints are up-to-date')
