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
    number = ['']
    for j in range(3):
        if int(ip[j]) < 100:
            number[0] += '0'
        if int(ip[j]) < 10:
            number[0] += '0'
        number[0] += ip[j]
    number[0] = int(number[0])
    number.append(int(ip[-1])) 
    return number

useless_routers = []

for start_ip, end_ip in ip_ranges:
    if make_int(end_ip)[-1] == 1:
        useless_routers.append(end_ip)

for router in useless_routers:
    router_first_digits = make_int(router)[0] 
    for start_ip, end_ip in ip_ranges:
        start_ip_first_digits = make_int(start_ip)[0]
        end_ip_first_digits = make_int(end_ip)[0]
        end_ip_last_digits = make_int(end_ip)[1]
        if router_first_digits >= start_ip_first_digits and (router_first_digits < end_ip_first_digits or (end_ip_last_digits != 1 and router_first_digits == end_ip_fist_digits)):
            useless_routers.remove(router)

print(useless_routers)
