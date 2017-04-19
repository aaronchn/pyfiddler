# pyfiddler
Use Python to call FiddlerCore and capture Both HTTP and HTTPS.

Auto supply the certificate when capture HTTPS . Use Bouncy Castle certificate generator to generates a root certificate and asks to trust it, then generates end-entity certificates on-the-fly for each domain visited with the root certificate as the signer.

UsesCase：
Put FiddlerCore4 in any path and append it to Python sys.path
Put CertMaker.dll and BCMakeCert.dll to Python bin path like C:\python27 

Dependence：
pythonnet
pypiwin32

Test environment：
Python version:2.7.13
Pythonnet version:2.3.0
FiddlerCore 4.6.20171.13571

Thanks:
http://www.telerik.com/blogs/understanding-fiddler-certificate-generators
https://weblog.west-wind.com/posts/2014/jul/29/using-fiddlercore-to-capture-http-requests-with-net#CertificateInstallationwithFiddlerCore