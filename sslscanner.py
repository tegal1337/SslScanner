from ast import If
import os,sys
import pkg_resources

for package in ['sslyze']:
    try:
        dist = pkg_resources.get_distribution(package)
    except pkg_resources.DistributionNotFound:
        ist = os.system("pip3 install sslyze")
        ist = os.system("sudo apt install sslyze -y")
        print (ist)

os.system('clear')
print ("""
  __   __  _      __   ___ __  __  _ __  _ ___ ___  
/' _//' _/| |   /' _/ / _//  \|  \| |  \| | __| _ \ 
`._`.`._`.| |_  `._`.| \_| /\ | | ' | | ' | _|| v / 
|___/|___/|___| |___/ \__/_||_|_|\__|_|\__|___|_|_\ 
                    Tegal1337
----------------------------------------------------
python3 sslscanner.py domain.com
""")

host = sys.argv[1]


ssl = os.system("sslyze --mozilla_config=modern --fallback --reneg --elliptic_curves --heartbleed --certinfo --sslv3 --http_headers --openssl_ccs --early_data --robot "+host+" --json_out=results.json")
print (ssl)
