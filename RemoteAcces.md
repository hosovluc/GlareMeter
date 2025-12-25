# Raspberry Pi – Initial Setup and Remote Access (SSH & VNC)

## Official Documentation
- Getting Started:  
  https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system
- Remote Access (SSH):  
  https://www.raspberrypi.com/documentation/computers/remote-access.html#ssh

---

## 1. Install the Operating System
1. On your PC, download and open **Raspberry Pi Imager**.
2. Insert the **SD card** into your PC.
3. Use Raspberry Pi Imager to:
   - Select the desired **Raspberry Pi OS**
   - Select the **SD card**
   - Write the OS to the SD card

---

## 2. First Boot and Network Setup
1. Insert the SD card into the Raspberry Pi.
2. Power on the Raspberry Pi.
3. Connect:
   - Monitor
   - Keyboard
   - Network (Ethernet or Wi-Fi)
4. Find the **IP address** of the Raspberry Pi.
5. Open **Raspberry Pi Configuration** and verify that **SSH is enabled**.

---

## 3. Enable VNC
1. Open **Raspberry Pi Configuration**.
2. Go to the **Interfaces** tab.
3. Enable **VNC**.
4. Apply changes and reboot if required.

---

## 4. Install and Start VNC Server
Based on the guide:  
https://www.itnetwork.cz/hardware-pc/raspberry-pi/raspberry-pi-pripojeni-pomoci-ssh-a-vnc

1. Connect to the Raspberry Pi via **SSH**.
2. Run the following commands in the terminal:

```bash
sudo apt-get update
sudo apt-get install tightvncserver
vncserver :1
