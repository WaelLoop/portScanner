import sys
import nmap
import datetime


def portScanning(ip):
    file = open(str(datetime.datetime.now()), 'w+')
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


def readHostsFromFile():
    hosts= open(sys.argv[1], 'w')
    for host in hosts.readline():
        portScanning(host)


if __name__ == '__main__':
    readHostsFromFile()
