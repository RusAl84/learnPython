import subprocess
import os
import sys
import time
import signal

from multiprocessing import Pool, Process
import time

import socket
from urllib.parse import urlparse

###########################################SUBPROCESS###################################################################
def shell_less():
    try:
        completed = subprocess.run(['ls','-alt'], stdout=subprocess.PIPE)
        print(completed.stdout.decode('utf-8')) #возвращают байтовый поток, нам надо строки.
    except subprocess.CalledProcessError as err:
        print("ERROR:", err)

def shell_and_suppres_err():
    try:
        completed = subprocess.run(
            'echo to stdout; echo to stderr 1>&2; exit 1',
            check=True,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, #try subporcess.DEVNULL to suppress output
        )
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        print('returncode:', completed.returncode)
        print('Have {} bytes in stdout: {!r}'.format(
            len(completed.stdout),
            completed.stdout.decode('utf-8'))
        )

def manual_piping():
    print('we pass msg to shell, and capture output:')

    proc = subprocess.Popen(
        ['cat', '-'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    msg = 'through stdin to stdout'.encode('utf-8')
    stdout_value = proc.communicate(msg)[0].decode('utf-8')
    print('pass through:', repr(stdout_value))

def connecting_commands():
    print('Manual chain...:')

    cat = subprocess.Popen(
        ['cat', 'practice_6.py'],
        stdout=subprocess.PIPE,
    )

    grep = subprocess.Popen(
        ['grep', '.. reader'],
        stdin=cat.stdout,
        stdout=subprocess.PIPE,
    )

    end_of_pipe = grep.stdout

    print('Included files:')
    for line in end_of_pipe:
        print(line.decode('utf-8').strip())

received = False

def signal_usr(signum, frame):
    "Callback invoked when a signal is received"
    global received
    received = True
    print('CHILD {:>6}: Received USR1'.format(pid))
    sys.stdout.flush()

def communicate(pid):
    print('CHILD {:>6}: Setting up signal handler'.format(pid))
    sys.stdout.flush()
    signal.signal(signal.SIGUSR1, signal_usr)
    print('CHILD {:>6}: Pausing to wait for signal'.format(pid))
    sys.stdout.flush()
    time.sleep(3)

    if not received:
        print('CHILD {:>6}: Never received signal'.format(pid))

###########################################MULTIPROCESSING######################################################
def countdown(n):
    while n > 0:
        n -= 1

def fn1(x):
    return x*x

def sleep_secs(amount):
    time.sleep(amount)

def pool_context(amount=3):
    t1 = time.time()
    with Pool(3) as p:
        print(p.map(fn1, [1, 2, 3]))
        p.apply_async(countdown, (100000000,))
        p.apply_async(sleep_secs, (2,))
    t2 = time.time()
    print(t2 - t1)
##################################################SOCKET###############################################################
def get_port_by_server_name(urls = None):
    if not urls:
        urls = [
            'http://www.python.org',
            'https://www.mybank.com',
            'ftp://prep.ai.mit.edu',
            'gopher://gopher.micro.umn.edu',
            'smtp://mail.example.com',
            'imap://mail.example.com',
            'imaps://mail.example.com',
            'pop3://pop.example.com',
            'pop3s://pop.example.com',
        ]

    for url in urls:
        parsed_url = urlparse(url)
        port = socket.getservbyname(parsed_url.scheme)
        print('{:>6} : {}'.format(parsed_url.scheme, port))

def look_up_ports(look_up_table = None):
    if not look_up_table:
        look_up_table = [80, 443, 21, 70, 25, 143, 993, 110, 995]
    for port in [80, 443, 21, 70, 25, 143, 993, 110, 995]:
        url = '{}://example.com/'.format(socket.getservbyport(port))
        print(url)
def echo_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 10000)
    message = b'This is the message.  It will be repeated.'

    try:

        # Send data
        print('sending {!r}'.format(message))
        sent = sock.sendto(message, server_address)

        # Receive response
        print('waiting to receive')
        data, server = sock.recvfrom(4096)
        print('received {!r}'.format(data))

    finally:
        print('closing socket')
        sock.close()

if __name__ == "__main__":
    #########################################SUBPROCESS################################################################
    # https://learn.microsoft.com/ru-ru/windows/wsl/basic-commands#set-default-linux-distribution
    # shell_less()
    # shell_and_suppres_err()
    # manual_piping()
    # connecting_commands()
    # pid = os.getpid()
    # communicate(pid)

    # pool_context()

    ############################################SOCKET##################################################################
    # get_port_by_server_name()
    # look_up_ports()
    echo_client()
