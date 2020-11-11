import time

from socket import inet_aton
from zeroconf import Zeroconf, ServiceInfo


def main():
    service_info = ServiceInfo(
        type_='_sd-chat-host._tcp.local.',
        name='host1._sd-chat-host._tcp.local.',
        port=5000,
        addresses=[inet_aton('192.168.15.20')]
    )
    zeroconf = Zeroconf()
    zeroconf.register_service(service_info)
    print(f'Serviço Anunciado... Nome: {service_info.name}')
    time.sleep(10)
    zeroconf.unregister_service(service_info)


if __name__ == '__main__':
    main()
