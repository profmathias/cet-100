from zeroconf import Zeroconf, ServiceBrowser, ServiceListener


class Listener(ServiceListener):

    def update_service(self, zc: 'Zeroconf', type_: str, name: str) -> None:
        print(f'Um serviço foi atualizado. Tipo: {type_} Nome: {name}')

    def remove_service(self, zc: 'Zeroconf', type_: str, name: str):
        print(f'Um serviço foi removido: Tipo: {type_} Nome: {name}')

    def add_service(self, zc: 'Zeroconf', type_: str, name: str):
        print(f'Um servico foi encontrado. Tipo: {type_} Name: {name}')


def main():
    zeroconf = Zeroconf()
    listener = Listener()
    service_browser = ServiceBrowser(zeroconf, "_sd-chat-host._tcp.local.", listener)
    try:
        input("Press enter to exit...\n\n")
    finally:
        zeroconf.close()


if __name__ == '__main__':
    main()
