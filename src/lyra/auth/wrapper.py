from cdsapi.api import Client as CdsApiClient
from warnings import warn
from requests import Session
from typing import Optional, Callable, Any
from .types import Deprecated, Unreachable

DEFAULT_CDS_API_URL = 'https://cds.climate.copernicus.eu/api'

class ClientClass(CdsApiClient):
    def __init__(*_, **__) -> Unreachable:
        raise TypeError("This class should not be instantiated")
    
    def __new__(
          cls
        , url                 : Optional[str]      = None
        , key                 : Optional[str]      = None
        , quiet               : bool               = False
        , debug               : bool               = False
        , verify              : Optional[bool]     = None
        , timeout             : int                = 60
        , progress            : bool               = True
        , full_stack          : Deprecated[bool]   = None
        , delete              : bool               = True
        , retry_max           : int                = 500
        , sleep_max           : int                = 120
        , wait_until_complete : bool               = True
        , info_callback       : Optional[Callable] = None
        , warning_callback    : Optional[Callable] = None
        , error_callback      : Optional[Callable] = None
        , debug_callback      : Optional[Callable] = None
        , metadata            : Optional[Any]      = None
        , forget              : Deprecated[bool]   = None
        , session             : Optional[Session]  = None
        ) -> CdsApiClient:

        session = session or Session()

        try:
            from dotenv import find_dotenv, dotenv_values
            env_file = find_dotenv('.env')
            key = dotenv_values(env_file).get('CDS_API_KEY', key)
            
            if key is None:
                raise ValueError('No CDS_API_KEY found in ".env" file')
            
        except ImportError:
            warn('python-dotenv not found, loading key from parameter. You can install it with "pip install python-dotenv"')

        except FileNotFoundError:
            warn('No ".env" file found, loading key from parameter.')

        url = url or DEFAULT_CDS_API_URL

        return CdsApiClient(
              url                 = url
            , key                 = key
            , quiet               = quiet
            , debug               = debug
            , verify              = verify
            , timeout             = timeout
            , progress            = progress
            , full_stack          = full_stack
            , delete              = delete
            , retry_max           = retry_max
            , sleep_max           = sleep_max
            , wait_until_complete = wait_until_complete
            , info_callback       = info_callback
            , warning_callback    = warning_callback
            , error_callback      = error_callback
            , debug_callback      = debug_callback
            , metadata            = metadata
            , forget              = forget
            , session             = session
        )

global client_instance
client_instance = None
def Client(
          url                 : Optional[str]      = None
        , key                 : Optional[str]      = None
        , quiet               : bool               = False
        , debug               : bool               = False
        , verify              : Optional[bool]     = None
        , timeout             : int                = 60
        , progress            : bool               = True
        , full_stack          : Deprecated[bool]   = None
        , delete              : bool               = True
        , retry_max           : int                = 500
        , sleep_max           : int                = 120
        , wait_until_complete : bool               = True
        , info_callback       : Optional[Callable] = None
        , warning_callback    : Optional[Callable] = None
        , error_callback      : Optional[Callable] = None
        , debug_callback      : Optional[Callable] = None
        , metadata            : Optional[Any]      = None
        , forget              : Deprecated[bool]   = None
        , session             : Optional[Session]  = None
        ) -> ClientClass:
    global client_instance
    if client_instance is None:
        client_instance = ClientClass(
              url                 = url
            , key                 = key
            , quiet               = quiet
            , debug               = debug
            , verify              = verify
            , timeout             = timeout
            , progress            = progress
            , full_stack          = full_stack
            , delete              = delete
            , retry_max           = retry_max
            , sleep_max           = sleep_max
            , wait_until_complete = wait_until_complete
            , info_callback       = info_callback
            , warning_callback    = warning_callback
            , error_callback      = error_callback
            , debug_callback      = debug_callback
            , metadata            = metadata
            , forget              = forget
            , session             = session
        )
    return client_instance