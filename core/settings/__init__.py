import environ

env = environ.Env()
environ.Env.read_env()
from .base import *

# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
if env("env") == "prod":
    print("DJANGO HELLO WORLD")
    from .prod import *
else:
    print("DJANGO HELLO WORLD DEV")
    from .dev import *
