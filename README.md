# All ports are OPEN. Honeypot.

Writeup: http://www.korznikov.com/2014/10/every-port-is-open-for-security.html

Dependencies: 
  iptables
  ipset

Make sure to add these rules to iptables:
```
iptables -A OUTPUT -p tcp -m tcp --tcp-flags RST RST -j DROP
iptables -A OUTPUT -p icmp -m icmp --icmp-type 3 -j DROP
iptables -t nat -A PREROUTING -p tcp -m set --match-set rports dst -j REDIRECT --to-ports 8888
```
Then run some application, that will listen on 8888 port:

socat TCP-LISTEN:8888,reuseaddr,fork -

# op_generate.py
will generate ipset within 1-65535 ports range and will exclude currently opened ports.

# op_monitor.py
script that monitor netstat output for newly opened/closed ports, then add it or remove from ipset.
