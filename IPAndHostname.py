import socket
try:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print('Hostname :', hostname)
    print('IP Address :', ip_address)
    fqdn = socket.getfqdn('www.google.com')
    print('FQDN', fqdn)
    print(socket.gethostbyname_ex(hostname))

except:
    print('error while getting hostname or invalid hostname!')



