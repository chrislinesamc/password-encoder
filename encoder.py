import  sys
import base64
from base64 import b32encode

# get argument from command line
input = sys.argv[1]

#b32encoding
input = b32encode(input.encode()).decode()

#b64encoding
input = base64.b64encode(input.encode("ascii")).decode("ascii")

print(input)
