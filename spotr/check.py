import json
import requests
import numpy as np
import pandas as pd

import requests
from requests.auth import HTTPBasicAuth
username = "Piyush4064"
data = requests.get('https://codeforces.com/api/user.info?handles=' + username)
data = data.json()