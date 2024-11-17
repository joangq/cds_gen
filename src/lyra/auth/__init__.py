"""
Wrapper for the CDS API Client.
Allows for dotenv authentication for normalization of credentials,
instead of looking up the credentials in $HOME.
"""

from .wrapper import ClientClass
from .wrapper import Client