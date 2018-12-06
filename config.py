#!usr/bin/python
__author__ = 'u671436'
import base64

#Encoded password, python decodes while connecting to dB

host = "ipvrw00a0006.wellsfazargo.com"
user = "WWS_Strategies"
passwd = base64.b64decode("QWk5MjM0TnlkI2N4MDJkMDg=")
db = "HCM"

#Getting some special charecters from HCM dB like %20 and %2C
#Replacing those in the query
#Example replace('%2C', ',') and replace('%20', ' ')

def query(hostname):
    return """select Server_Name,HPSA_Mesh,Remote_Console_IP,replace(Serial,'%20', ' ') as serial,
    BoKS_KEON,BMC_Firmware,DNS_Domain,replace(DRAC,'%20', ' ') as DRAC,
    replace(Model,'%20', ' ') as Model,
    OS_Type,OS_Version,
    OS_Version_Minor,
    replace(replace(FC_HBA_Info1,'%2C', ','),'%20', ' ') as HBA_Info1,
    replace(replace(FC_HBA_Info2,'%2C', ','),'%20', ' ') as FC_HBA_Info2,
    replace(replace(FC_HBA_Info3,'%2C', ','),'%20', ' ') as FC_HBA_Info3,
    replace(replace(FC_HBA_Info4,'%2C', ','),'%20', ' ') as FC_HBA_Info4,
    replace(replace(FC_HBA_Info5,'%2C', ','),'%20', ' ') as FC_HBA_Info5,
    replace(replace(FC_HBA_Info6,'%2C', ','),'%20', ' ') as FC_HBA_Info6,
    replace(replace(FC_HBA_Info7,'%2C', ','),'%20', ' ') as FC_HBA_Info7,
    replace(replace(FC_HBA_Info8,'%2C', ','),'%20', ' ') as FC_HBA_Info8,
    replace(replace(FC_HBA_Info9,'%2C', ','),'%20', ' ') as FC_HBA_Info9,
    replace(replace(FC_HBA_Info10,'%2C', ','),'%20', ' ') as FC_HBA_Info10,
    replace(Memory,'%20', ' ') as Memory,
    replace(replace(replace(replace(Memory_Info1,'%2C', ','),'%20', ' '),'%28', ''),'%29', '') as Memory_Info1,
    replace(replace(replace(replace(Memory_Info2,'%2C', ','),'%20', ' '),'%28', ''),'%29', '') as Memory_Info2,
    replace(replace(replace(replace(Memory_Info3,'%2C', ','),'%20', ' '),'%28', ''),'%29', '') as Memory_Info3,
    replace(replace(replace(replace(Memory_Info4,'%2C', ','),'%20', ' '),'%28', ''),'%29', '') as Memory_Info4,
    replace(replace(replace(replace(Memory_Info5,'%2C', ','),'%20', ' '),'%28', ''),'%29', '') as Memory_Info5,
    replace(replace(replace(replace(Memory_Info6,'%2C', ','),'%20', ' '),'%28', ''),'%29', '') as Memory_Info6,
    replace(replace(replace(replace(Memory_Info7,'%2C', ','),'%20', ' '),'%28', ''),'%29', '') as Memory_Info7,
    replace(replace(replace(replace(Memory_Info8,'%2C', ','),'%20', ' '),'%28', ''),'%29', '') as Memory_Info8,
    replace(replace(replace(replace(Memory_Info9,'%2C', ','),'%20', ' '),'%28', ''),'%29', '') as Memory_Info9,
    replace(replace(replace(replace(Memory_Info10,'%2C', ','),'%20', ' '),'%28', ''),'%29', '') as Memory_Info10,
    replace(replace(replace(Physical_Type,'%2C', ','),'%20', ' '),'%3A', ':') as Physical_Type,
    replace(replace(replace(Physical_Disk1,'%2C', ','),'%20', ' '),'%3A', ':') as Physical_Disk1,
    replace(replace(replace(Physical_Disk2,'%2C', ','),'%20', ' '),'%3A', ':') as Physical_Disk2,
    replace(replace(replace(Physical_Disk3,'%2C', ','),'%20', ' '),'%3A', ':') as Physical_Disk3,
    replace(replace(replace(Physical_Disk4,'%2C', ','),'%20', ' '),'%3A', ':') as Physical_Disk4,
    replace(replace(replace(Physical_Disk5,'%2C', ','),'%20', ' '),'%3A', ':') as Physical_Disk5,
    replace(replace(replace(Physical_Disk6,'%2C', ','),'%20', ' '),'%3A', ':') as Physical_Disk6,
    replace(replace(replace(Physical_Disk7,'%2C', ','),'%20', ' '),'%3A', ':') as Physical_Disk7,
    replace(replace(replace(Physical_Disk8,'%2C', ','),'%20', ' '),'%3A', ':') as Physical_Disk8,
    replace(replace(replace(Physical_Disk9,'%2C', ','),'%20', ' '),'%3A', ':') as Physical_Disk9,
    replace(replace(replace(Physical_Disk10,'%2C', ','),'%20', ' '),'%3A', ':') as Physical_Disk10,
    Architecture,IP_Addresses,Kernel,Last_Bundle,replace(Legacy_Name,'%20', ' ') as Legacy_Name,
    replace(replace(MAC_Addresses,'%3A', ':'),'%20', ' ') as MAC_Addresses 
    from HCM_CA_data where Server_Name like '{}';""".format(hostname)
