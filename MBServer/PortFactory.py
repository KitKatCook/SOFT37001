from ServerSetupConfig import *

from http.server import BaseHTTPRequestHandler
from socketserver import TCPServer

class PortCheckerFactory():
    PortsInUse = list[int]

    def GetNextPort():
        for p in range(port, (port + 1000)):
            try:
                with TCPServer(('', p), BaseHTTPRequestHandler) as s:
                    s.server_close()
                if p in PortCheckerFactory.PortsInUse:
                    raise OSError()
                else:
                    self.PortsInUse.append(port)
                return p
            except OSError:
                pass
            
            raise OSError("Port {} is already in use.".format(p))
        