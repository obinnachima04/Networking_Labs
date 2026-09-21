from netmiko import ConnectHandler

#define the device login details

devices = [ 
    {
        "name": "R1", 
        "details":{
        "device_type": "cisco_ios", 
        "host": "192.168.122.2", 
        "username": "obinna", 
        "password": "cisco"
        }
    },
        
{
    "name": "R2", 
    "details":{
        "device_type": "cisco_ios",
        "host": "192.168.122.3",
        "username": "obinna",
        "password": "cisco"
        }
    },

{
    "name": "R3", 
    "details":{
        "device_type": "cisco_ios",
        "host": "192.168.122.4",
        "username": "obinna",
        "password": "cisco"
        }
    },

{
    "name": "SW1", 
    "details":{
        "device_type": "cisco_ios",
        "host": "192.168.122.5",
        "username": "obinna",
        "password": "cisco"
        }
    },

{
    "name": "SW2", 
    "details":{
        "device_type": "cisco_ios",
        "host": "192.168.122.6",
        "username": "obinna",
        "password": "cisco"
        }
    },

{
    "name": "SW3", 
    "details":{
        "device_type": "cisco_ios",
        "host": "192.168.122.7",
        "username": "obinna",
        "password": "cisco"
        }
    },

{
    "name": "SERVER",
    "details":{
        "device_type": "cisco_ios",
        "host": "192.168.122.8",
        "username": "obinna",
        "password": "cisco"
        }
    }

]


#looping through each device

for device in devices:
    hostname = device["name"]
    device_details = device["details"]
    ip_add = device_details["host"]
    print(f"\n\nconnecting to {hostname} >>>>>>>>>>>>>>>\n")


    #establishing SSH connection
    
    connection = ConnectHandler(**device_details)

    print(f"\nSuccessfully connected to {hostname} @ {ip_add}\n")


    #running show commands

    show_interfaces = connection.send_command("sh ip int br | ex un")
    routing_table = connection.send_command("show ip route")
    running_config = connection.send_command("show run")
    cdp_neighbors = connection.send_command("sh cdp nei")
    ospf_neighbors = connection.send_command("sh ip ospf nei")

    print(f"\n ========== Active IP_Interfaces ========== \n{show_interfaces}")
    #print(f"f\n =========== running configuration ============= \n{running_config}")
    #print(f"\n ========== CDP_Neighbors ========== \n{cdp_neighbors}")
   #print(f"\n ========== OSPF_Neighbors ========== \n{ospf_neighbors}")
    
    print("=" * 85)

  #  if hostname.startswith("R"):
     #   connection.send_command("show ip route")
      #  print(f"\n ========== Routing_Table ========== \n{routing_table}")
   


