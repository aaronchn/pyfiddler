# coding:utf-8

import clr
import sys
import win32api
import win32con
import datetime
from certificate import *

sys.path.append("C:\\api")
clr.FindAssembly("FiddlerCore4")
clr.AddReference("FiddlerCore4")
import Fiddler as FC

# do some thing when Ctrl-c or colse
def onClose(sig):
    print chr(7)
    FC.FiddlerApplication.Shutdown()
    win32api.MessageBox(win32con.NULL, 'See you later', 'Exit', win32con.MB_OK)
    

# will be invoked when it is called by delegate.
def printLog(source,oLEA):
    print "\n** LogString: **\n" + oLEA.LogString

def printSession(s):
    
    if s is None or s.oRequest is None or s.oRequest.headers is None:
        return

    # Ignore HTTPS connect requests 
    if s.RequestMethod == "CONNECT":
        return
        
    # Filter for host
    host_obmit = "123.123.123.123"
    host = s.hostname.lower()
    if host_obmit not in host:
        return
    
    # Filter for path
    url = s.url.lower()
    if '/path' not in url:
        return
    
    datetime_now = datetime.datetime.now().strftime('%a, %Y %b %d %H:%M:%S')
    datetime_now_utc = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')    
    
    reqHeaders = s.oRequest.headers.ToString()
    reqBody = s.GetRequestBodyAsString()
    respCode = s.responseCode
    respHeaders = s.oResponse.headers.ToString()
    
    print '--->' 
    print datetime_now
    print reqHeaders
    
    # deal with cookie
    if s.oRequest.headers.Exists("cookie"):
        cookie = s.oRequest.headers.AllValues("cookie")
        print "Request cookie are:",cookie

    #if reqBody: print "!! Request body:\n",reqBody 
    print '<---'
    print respCode

def fiddler(FC,flags):   
    # register event handler
    # object.SomeEvent += handler
    #
    # unregister event handler
    # object.SomeEvent -= handler
    #
    # passed a callable Python object to get a delegate instance.
    FC.FiddlerApplication.Log.OnLogString += printLog
    FC.FiddlerApplication.AfterSessionComplete += printSession
    
    # When decrypting HTTPS traffic,ignore the server certificate errors  
    FC.CONFIG.IgnoreServerCertErrors = False
     
    # start up capture
    FC.FiddlerApplication.Startup(8888, flags)


if __name__ == '__main__':
   
    win32api.SetConsoleCtrlHandler(onClose, 1)
    captureType = "http"
    
    #RegisterAsSystemProxy:1
    #OptimizeThreadPool:512
    #MonitorAllConnections:32
    #DecryptSSL:2
    #AllowRemoteClients:8
    
    if captureType == "https":
        prepareCert(FC)      
        fiddler(FC, 1+512+32+2)
    else:
        fiddler(FC, 1+512+32)    
    try:
        # keep console window be open        
        raw_input()
    except:
        pass
