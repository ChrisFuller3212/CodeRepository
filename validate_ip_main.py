"""

Main program for: validate_ip.py
By: CHRISTIAN FULLER

"""

import validate_ip

def main():
    while True:
        ip_addr_str = input('Enter a IP address: ')
        subnet_mask_str = input('Enter a network mask: ')
        ipresult = validate_ip.validate_ip_address(ip_addr_str)
        netmaskresult = validate_ip.validate_subnet_mask(subnet_mask_str)
        print(ipresult)
        print(netmaskresult)
        break

if __name__ == '__main__':
    main()