import re
import os
import requests

URL = os.environ.get("URL", "http://gabibbo-says.challs.olicyber.it")

init_flag = "flag{.*}"

r = requests.post(URL, data={
    "gabibbo" : "angry"
})

flag = re.findall(init_flag, r.text)[0]

print(flag) # flag{v0l3t3_4nCh3_l4_m14_f1rm4?}