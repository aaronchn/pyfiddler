# pyfiddler
Using  Python to call FiddlerCore and capture both HTTP and HTTPS packets.

Auto supply the certificate when capture HTTPS . Use Bouncy Castle certificate generator to generates a root certificate and asks to trust it, then generates end-entity certificates on-the-fly for each domain visited with the root certificate as the signer.

- UsesCase：</br>
Put FiddlerCore4.dll in any path and append it to Python sys.path to reference it </br>
Put CertMaker.dll and BCMakeCert.dll to Python bin directory like C:\python27 </br>

- Dependence：</br>
pythonnet</br>
pypiwin32</br>

- Test environment：</br>
Python version: 2.7.13</br>
Pythonnet version: 2.3.0</br>
FiddlerCore 4.6.20171.13571</br>
Win7 32bit and xp sp3 with .net 4 </br>

- Thanks:</br>
http://www.telerik.com/blogs/understanding-fiddler-certificate-generators </br>
https://weblog.west-wind.com/posts/2014/jul/29/using-fiddlercore-to-capture-http-requests-with-net#CertificateInstallationwithFiddlerCore
