"""

validate_ip.py

By: CHRISTIAN FULLER

"""

#this is the validate ip address function that validates the ip address entered by the user.
#what happens in the first few lines is the splitting of the entered string into a list
#so the function can check to see if the string entered is valid or not.

def validate_ip_address(ip_addr_str):
    ipOctets = ip_addr_str.split(".")
    #here is where the validation begins for the ip address string
    if (len(ipOctets) != 4):
        return (False, 0, 0, 0, 0, 0)
    for o in ipOctets:
        if o.isdigit() == False:
            return (False, 0, 0, 0, 0, 0)
        if (int(o) < 0) or (int(o) > 255):
            return (False, 0, 0, 0, 0, 0)
#here is where each octet of the strings entered is converted to integers so that 
#we can multiply them to calculate the integer value of the ip address entered.
    oct1 = int(ipOctets[0])
    oct2 = int(ipOctets[1])
    oct3 = int(ipOctets[2])
    oct4 = int(ipOctets[3])
    num = (oct1*256**3) + (oct2*256**2) + (oct3*256**1)+ (oct1*256)
#this simply states that if the results up to this point are false, print false in this format
#likewise if the result is true, print or return in this format.
    return (True, num, oct1, oct2, oct3, oct4)
#this function is very simplar to the first in almost every way as this function
#validated the subnetmask entered. Last assignment, I validated the networkmask using
#.join to join lists which is hard to do, so this time around i used easier definition of variables.
def validate_subnet_mask(subnet_mask_str):
    netmaskOctets = subnet_mask_str.split(".")
    if (len(netmaskOctets) != 4):
        return (False, 0, 0, 0, 0, 0)
    for o in netmaskOctets:
        if o.isdigit() == False:
            return (False, 0, 0, 0, 0, 0)
        if (int(o) < 0) or (int(o) > 255):
            return (False, 0, 0, 0, 0, 0)
#again, i am converting the ctrings to integers for arithmetic
    oct1 = int(netmaskOctets[0])
    oct2 = int(netmaskOctets[1])
    oct3 = int(netmaskOctets[2])
    oct4 = int(netmaskOctets[3])
    num = (oct1*256**3) + (oct2*256**2) + (oct3*256**1)+ (oct1*256)  
#here is rthe difference: starting here, i immediatly say
#if the string entered is not a valid entry from the previous function, then its false.
    if not validate_ip_address(subnet_mask_str):
        return (False, 0, 0, 0, 0, 0)
#then, i say here:
#if the string entered is 1, the result is false but if the string entered is 0, it is true.
    isbitZero = subnet_mask_str[0] == "0"
    for bit in subnet_mask_str[1]:
        if bit == "1" and isbitZero:
            return (False, 0, 0, 0, 0, 0)
        if bit == "0":
            return (False, 0, 0, 0, 0, 0)
#this was the easiest part because im basically just printing the results that were already found
#into the format requested in the assignment
    return (True, num, oct1, oct2, oct3, oct4)