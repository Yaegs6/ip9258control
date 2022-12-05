
import getpass
import sys
import telnetlib
import urllib2
import time 

connection = None 

class Ip9258:
    def __init__(self, hostname, username, password):
        self._hostname = hostname

        # create a password manager
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, 'http://' + hostname, username, password)
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)

        # Now all calls to urllib2.urlopen use our opener.
        urllib2.install_opener(opener)

    def on(self, port):
        '''
        This turns on the power of the port number provided. 
        If a connection is not achieved after 10 attempts, it
        exits the script.

        ''' 
        for attempt in range(0, 10):
            try:
                connection = urllib2.urlopen('http://' + self._hostname + '/set.cmd?cmd=setpower+p6' + str(port) + '=1')
                connection.close()
                str_error = None                
            except Exception as e:
                print("Failed to connect to power supply. Retrying connection...")
                str_error = e
                pass
            if str_error:
                time.sleep(2)
            else:
                break
        else:
            "Failed to connect to power supply 10 times. test exit"
            sys.exit(0) 
                      
    def off(self, port):
        '''
        This turns off the power of the port number provided.
        If a connection is not achieved after 10 attempts, it 
        exits the script.

        '''
        for attempt in range(0, 10):
            try:
                connection = urllib2.urlopen('http://' + self._hostname + '/set.cmd?cmd=setpower+p6' + str(port) + '=0')
                connection.close()
                str_error = None                
            except Exception as e:
                print("Failed to connect to power supply. Retrying connection...")
                str_error = e
                pass
            if str_error:
                time.sleep(2)
            else:
                break                
        else:
            "Failed to connect to power supply 10 times. test exit"
            sys.exit(0) 


