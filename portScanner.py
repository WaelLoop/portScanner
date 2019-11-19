import sys
import nmap
import datetime

# function that does the port scan using nmap library
def portScanning(ip):
    try:
	#create our output file
        file = open(str(datetime.datetime.now()), 'a+')
	#initialize our nmap scanner object
        nm = nmap.PortScanner()
	#nmap -oX - -p 22-443 ip
        nm.scan(ip,'22-443')
	# appending hostname and if it's status
        file.write("="*50 + '\n')
        file.write('Host: %s\n' % ip)
        file.write('Hostname: %s\n' % nm[ip].hostname())
        file.write('State: %s\n' % nm[ip].state())

	# append protocols and ports
        for protocol in nm[ip].all_protocols():
            file.write('=' * 15 + '\n')
            file.write('Protocol: %s\n' % protocol)

            listOfPorts = nm[ip][protocol].keys()

            for port in listOfPorts:
                file.write('Port: %s  State: %s\n' % (port, nm[ip][protocol][port]['state']))
    except Exception as e:
	# error handling
        print("Couldnt Scan" + ip + ": " + e)

# method to read the file of hosts to scan
def readHostsFromFile():
    hosts= open(sys.argv[1], 'r')
    for host in hosts.readlines():
        portScanning(host.strip())


if __name__ == '__main__':
	if(len(sys.argv) == 2):
		readHostsFromFile()
	else:
		print("invalid input. Pass in hosts.txt")
