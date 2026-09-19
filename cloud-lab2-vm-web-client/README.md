# Hardware-Assisted Virtualization: VM Web Server + Client

A QEMU/KVM and libvirt lab demonstrating two communicating virtual
machines on a virtual NAT network.

## Architecture

vm-client
│
│ HTTP
▼
vm-server
│
└── Flask Calculator

## Environment

- QEMU/KVM
- libvirt
- Ubuntu Server 26.04.1
- Python 3
- Flask
- libvirt default NAT network

## VMs

### vm-server

- 1 vCPU
- 1536 MB RAM
- 10 GB disk
- Flask application
- IP: 192.168.122.143

### vm-client

- 1 vCPU
- 2048 MB RAM
- 15 GB disk
- Lightweight GUI
- Web browser

## Networking

Both VMs use libvirt's default virtual network.

The client communicates with the Flask server using:

`http://<server-ip>:5000/`

## Calculator

Supports:

- Addition
- Subtraction
- Multiplication
- Division

## Screenshots

### Both VMs running

![Both VMs running](screenshots/01_virsh_list_all.jpeg)

### Client VM

![Client VM](screenshots/02_vm_client.jpeg)

### Server VM

![Server VM](screenshots/03_vm_server.jpeg)

### VM Networking

![VM networking](screenshots/04_vm_client_server.jpeg)

### Client → Server Ping

![Client to server ping](screenshots/05_ping_vm_client_to_vm_server.jpeg)

### Calculator Result in Browser

![Calculator result](screenshots/06_calculator_result_in_browser.jpeg)
