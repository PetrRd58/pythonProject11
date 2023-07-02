import requests


url = 'http://localhost:8000/cgi-bin/nserv2.py'
servern = requests.get(url)
#response.raise_for_status()
print(servern.text)
my_file = open("servern.txt", "wb")
my_file.write(servern.content)
my_file.close()