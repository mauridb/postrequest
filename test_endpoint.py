import sys
import requests
import requests.auth import HTTPDigestAuth



URL = sys.argv[1]
AUTH = HTTPDigestAuth('<USER>', '<PASSWORD>')
PAYLOAD = {

   'key':'value',

}

r = requests.post(str(URL), auth=AUTH, params=PAYLOAD)
# print(r)

