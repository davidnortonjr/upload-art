from zeroconf import ServiceBrowser, ServiceListener, Zeroconf

class MyListener(ServiceListener):

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        return

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        return

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        if info.properties[b'manufacturer'] == b'Samsung':
            print(f"Found {name.replace('._airplay._tcp.local.', '')}, hostname: {info.server}")

zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_airplay._tcp.local.", listener)
try:
    input("Press enter to exit...\n\n")
finally:
    zeroconf.close()
