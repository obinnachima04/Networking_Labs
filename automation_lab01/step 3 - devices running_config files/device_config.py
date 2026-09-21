from netmiko import ConnectHandler

# List of devices
devices = [
    {
        "name": "R1",
        "config_file": "R1_config.txt",
        "login": {
            "host": "192.168.122.2",  # Replace with R1's management IP
            "device_type": "cisco_ios",
            "username": "obinna",
            "password": "cisco",
        },
    },

    {
        "name": "R2",
        "config_file": "R2_config.txt",
        "login": {
            "host": "192.168.122.3",  # Replace with R2's management IP
            "device_type": "cisco_ios",
            "username": "obinna",
            "password": "cisco",
        },
    },

    {
        "name": "R3",
        "config_file": "R3_config.txt",
        "login": {
            "host": "192.168.122.4",  #R3's management IP
            "device_type": "cisco_ios",
            "username": "obinna",
            "password": "cisco",
        },
    },

    {
        "name" : "SERVER",
        "config_file" : "SERVER_config.txt",
        "login" : {
            "host" : "192.168.122.8", #Server's management IP
            "device_type": "cisco_ios",
            "username" : "obinna",
            "password" : "cisco",
        },
    },

    {
        "name" : "SW2",
            "config_file" : "SW2_config.txt",
            "login" : {
                "host" : "192.168.122.6", #SW2's management IP
                "device_type": "cisco_ios",
                "username" : "obinna",
                "password" : "cisco",
        },
    },

    {
         "name" : "SW3",
            "config_file" : "SW3_config.txt",
            "login" : {
                "host" : "192.168.122.7", #SW3's management IP
                "device_type": "cisco_ios",
                "username" : "obinna",
                "password" : "cisco",
        },
    }
]

# Loop through each device one by one
for device in devices:
    print(f"\nConnecting to {device['name']} @{device['login']['host']} >>>>>>>>>>>>>>")
    print(f"\nSuccessfully connected to {device['name']}\n")

    try:
        # Open and read the routing commands from the text file
        with open(device["config_file"], "r") as file:
            config_commands = file.read().splitlines()

        # Connect to the device using Netmiko
        net_connect = ConnectHandler(**device["login"])

        #send devices configurations
        print(f"\nSending {device['name']}'s configurations from {device['config_file']}...\n")

        running_config = net_connect.send_config_set(config_commands)

        print(running_config)

        #save running configs to startup config
        print(f"\nSaving running configuration to startup configuration on {device['name']}.........\n")

        save_config = net_connect.send_command_timing(
            "write memory",
            read_timeout=120
            )

        print(save_config)

        # verify startup-configuration
        startup_config = net_connect.send_command_timing("show startup-config | section router ospf", read_timeout=120)

        print("\nSTARTUP CONFIGURATION:")
        print(startup_config)
        

        print(f"Successfully saved configuration on {device['name']}")

        # Close the connection cleanly
        net_connect.disconnect()
        print(f"\nFinished configuring {device['name']}\n" + "=" * 85 + "\n\n")

    except FileNotFoundError:
        print(f"ERROR: File '{device['config_file']}' was not found!\n" + "=" * 85)
    except Exception as e:
        print(f"ERROR: Could not configure {device['name']}. Reason: {e}\n" + "=" * 85)


