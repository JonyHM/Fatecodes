ip = open('IPS.txt', 'r')
val = open('Validos.txt', 'w')
inv = open('Invalidos.txt', 'w')

def ip_val(ip):
    ips = ip.split('.')
    for numero in ips:
        if int(numero) > 255:
            return False
    return True

for line in ip:
    if ip_val(line.strip()):
        val.write(line)
    else:
        inv.write(line)
    
ip.close()
val.close()
inv.close()
