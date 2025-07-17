import ssl
import socket
from datetime import datetime
domains = [
    "google.com",
    "github.com",
    "dockerhub.io"
]
def get_ssl_expiry(domain, port=443):
    """Returns the expiry date of ssl certificates"""
    context = ssl.create_default_context()
    with socket.create_connection((domain, port), timeout=5)as sock:
        with context.wrap_socket(sock, server_hostname=domain)as ssock:
            cert = ssock.getpeercert()
            expiry = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
            return expiry