#!/usr/bin/python
#__author__ Alexander Korznikov @nopernik

from subprocess import check_output
import re
from time import sleep
import os

set_name = 'rports'

def open_ports():
   netstat = check_output('netstat -tan',shell=True)
   lports = re.findall(r'(?<=\:)[0-9]{1,5}\w(?=.+listen)',netstat.lower())
   lports = list(set(lports))
   return lports

tmp_ports = []

while 1:
   openports = open_ports()
   new_open = list(set(openports) - set(tmp_ports))
   new_closed = list(set(tmp_ports) - set(openports))
   if len(new_open):
     for port in new_open:
       print '[-] Removing port %s from ipset' % port
       os.system('ipset del %s %s' % (set_name,port))
   if len(new_closed):
     for port in new_closed:
       print '[+] Adding port %s to ipset' % port
       os.system('ipset add %s %s' % (set_name,port))
   tmp_ports = openports
   sleep(1)
