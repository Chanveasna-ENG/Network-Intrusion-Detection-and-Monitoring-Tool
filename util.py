import subprocess

def block_ip(ip):
    subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                    'name="Block IP {}"'.format(ip), 'dir=in', 'action=block',
                    'remoteip={}'.format(ip), 'enable=yes'], check=True)


def allow_ip(ip):
    subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                    'name="Block IP {}"'.format(ip)], check=True)
    
def alert_ip(ip):
    pass