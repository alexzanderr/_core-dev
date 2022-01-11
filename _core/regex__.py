

import re


ip_regex_section = "(\\d{1,2}|(0|1)\\d{2}|2[0-4]\\d|25[0-5])"
ip_regex = re.compile(ip_regex_section + "\\." +  ip_regex_section + "\\." + ip_regex_section + "\\." + ip_regex_section)

def is_valid_IP_address(ip_address):
    return ip_regex.fullmatch(ip_address) != None



if __name__ == "__main__":
    ip_addresses = [
        '23.45.12.56',
        'I.Am.not.an.ip'
    ]

    for ip in ip_addresses:
        print(is_valid_IP_address(ip))
