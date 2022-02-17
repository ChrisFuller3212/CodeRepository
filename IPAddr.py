"""
Name: Christian Fuller
Date: 10-19-21
Description: This program will convert the IP address problem from our previous
assignments to a class of objects. The IPAddr object class has the following methods:

"""

class IPAddr(object):
    """ Method that returns a new IPAddr object """
    def __init__(self):
        """ This method initializes the program. """
        self.IPAddrStr = ""
        self.NMAddrStr = ""
        self.IPAddrStrOK = False
        self.NMAddrStrOK = False
        self.IPAddr = 0
        self.NMAddr = 0
        self.IPAddrOctets = ()
        self.NMAddrOctets = ()

    def setIPAddr(self,str):
        """ Method that Sets or resets the object's 
        string representation of an IP address. """
        ipOctets = str.split(".")
        if (len(ipOctets) != 4):
            return (False)
        for o in ipOctets:
            if o.isdigit() == False:
                return (False)
            if (int(o) < 0) or (int(o) > 255):
                return (False)
            else:
                self.IPAddrStrOK = True
                self.IPAddrStr = str
                return True

    def setNMAddr(self,str):
        """ This method sets or resets the object's 
        string representation of a network mask """
        netmaskOctets = str.split(".")
        if (len(netmaskOctets) != 4):
            return (False)
        for o in netmaskOctets:
            if o.isdigit() == False:
                return (False)
            if (int(o) < 0) or (int(o) > 255):
                return (False)
        isbitZero = str[0] == "0"
        for bit in str[1]:
            if bit == "1" and isbitZero:
                return (False)
            if bit == "0":
                return (False)
            else:
                self.NMAddrStrOK = True
                self.NMAddrStr = str
                return True

    def getIPAddr(self):
        """ This mathod returns the 32-bit representation of the objects IP address.  
        If there is no valid IP address in the object, return a zero."""
        str = self.IPAddrStr
        ipOctets = str.split(".")
        oct1 = int(ipOctets[0])
        oct2 = int(ipOctets[1])
        oct3 = int(ipOctets[2])
        oct4 = int(ipOctets[3])
        num = (oct1*256**3) + (oct2*256**2) + (oct3*256**1)+ (oct4*256)
        if self.IPAddrStrOK:
            self.IPAddr = num
            return num
        else:
            return 0

    def getNMAddr(self):
        """ This mathod returns the 32-bit representation of the objects network mask.  
        If there is no valid IP address in the object, return a zero."""
        str = self.NMAddrStr
        ipOctets = str.split(".")
        oct1 = int(ipOctets[0])
        oct2 = int(ipOctets[1])
        oct3 = int(ipOctets[2])
        oct4 = int(ipOctets[3])
        num = (oct1*256**3) + (oct2*256**2) + (oct3*256**1)+ (oct4*256)
        if self.NMAddrStrOK:
            self.NMAddr = num
            return num
        else:
            return 0

    def getIPAddrOctets(self):
        """ This method Returns a 4-element tuple that contains 
        numeric representations of the individual octets of the IP address.  
        If there is no valid IP address in the object, return an empty tuple. """
        str = self.IPAddrStr
        ipOctets = str.split(".")
        oct1 = int(ipOctets[0])
        oct2 = int(ipOctets[1])
        oct3 = int(ipOctets[2])
        oct4 = int(ipOctets[3])
        if self.IPAddrStrOK:
            return (oct1, oct2, oct3, oct4)
        else:
            return (0, 0, 0, 0)

    def getNMAddrOctets(self):
        """ This method returns a 4-element tuple that contains 
        numeric representations of the individual octets of the network mask.  
        If there is no valid network mask in the object, return an empty tuple. """
        str = self.NMAddrStr
        ipOctets = str.split(".")
        oct1 = int(ipOctets[0])
        oct2 = int(ipOctets[1])
        oct3 = int(ipOctets[2])
        oct4 = int(ipOctets[3])
        if not self.setNMAddr():
            return (oct1, oct2, oct3, oct4)
        else:
            return (0, 0, 0, 0)

    def getIPNetworkOnly(self):
        """ Returns the 32-bit representation of the 
        bitwise AND of the objects ip address and network mask.  
        If either the ip address or network mask are invalid,  the result is 0."""
        x = self.IPAddr
        y = self.NMAddr
        if self.IPAddrStrOK and self.NMAddrStrOK:
            return format(x & y, '032b')
        else:
            return 0

    def __str__(self):
        """ This method Returns a string of the ip address, a colon, and the network mask.  
        For example: 192.168.1.1:255.255.255.0  
        If either the ip address or network mask are invalid, the string will be: x.x.x.x:x.x.x.x """
        if self.IPAddrStr and self.NMAddrStr:
            return self.IPAddrStr + ':' + self.NMAddrStr
        else:
            return 'x.x.x.x:x.x.x.x'