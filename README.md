# port_scanner
A script that scans ports 20 - 1023 of a specific IP address entered by the user


It starts by creating a new socket object, openSocket
Next it has a timeout of 0.2 seconds, however since im testing using my loopback address its not really necessary to have a timeout but if I test an address that isnt my loopback the timeout would be necessary because the scanner needs time to test the port or it could result in a false negative as an open port might be skipped if it goes too quick
openSocke returns a value based on whether a port is open or closed and that value is assigned to result. The connect_ex method is useful here because it returns a value of either 0 meaning true or any value other than 0 meaning false, if the result is 0 then the port is open and the script prints out the open port number, if a port is closed it just ignores it and keeps going until there is another open port. 
when the scan is complete, the socket is closed and the connection ends
Pressing ctrl + c ends the script early 
