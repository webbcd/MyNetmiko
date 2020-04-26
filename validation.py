import subprocess, sys, socket
import threading
from multiprocessing import Queue
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler

# Define username and password to login to all routers with
USER = input('TACACS Username? ')
PASSWORD = getpass()

#define commands to run from text file 
commands = open('./commands.txt', 'r').read().split('\n')

# Define IPs, you could also make a dictionary imported from a CSV file, or create a list from a text file of hostnames
routers = open('./devices.txt', 'r').read().split('\n')

def ssh_session(routers, output_q):
    # Place what you want each thread to do here, for example connect to SSH, run a command, get output
    output_dict = {}
    hostname = router
    router = {'device_type': 'ruckus_fastiron', 'ip': router, 'username': USER, 'password': PASSWORD, 'verbose': False, }
    ssh_session = ConnectHandler(**router)
    output = ssh_session.send_command(commands)
    output_dict[hostname] = output
    output_q.put(output_dict)
    
    connection.save_config()
    connection.disconnect()

if __name__ == "__main__":

    output_q = Queue()
    
    # Start thread for each router in routers list
    for router in routers:
          my_thread = threading.Thread(target=ssh_session, args=(router, output_q,))
          my_thread.start()

    # Wait for all threads to complete
    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            some_thread.join()

    # Retrieve everything off the queue - k is the router IP, v is output
    # You could also write this to a file, or create a file for each router
    
    while not output_q.empty():
        my_dict = output_q.get()
        for k, val in my_dict.iteritems():
            print (k)
            print (val)