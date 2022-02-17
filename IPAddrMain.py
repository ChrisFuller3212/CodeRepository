"""

Main program for: IPAddr.py
By: CHRISTIAN FULLER

"""

from IPAddr import IPAddr

def main():
    x = IPAddr()
    while True:
        ip_addr_str = input('Enter a IP address: ')
        #subnet_mask_str = input('Enter a network mask: ')
        x.setIPAddr(ip_addr_str)
        if x.IPAddrStrOK:
            break
        else:
            print('try again')

    while True:
        nm_addr_str = input('Enter a network mask: ')
        x.setNMAddr(nm_addr_str)
        if x.NMAddrStrOK:
            break
        else:
            print('try again')
    x.getNMAddr()
    bitwiseAnd = x.getIPNetworkOnly()
    oct1 = str(int(bitwiseAnd[:8], 2))
    oct2 = str(int(bitwiseAnd[8:16], 2))
    oct3 = str(int(bitwiseAnd[16:24], 2))
    oct4 = str(int(bitwiseAnd[24:32], 2))
    network = oct1 + '.' + oct2 + '.' + oct3 + '.' + oct4
    networkHosts = (2**format(x.getNMAddr(), '032b') .count('0'))

    print('The total number of usable hosts on network ' + network + 'is' + str(networkHosts))

if __name__ == '__main__':
    main()