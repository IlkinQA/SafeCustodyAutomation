import enum
from tokenize import Token

import pytest
import requests
from src.Data.Token import *


class ClientData(enum.Enum):
    UserId = '1264372'
    OrganizationId = '274116'
    Login = 'UAI5981842'
