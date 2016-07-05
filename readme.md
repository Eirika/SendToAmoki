Send To Amoki
===========
Install
-------
* Windows :
	* Clone this repo
	* Go to : `%appdata%\Roaming\Microsoft\Windows\SendTo`
	* Create a shortcut to pointing to `python "path_to_sendToAmoki.py"` with quotes!


* Linux :
    * You need to have python3
	```sh
	git clone https://github.com/Eirika/sendToAmoki.git 
	cd sendToAmoki
	ln -s `pwd`/sendToAmoki.py /usr/local/bin/sendToAmoki
	```


* In all cases :
    * If you want to use the auto credential system, create a file exactly named `credentials.py` containing :
		
		```python
		conf_host = "URL / IP TO YOUR FTP HOST"
		conf_user = "YOUR USERNAME"
		conf_password = "YOUR PASSWORD"
        ``` 
        This file need to be located in the same directory of the script `sendToAmoki.py`

How to use
----------
* Windows :
	* Just right-click the file(s) or folder(s) you want to upload and wait until the script prints `FIN !`


* Linux :
	```sh
	sendToAmoki file|directory [file|directory...]
	```
	If you want a similar behavior than Windows, google it depending your file browser


---
>> By Eirika and Amoki
 
