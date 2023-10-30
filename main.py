import argparse,re,os

from Tools import subnet,interfaceScan,Logo

class Main:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description="")
        parser.add_argument('choice',choices=["spoof","backdoor","dos","scan","jam","build"])
        parser.add_argument('-t','--type',required=True,help="attack type")
        parser.add_argument('--lhost',help="Host Ip Address")
        parser.add_argument('--lport',type=int,help='Port Number')
        parser.add_argument('--range',help="subnet range")
        parser.add_argument('--interface',help="interface")
        parser.add_argument('--mac',help="mac address")
        parser.add_argument('--target',help="targget ip address")
        parser.add_argument('--targetmac',help="targget MAC address")
        self.args = parser.parse_args()

    def forward(self):
        os.system("cls")
        choice = self.args.choice
        type = (self.args.type).lower()
        lhost = self.args.lhost
        lport = self.args.lport
        subnet_range = self.args.range
        interface = self.args.interface
        newMac = self.args.mac
        target = self.args.target
        target_mac = self.args.targetmac
        Logo.Logo().logo1()
        
        if(choice == "scan"):
            if(type == "subnet"):
                if(subnet_range):
                    subnet.Scanner(range=subnet_range).scan()
                elif(interface):
                    interfaceScan.InterfaceScanner(interface=interface).scan()

        





runner = Main()
runner.forward()

