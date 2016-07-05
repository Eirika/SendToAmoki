# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# from __future__ import division
import sys
import ftplib
import os

try:
    from credentials import conf_host, conf_user, conf_password
    host = conf_host
    user = conf_user
    password = conf_password
except Exception:
    print('No cendentials file found')
    host = input('Hostname : ')
    user = input('Username : ')
    password = input('Password : ')

if not sys.argv[1:]:
    print("No file to upload !")
    sys.exit(1)


ftp = ftplib.FTP(host, user, password)  # on se connecte
files_to_upload = sys.argv[1:]
answer = 'nope'


def upload_directory(path):
    global answer
    files = os.listdir(path)
    os.chdir(path)
    for file in files:
        if os.path.isfile(path + '\{}'.format(file)):
            upload_file(file)

        elif os.path.isdir(path + '\{}'.format(file)):
            if file not in [name for name, data in list(ftp.mlsd())]:
                ftp.mkd(file)
            print('Created directory : {}'.format(os.path.basename(file)))
            ftp.cwd(file)
            upload_directory(path + '\{}'.format(file))
    ftp.cwd('..')
    os.chdir('..')


def upload_file(path):
    global answer
    if answer == 'a':
        do_upload = True
    elif os.path.basename(path) in [name for name, data in list(ftp.mlsd())]:
        answer = 'nope'
        while answer.lower() not in ['y', 'n', 'a']:
            answer = input('This file already exist, override it ? [Y (yes) / N (no) / A (all occurences)] : ')
        if answer.lower() == 'n':
            print('File NOT upload because of conflict : {}'.format(os.path.basename(path)))
        else:
            do_upload = True
    else:
        do_upload = True

    if do_upload or answer == 'all':
        fh = open(path, 'rb')
        ftp.storbinary('STOR ' + os.path.basename(path), fh)
        print('Uploaded {}'.format(os.path.basename(path)))
        fh.close()

# # Send to ftp
for element in files_to_upload:
    if os.path.isdir(element):
        if os.path.basename(element) not in [name for name, data in list(ftp.mlsd())]:
            ftp.mkd(os.path.basename(element))
        print('Created main directory : {}'.format(os.path.basename(element)))
        ftp.cwd(os.path.basename(element))
        upload_directory(element)  # now call the recursive function
    elif os.path.isfile(element):
        upload_file(element)
ftp.quit()


print("""\n
 ______  _____  _   _    _
|  ____||_   _|| \ | |  | |
| |__     | |  |  \| |  | |
|  __|    | |  | . ` |  | |
| |      _| |_ | |\  |  |_|
|_|     |_____||_| \_|  (_)\n
""")

input("Press Enter to continue...")
