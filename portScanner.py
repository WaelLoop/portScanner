import sys
import nmap
import datetime


def portScanning(ip):
    try:
        file = open(str(datetime.datetime.now()), 'a+')
        nm = nmap.PortScanner()
        nm.scan(ip,'22-443')

        file.write("="*50 + '\n')
        file.write('Host: %s\n' % ip)
        file.write('Hostname: %s\n' % nm[ip].hostname())
        file.write('State: %s\n' % nm[ip].state())

        for protocol in nm[ip].all_protocols():
            file.write('=' * 15 + '\n')
            file.write('Protocol: %s\n' % protocol)

            listOfPorts = nm[ip][protocol].keys()

            for port in listOfPorts:
                file.write('Port: %s  State: %s\n' % (port, nm[ip][protocol][port]['state']))
    except Exception as e:
        print("Couldnt Scan" + ip + ": " + e)


def readHostsFromFile():
    hosts= open(sys.argv[1], 'r')
    for host in hosts.readlines():
        portScanning(host.strip())


if __name__ == '__main__':
	if(len(sys.argv) == 2):
		readHostsFromFile()
	else:
		print("invalid input. Pass in hosts.txt")