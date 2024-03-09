<!-- TOC -->
# WoL-Server

## Description
This is a small leightweight Python based WoL-Server that allows you to wake your Client with single press of a button.

## Setup
1. Clone the Repository
2. Create a venv in the project directory:
```bash 
python -m venv venv
```
3. Activate the venv:
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS and Linux
```bash
source venv/bin/activate
```
4. Install dependencies
```bash
pip install -r requirements.txt 
```
5. Run the application
```bash
python app.py
```
This will start the application. You can then access it in your web browser at `http://localhost:5000`.
You can reach the website by using the Devices-IP aswell.

6. Add Icons

Since i dont want to mess with any license stuff, you have to add your own icons. The need the following naming scheme:
- Laptop_icon.png
- Pc_icon.png
- Pi_icon.png

To add these Icons we save them in the templates Folder, where the index.html can also be found.

## User Guide
With the application started, we first have to add an device.
![image](https://github.com/HitoHitoNika/WoL-Server/assets/103290810/4af9008c-edcf-4d15-8d09-cf9799477aae)
There are two things we have to care about:
- We have to enter the devices mac adress
- We DONT enter the - or : between each part of the MAC
- Example: DONT 01:23:45:67:89:FF instead do 0123456789FF

You can also choose between device type:
- PC
- Laptop
- Raspberry Pi
This will change the icon that will be shown on the website!
After we have added our device it should look like this:
![image](https://github.com/HitoHitoNika/WoL-Server/assets/103290810/47567188-8443-48d4-8ab4-8ca98d6e1450)
