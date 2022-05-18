from ast import Index
import telnetlib
import getpass


user = input("Enter the Username: ")
password = getpass.getpass("Enter the Telnet Password: ")

f_handler = open('sw.txt')
count = 3

for line in f_handler:
    HOST = line.strip('\n')
    print("Telnet to host: " + HOST)
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"configure terminal\n")
    tn.write(b"ip routing\n")

    for i in range(2, 10):
        count = count + 1

       
        
        tn.write(b"vlan " + str(i).encode('ascii') + b"\n")
        tn.write(b"name VLAN_" + str(i).encode('ascii') + b"\n")

            
        if i == 3:
            tn.write(b"name Management" + b"\n")
            tn.write(b"int vlan 3\n")
            tn.write(b"ip address 10.10." + str(count + 1).encode('ascii') + b".2 255.255.255.0\n")
            tn.write(b"no shutdown\n")
            tn.write(b"exit\n")
            tn.write(b"int g1/1\n")
            tn.write(b"switchport mode access\n")
            tn.write(b"switchport access vlan 3\n")
            tn.write(b"exit\n")
            tn.write(b"ip default-gateway 10.10." + str(count + 1).encode('ascii') + b".1\n")

            ###### Management DHCP
            tn.write(b"ip dhcp exclude 10.10." + str(count + 1).encode('ascii') + b".1 10.10." + str(count + 1).encode('ascii') + b".100\n")
            tn.write(b"ip dhcp pool VLAN_Management_" + str(i).encode('ascii') + b"\n")
            tn.write(b"network 10.10." + str(count + 1).encode('ascii') + b".0 255.255.255.0\n")
            tn.write(b"defau 10.10." + str(count + 1).encode('ascii') + b".1\n")
            tn.write(b"dns 8.8.8.8\n")
            tn.write(b"exit\n")

            ######## routing switch
            tn.write(b"router ospf 3\n")
            tn.write(b"router-id " + str(i+1).encode('ascii') + b"." + str(i+1).encode('ascii') + b"." + str(count + 5).encode('ascii') + b"." + b"1 \n")
            tn.write(b"network 10.10." + str(count + 1).encode('ascii') + b".0 0.0.0.255 area 0\n")
            tn.write(b"network 0.0.0.0 0.0.0.0 area 0\n")
            tn.write(b"network " + str(HOST).encode('ascii') + b" 0.0.0.255 area 0\n")
        
        if i == 4:
            tn.write(b"name Student" + b"\n")
            tn.write(b"int vlan 4\n")
            tn.write(b"ip address 10.10." + str(count + 2).encode('ascii') + b".2 255.255.255.0\n")
            tn.write(b"no shutdown\n")
            tn.write(b"exit\n")
            tn.write(b"int g1/2\n")
            tn.write(b"switchport mode access\n")
            tn.write(b"switchport access vlan 4\n")
            tn.write(b"exit\n")
            tn.write(b"ip default-gateway 10.10." + str(count + 2).encode('ascii') + b".1\n")

            ############## Student DHCP
            tn.write(b"ip dhcp exclude 10.10." + str(count + 2).encode('ascii') + b".1 10.10." + str(count + 2).encode('ascii') + b".10\n")
            tn.write(b"ip dhcp pool VLAN_Student_" + str(i).encode('ascii') + b"\n")
            tn.write(b"network 10.10." + str(count + 2).encode('ascii') + b".0 255.255.255.0\n")
            tn.write(b"defau 10.10." + str(count + 2).encode('ascii') + b".1\n")
            tn.write(b"dns 8.8.8.8\n")
            tn.write(b"exit\n")


             ######## routing switch
            tn.write(b"router ospf 4\n")
            tn.write(b"router-id " + str(i+2).encode('ascii') + b"." + str(i).encode('ascii') + b"." + str(count + 5).encode('ascii') + b"." + b"1 \n")
            tn.write(b"network 10.10." + str(count + 2).encode('ascii') + b".0 0.0.0.255 area 0\n")
            tn.write(b"network 0.0.0.0 0.0.0.0 area 0\n")
            tn.write(b"network " + str(HOST).encode('ascii') + b" 0.0.0.255 area 0\n")
        
        if i == 5:
            tn.write(b"name Staff" + b"\n")
            tn.write(b"int vlan 5\n")
            tn.write(b"ip address 10.10." + str(count + 3).encode('ascii') + b".2 255.255.255.0\n")
            tn.write(b"no shutdown\n")
            tn.write(b"exit\n")
            tn.write(b"int g1/3\n")
            tn.write(b"switchport mode access\n")
            tn.write(b"switchport access vlan 5\n")
            tn.write(b"exit\n")
            tn.write(b"ip default-gateway 10.10." + str(count + 3).encode('ascii') + b".1\n")

            ############## Staff DHCP
            tn.write(b"ip dhcp exclude 10.10." + str(count + 3).encode('ascii') + b".1 10.10." + str(count + 3).encode('ascii') + b".10\n")
            tn.write(b"ip dhcp pool VLAN_Staff_" + str(i).encode('ascii') + b"\n")
            tn.write(b"network 10.10." + str(count + 3).encode('ascii') + b".0 255.255.255.0\n")
            tn.write(b"defau 10.10." + str(count + 3).encode('ascii') + b".1\n")
            tn.write(b"dns 8.8.8.8\n")
            tn.write(b"exit\n")


             ######## routing switch
            tn.write(b"router ospf 5\n")
            tn.write(b"router-id " + str(i+3).encode('ascii') + b"." + str(i).encode('ascii') + b"." + str(count + 5).encode('ascii') + b"." + b"1 \n")
            tn.write(b"network 10.10." + str(count + 3).encode('ascii') + b".0 0.0.0.255 area 0\n")
            tn.write(b"network 0.0.0.0 0.0.0.0 area 0\n")
            tn.write(b"network " + str(HOST).encode('ascii') + b" 0.0.0.255 area 0\n")

            break



    tn.write(b"end\n")
    ##tn.write(b"wr\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode())