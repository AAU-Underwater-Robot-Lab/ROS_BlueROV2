[Go back](../README.md)

# <b>Setup wireless internet sharing through ethernet</b>
A guide on how to share your wireless internet connection from your Desktop to your Jetson board through ethernet.

## <b>On your Ubuntu Desktop</b>
Follows these steps:

* Open nm-connection-editor from the terminal

  `nm-connection-editor`
* Click on the wired connection and select edit cog wheel below
* Go to the ipv4 settings tab there in the Method select `Shared to Other Computers`
* Add a new address under <b>Address (optional)</b>:
    Adress: 192.168.2.60
    Netmask: 24
    Gateway: Leave blank

**The Address can be changed, however the it always be 192.168.2.\* and not end with 10, 20, 94 or 100, as these are already used by other systems. Beside that the Gateway on the Jetson must be changed to match this address!**

* Press `Save`

**Note: If the changed are not applied run `sudo systemctl restart networking` in the terminal to restart the network.**

## <b>On your Jetson Board</b>
* Go to network settings
* Click on the wired connection and select edit cog wheel
* Go to the ipv4 settings tab there in the Method select `Manual`
* Add a new address under <b>Address (optional)</b>:
    Adress: 192.168.2.10
    Netmask: 24
    Gateway: 192.168.2.60 
    
**Gateway should be the same as the address used for your desktop**

* Press `Save`

**Note: If the changed are not applied run `sudo systemctl restart networking` in the terminal to restart the network.**
