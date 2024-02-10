import requests
import sys
import os
import time
import random
import re
from pathlib import Path

# Default variables
output='./output/'
extension=''

# Arguments
list=sys.argv[1]
#output=sys.argv[2]
extension=sys.argv[2]

# Create output directory.
Path(output).mkdir(parents=True, exist_ok=True)

# Increment file name function
def counter(i):
    return i + 1
# File counter.
i = 1

# Requests headers.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}
with open(list) as url_file:
    for x in url_file:
        #r = requests.get(x.rstrip('\n\'"'))
        r = requests.get(re.sub(f"[\n\,\"\']", "", x), headers=headers)
        with open(output +"image" + "-"+ str(i).zfill(4) + extension, 'wb') as f:
            f.write(r.content)
            file_name = f.name
            i = counter(i)
        print("Requested -> "+str(r.request.headers))
        print("")
        print("Saving -> "+f.name)
        print("")
        t = random.randint(1, 5)
        print("Sleeping "+str(t))
        print("")
        time.sleep(t)




