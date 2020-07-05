#CONSTANTS
import inspect

URL = "http://demo.appsee.sncqe.com:5000/analytics"
USERNAME = "viewer"
INSTANCE = "demo"
PASSWORD = "AStrip01"


def whoami():
    return inspect.stack()[1][3]
