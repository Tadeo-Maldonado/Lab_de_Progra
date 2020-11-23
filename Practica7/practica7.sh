curl=$(curl ipconfig.me)
ip=$(hostname -I)


nmap --script ftp-syst $ip >txt.txt
nmap --script http-jsonp-detection.nse scanme.nmap.org >>txt.txt
nmap --script netbus-brute $curl >>txt.txt

base64 < txt.txt > Practica7.txt
