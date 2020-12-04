import socket
try:
    hostname = socket.gethostname() # returns hostname
    ip_address = socket.gethostbyname(hostname)  # returns IPv4 address with respect to hostname
    print('Hostname :', hostname)
    print('IP Address :', ip_address)
    fqdn = socket.getfqdn('www.google.com') # returns fully qualified domain name for name
    print('FQDN', fqdn)
    print(socket.gethostbyname_ex(hostname)) # Return a triple (hostname, aliaslist, ipaddrlist)

except:
    print('error while getting hostname or invalid hostname!')



