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
        
for domain in domains:
    try:
        expiry_date = get_ssl_expiry(domain)
        days_left = (expiry_date -datetime.utcnow()).days
        status = "ok" if days_left > 15 else "expiring soon"
        print(f"{domain:<30} expires in {days_left} days ({expiry_date}) [{status}]")
    except Exception as e:
        print(f"{domain:<30} Error: {e}")