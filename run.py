
import random
import requests
import time
import urllib.parse
import json
import base64
import socket
from datetime import datetime


def load_credentials():
    # Membaca token dari file dan mengembalikan daftar token
    try:
        with open('query_id.txt', 'r') as f:
            queries = [line.strip() for line in f.readlines()]
        # print("Token berhasil dimuat.")
        return queries
    except FileNotFoundError:
        print("File query_id.txt tidak ditemukan.")
        return [  ]
    except Exception as e:
        print("Terjadi kesalahan saat memuat token:", str(e))
        return [  ]

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
    'content-length': '0',
    'priority': 'u=1, i',
    'Origin': 'https://mmbump.pro',
    'Referer': 'https://mmbump.pro/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    
}

def getuseragent(index):
    try:
        with open('useragent.txt', 'r') as f:
            useragent = [line.strip() for line in f.readlines()]
        if index < len(useragent):
            return useragent[index]
        else:
            return "Index out of range"
    except FileNotFoundError:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
    except Exception as e:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'

    

def login(query):
    url = "https://api.mmbump.pro/v1/login"
    payload = {
          'initData': query
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def task_list(token):
    url = "https://api.mmbump.pro/v1/task-list"
    headers['Authorization'] = token
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def complete(token, id):
    url = 'https://api.mmbump.pro/v1/task-list/complete'
    headers['Authorization'] = token
    data = {
        'id': id
    }
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def claim(token):
    url = 'https://api.mmbump.pro/v1/task-list/claim'
    headers['Authorization'] = token
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def refclaim(token, useragent):
    url = 'https://api.mmbump.pro/v1/friends/claim'
    headers['Authorization'] = token
    headers['user-agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def start(token, useragent):
    url = 'https://api.mmbump.pro/v1/farming/start'
    headers['Authorization'] = token
    headers['X-Requested-With'] = 'org.telegram.messenger'
    headers['user-agent'] = useragent
    data = {'status': "inProgress"}

    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return []
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def finish(token, useragent, tapcount):
    url = 'https://api.mmbump.pro/v1/farming/finish'
    headers['Authorization'] = token
    headers['X-Requested-With'] = 'org.telegram.messenger'
    headers['user-agent'] = useragent
    data = {'tapCount': tapcount}

    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return []
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def buyx5(token):
    url = 'https://api.mmbump.pro/v1/product-list/buy'
    headers['Authorization'] = token
    data = {'id': "x5"}

    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def checkin(token):
    url = 'https://api.mmbump.pro/v1/grant-day/claim'

    headers['Authorization'] = token
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.json())
            return []
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def dailyclaim():

    while True:
        reffstatus = input("Claim ref ? (default n) (y/n): ").strip().lower()
        if reffstatus in ['y', 'n', '']:
            reffstatus = reffstatus or 'n'
            break
        else:
            print("Input 'y' atau 'n'.")

    while True:
        queries = load_credentials()
        for index, query in enumerate(queries):
            data_login = login(query)
            useragent = getuseragent(index)
            if data_login is not None:
                print(f'============== Account : {index+1} =============')
                token = data_login.get('token')
                taps = random.randint(200, 800)
                data_finish = finish(token, useragent, taps)
                while True:
                    if data_finish is not None:
                        if data_finish != []:
                            if data_finish.get('code') != 403:
                                session = data_finish.get('session')
                                print("Claimmed....")
                                time.sleep(2)
                                print(f"ID : {session.get('user_telegram_id')} | total balance : {data_finish.get('balance')}")
                                print(f"Total Taps : {session.get('taps')}")
                            else:
                                print("claim balance not found")
                        time.sleep(5)
                        data_claim = start(token, useragent)
                        while True:
                            if data_claim is not None:
                                if data_claim != []:
                                    if data_claim.get('code') == None:
                                        print(f"Farming Status : {data_claim.get('status')}")
                                    else:
                                        print("Farming status still running")
                                time.sleep(5)
                                break
                            else:
                                print("Failed Start Farming")
                                time.sleep(1)
                                print("Repeat Get Data")
                                time.sleep(2)
                                data_claim = start(token, useragent)
                        break
                    else:
                        print('Failed Claim Farming')
                        time.sleep(1)
                        print("Repeat Get Data")
                        time.sleep(2)
                        data_finish = finish(token, useragent, taps)
                
                if reffstatus == 'y':
                    while True:
                        data_refclaim = refclaim(token, useragent)
                        if data_refclaim is not None:
                            print(f"Claim ref : {data_refclaim.get('sum')} | Total Balance : {data_refclaim.get('balance')}")
                            time.sleep(5)
                            break
                        else:
                            print("Failed Claim Ref")
                            time.sleep(1)
                            print("Repeat Get Data")
                            time.sleep(2)
                            data_refclaim = refclaim(token, useragent)
                        
                print('=========================================')
                print()
                time.sleep(5)
            
        delay = random.randint(21600, 22000)
        printdelay(delay)
        time.sleep(delay)

def taskmain():
    queries = load_credentials()
    for index, query in enumerate(queries):
        data_login = login(query)
        if data_login is not None:
            token = data_login.get('token')
            task_list_data = task_list(token)
            if task_list_data is not None:
                print(f'============== Account : {index+1} =============')
                for data in task_list_data:
                    id = data.get('id')
                    data_complete = complete(token, id)
                    if data_complete is None:
                        print('Task Done')
                    else:
                        task = data_complete.get('task')
                        print(f"task : {task['name']} | status : {task['status']} | reward : {task['grant']}")
                    time.sleep(3)
                data_claim = claim(token)
                if data_claim is not None:
                    print('=================================================')
                    print(f"total reward : {data_claim['balance']}")
                    print()

def checkinmain():
    queries = load_credentials()
    for index, query in enumerate(queries):
        data_login = login(query)
        if data_login is not None:
            token = data_login.get('token')
            while True:
                data_checkin = checkin(token)
                if data_checkin is None:
                    time.sleep(3)
                    data_checkin = checkin(token)
                    print("Repeat")
                    print(data_checkin)
                else:
                    print(data_checkin)
                    break
            time.sleep(3)


#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################

def main():
    print(r"""
        
            Created By Snail S4NS Group
    find new airdrop & bot here: t.me/sanscryptox
              
        select this one :
        1. claim daily (6 hours)
        2. checkin daily
        3. complete task/quest
          
          """)

    selector = input("Select the one ? (default 1): ").strip().lower()

    if selector == '1':
        dailyclaim()
    elif selector == '2':
        checkinmain()
    elif selector == '3':
        taskmain()
    else:
        exit()

def printdelay(delay):
    now = datetime.now().isoformat(" ").split(".")[0]
    hours, remainder = divmod(delay, 3600)
    minutes, sec = divmod(remainder, 60)
    print(f"{now} | Waiting Time: {hours} hours, {minutes} minutes, and {sec} seconds")


def print_welcome_message(serial=None):
    print(r"""
              
            Created By Snail S4NS Group
    find new airdrop & bot here: t.me/sansxgroup
              
          """)
    print()
    if serial is not None:
        print(f"Copy, tag bot @SnailHelperBot and paste this key in discussion group t.me/sansxgroup")
        print(f"Your key : {serial}")

def read_serial_from_file(filename):
    serial_list = []
    with open(filename, 'r') as file:
        for line in file:
            serial_list.append(line.strip())
    return serial_list

serial_file = "serial.txt"
serial_list = read_serial_from_file(serial_file)


def get_serial(current_date, getpcname, name, status):
    formatted_current_date = current_date.strftime("%d-%m-%Y")
    # Encode each value using base64
    getpcname += "knjt"
    name    += "knjt"
    encoded_getpcname = base64.b64encode(getpcname.encode()).decode().replace("=", "")
    encoded_current_date = base64.b64encode(formatted_current_date.encode()).decode().replace("=", "")
    encoded_name = base64.b64encode(name.encode()).decode().replace("=", "")
    encoded_status = base64.b64encode(str(status).encode()).decode().replace("=", "")

    # Calculate the length of each encoded value
    getpcname_len = len(encoded_getpcname)
    current_date_len = len(encoded_current_date)
    name_len = len(encoded_name)
    status_len = len(encoded_status)

    # Concatenate the encoded values with their lengths
    serial = "S4NS-"
    serial += str(getpcname_len).zfill(2) + encoded_getpcname
    serial += str(current_date_len).zfill(2) + encoded_current_date
    serial += str(name_len).zfill(2) + encoded_name
    serial += str(status_len).zfill(2) + encoded_status
    return serial

def decode_pc(serial, getpcname, name, current_date):
    try:
        getpcname_len = int(serial[5:7])
        encoded_getpcname = serial[7:7+getpcname_len]
        current_date_len = int(serial[7+getpcname_len:9+getpcname_len])
        encoded_current_date = serial[9+getpcname_len:9+getpcname_len+current_date_len]
        name_len = int(serial[9+getpcname_len+current_date_len:11+getpcname_len+current_date_len])
        encoded_name = serial[11+getpcname_len+current_date_len:11+getpcname_len+current_date_len+name_len]
        status_len = int(serial[11+getpcname_len+current_date_len+name_len:13+getpcname_len+current_date_len+name_len])
        encoded_status = serial[13+getpcname_len+current_date_len+name_len:13+getpcname_len+current_date_len+name_len+status_len]

        # Decode each value using base64
        decoded_getpcname = base64.b64decode(encoded_getpcname + "==").decode()
        decoded_current_date = base64.b64decode(encoded_current_date + "==").decode()
        decoded_name = base64.b64decode(encoded_name + "==").decode()
        decoded_status = base64.b64decode(encoded_status + "==").decode()
        
        dates = compare_dates(decoded_current_date)

        if decoded_status != '1':
            print("Key Not Generated")
            return None
            
        elif decoded_getpcname.replace("knjt", "") != getpcname:
            print("Different devices registered")
            return None
        
        elif decoded_name.replace("knjt", "") != name:
            print("Different bot registered")
            return None
        
        elif dates < 0:
            print("Key Expired")
            return None
        else:
            print(f"            Key alive until : {decoded_current_date} ")
            return dates
    except Exception as e:
        print(f'Key Error : {e}')

def compare_dates(date_str):
    tanggal_compare_dt = datetime.strptime(date_str, '%d-%m-%Y')
    tanggal_now = datetime.now()
    perbedaan_hari = (tanggal_compare_dt - tanggal_now).days
    return perbedaan_hari

def started():
    getpcname = socket.gethostname()
    name = "MMPRO BUMP"
    current_date = datetime.now() # Get the current date
    status = '0'

    if len(serial_list) == 0:
        serial = get_serial(current_date, getpcname, name, status)
        print_welcome_message(serial)
    else:
        serial = serial_list[0]
        if serial == 'S4NS-XXWEWANTBYPASSXX':
            main()
        else:
            decodeds = decode_pc(serial, getpcname, name, current_date)
            if decodeds is not None:
                    print_welcome_message()
                    time.sleep(10)
                    main()         
            else:
                serial = get_serial(current_date, getpcname, name, status)
                print_welcome_message(serial)
                print("Please submit the key to bot for get new key")
            

if __name__ == "__main__":
    started()
