from flask import Flask, render_template, request, redirect,send_file
import socket
import csv

app = Flask(__name__)

# Pfad zur CSV-Datei
CSV_FILE = 'devices.csv'


# Funktion zum Laden der Geräte aus der CSV-Datei
def load_devices():
    try:
        with open(CSV_FILE, 'r', newline='') as file:
            reader = csv.DictReader(file)
            devices = [row for row in reader]
    except FileNotFoundError:
        devices = []
        save_devices(devices)
    return devices


# Funktion zum Speichern der Geräte in die CSV-Datei
def save_devices(devices):
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'mac_address', 'type_id'])
        writer.writeheader()
        writer.writerows(devices)


# Funktion zum Senden von Magic Packets
def send_magic_packet(mac_address):
    mac_bytes = bytes.fromhex(mac_address.replace(':', ''))
    magic_packet = b'\xff' * 6 + mac_bytes * 16

    # Broadcast Magic Packet to local network
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(magic_packet, ('192.168.1.255', 9))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_device = {
            "name": request.form['name'],
            "mac_address": request.form['mac_address'],
            "type_id": int(request.form['type_id'])
        }
        devices = load_devices()  # Lade Geräte, um neue hinzuzufügen
        devices.append(new_device)
        save_devices(devices)  # Speichere die aktualisierte Geräteliste
    devices = load_devices()  # Lade Geräte für Anzeige
    return render_template('index.html', devices=devices)


@app.route('/wake_device', methods=['POST'])
def wake_device():
    mac_address = request.form['mac_address']
    send_magic_packet(mac_address)
    return 'Magic Packet sent successfully'


@app.route('/add_device', methods=['POST'])
def add_device():
    new_device = {
        "name": request.form['name'],
        "mac_address": request.form['mac_address'],
        "type_id": int(request.form['type_id'])
    }
    devices = load_devices()  # Lade Geräte, um neues hinzuzufügen
    devices.append(new_device)
    save_devices(devices)  # Speichere die aktualisierte Geräteliste
    return redirect('/')

@app.route('/Laptop_icon.png',methods=['GET'])
def getLaptopImage():
    return send_file('./templates/Laptop_icon.png', mimetype='image/png')

@app.route('/Pi_icon.png',methods=['GET'])
def getPiImage():
    return send_file('./templates/Pi_icon.png', mimetype='image/png')

@app.route('/Pc_icon.png',methods=['GET'])
def getPcImage():
    return send_file('./templates/Pc_icon.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
