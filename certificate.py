# coding:utf-8
# use Bouncy Castle certificate generator both needs CertMaker.dll and BCMakeCert.dll 
# 
import json
def prepareCert(FC):
    try: 
        with open('certGenerator.json', 'r') as f:
            certificate = json.load(f)
            if certificate:
                FC.FiddlerApplication.Prefs.SetStringPref("fiddler.certmaker.bc.key", certificate['key'])
                FC.FiddlerApplication.Prefs.SetStringPref("fiddler.certmaker.bc.cert", certificate['cert'])
    except IOError as err:
        print("\n!! File Error:"+str(err))
    
    # when json file above load and call SetStringPref() method
    # FC.CertMaker.rootCertExists() will be True
    if not FC.CertMaker.rootCertExists():   
        FC.CertMaker.createRootCert()
        FC.CertMaker.trustRootCert() 
        
        cert = FC.FiddlerApplication.Prefs.GetStringPref("fiddler.certmaker.bc.cert", None)
        key = FC.FiddlerApplication.Prefs.GetStringPref("fiddler.certmaker.bc.key", None)
        certificate = {'key':key,'cert':cert}
        with open('certGenerator.json', 'w') as f:
            json.dump(certificate, f)
                   
    else:
        print "\n!! Root Certificate Exists **"