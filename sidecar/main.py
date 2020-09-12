#!/usr/bin/env python3
from dataclasses import dataclass
import os


@dataclass
class AgentConfig:
    def __init__(self):
        # description: Label that should be used for filtering
        self.label: str = os.getenv('LABEL', 300)
        # description: The value for the label you want to filter your resources on. Don't set a value to filter by any value
        self.label_value: str = os.getenv('LABEL_VALUE', 300)
        # description: Folder where the files should be placed
        self.folder_name: str = os.getenv('FOLDER', 300)
        # description: The annotation the sidecar will look for in configmaps to override the destination folder for files, defaults to 'k8s-sidecar-target-directory'
        self.folder_annotation: str = os.getenv('FOLDER_ANNOTATION', 300)
        # Tracked namespace
        # open('/var/run/secrets/kubernetes.io/serviceaccount/namespace').read()'C:/mydir'
        self.watched_namespaces: str = os.getenv('WATCHED_NAMESPACES', [open('D:/ns.txt').read()])
        # Resouce type, which is monitored by the sidecar. Options: configmap (default), secret, both
        self.resource_type: str = os.getenv('RESOURCE', 'configmap')
        # If METHOD is set with LIST, the sidecar will just list config-maps and exit. With SLEEP it will list all config-maps, then sleep for SLEEP_TIME seconds. Default is watch.
        self.watch_method: str = os.getenv('WATCH_METHOD', 'WATCH')
        # How many seconds to wait before updating config-maps when using SLEEP method.
        self.sleep_time: int = os.getenv('SLEEP_TIME', 300)
        # URL to which send a request after a configmap got reloaded
        self.request_url: str = os.getenv('REQ_URL', ')
        # description: Username to use for basic authentication
        self.request_username: int = os.getenv('REQ_USERNAME', 300)
        # description: Request method GET(default) or POST
        self.request_method: int = os.getenv('REQ_METHOD', 300)
        # description: If you use POST you can also provide json payload
        self.request_payload: int = os.getenv('REQ_PAYLOAD', 300)
        # description: Password to use for basic authentication
        self.request_password: int = os.getenv('REQ_PASSWORD', 300)
        # description: Total number of retries to allow
        self.request_retry_count: int = os.getenv('REQ_RETRY_TOTAL', 5)
        # description: How many connection-related errors to retry on
        self.request_retry_connect: int = os.getenv('REQ_RETRY_CONNECT', 5)
        # description: How many times to retry on read errors
        self.requst_retry_read: int = os.getenv('REQ_RETRY_READ', 5)
        # description: A backoff factor to apply between attempts after the second try
        self.request_retry_backoff: float = os.getenv('REQ_RETRY_BACKOFF_FACTOR', 0.2)
        # description: How many seconds to wait for the server to send data before giving up
        self.request_timeout: int = os.getenv('REQ_TIMEOUT', 10)
        # description: How many seconds to wait before watching resources again when an error occurs
        self.error_throttle_sleep: int = os.getenv('ERROR_THROTTLE_SLEEP', 5)
        # description: Set to true to skip tls verification for kube api calls
        self.sleep_tls_verify: bool = os.getenv('SKIP_TLS_VERIFY', True)
        # description: Set to true to produce unique filenames where duplicate data keys exist between ConfigMaps and/or Secrets within the same or multiple Namespaces.
        self.unique_filenames: str = os.getenv('UNIQUE_FILENAMES', 300)
        # description: The default file system permission for every file. Use three digits (e.g. '500', '440', ...)
        self.file_mode: str = os.getenv('DEFAULT_FILE_MODE', 300)



config = AgentConfig();
print(config.watched_namespaces)
