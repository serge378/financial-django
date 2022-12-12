import environ

env = environ.Env()
environ.Env.read_env()
from .base import *

# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
if env("env") == "prod":
    from .prod import *
else:
    from .dev import *
