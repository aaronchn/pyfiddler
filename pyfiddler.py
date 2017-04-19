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
        
    #captureDomain = ("google","github")
    #for i in captureDomain:
        #if i  not in s.hostname.lower():
            #return
    
    url = s.fullUrl.lower() 
    reqHeaders = s.oRequest.headers.ToString()
    reqBody = s.GetRequestBodyAsString()
    respHeaders = s.oResponse.headers.ToString()

    #"image/","text/css","text/javascript","application/x-javascript","application/json"
    mime = ("image/","text/css")      
    for i in mime:
        if i in respHeaders :
            print "Hide this ignore resource"
            return

    #if "Coolie" in reqHeaders:
    #    cookie = s.oRequest.headers["Cookie"]
    #    
       
    print '======>>' 
    print "Traffic time:" + utcTime + '\n'
    
    print reqHeaders
    if reqBody: print "Request body:" + reqBody 
    
    print '<-------'
    print respHeaders

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
    utcTime = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    
    captureType = "https"
    
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
        # keep console window opening        
        raw_input()
    except:
        pass