ip_ranges = [
    ['141.255.100.1', '141.255.100.1'],
    ['5.5.5.1', '142.255.100.1'],
    ['4.4.4.1', '4.4.5.1']
    ]

def make_int(ip):
    def spl(ip):
        ip = ip.split('.')
        return ip
    ip = spl(ip)
    number_string = ['']
    for j in range(3):
        if int(ip[j]) < 100:
            number_string[0] += '0'
        if int(ip[j]) < 10:
            number_string[0] += '0'
        number_string[0] += ip[j]
    number_string[0] = int(number_string[0])
    number_string.append(int(ip[-1])) 
    return number_string

useless_routers = []

for start_ip, end_ip in ip_ranges:
    if make_int(end_ip)[-1] == 1:
        useless_routers.append(end_ip)

for router in useless_routers:
    for start_ip, end_ip in ip_ranges:
        if make_int(router)[0] >= make_int(start_ip)[0] and (make_int(router)[0] < make_int(end_ip)[0] or (make_int(end_ip)[1] != 1 and make_int(router)[0] == make_int(end_ip)[0])):
            useless_routers.remove(router)

print(useless_routers)
