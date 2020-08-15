import nmap

ns = nmap.PortScanner()

print(ns.nmap_version())

ns.scan('',"1-1024')

print(ns.scanstats())

print(ns.csv())

input("completed! press enter to exit")
