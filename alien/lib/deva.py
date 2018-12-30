import logging
import socketserver
import threading

from lib.globals import LOGGER_TAG, TRIGGER_SRV_HOST, TRIGGER_SRV_PORT


class ExternalTriggerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        logger = logging.getLogger(LOGGER_TAG)
        try:
            command = self.request.recv(1024).strip().decode("utf-8")
            logger.info("Received External command from {}. Command : {}".
                        format(self.client_address, command))
            self.server.forward_command(command)
        except Exception:
            pass


class CustomizedTCPServer(socketserver.TCPServer):
    def __init__(self, talk_queue, server_address, RequestHandlerClass, bind_and_activate=True):
        super(CustomizedTCPServer, self).__init__(server_address=server_address,
                                                  RequestHandlerClass=RequestHandlerClass,
                                                  bind_and_activate=bind_and_activate)
        self.talk_queue = talk_queue

    def forward_command(self, command):
        self.talk_queue.put(command)


class ExternalTrigger(threading.Thread):
    def __init__(self, talk_queue):
        super(ExternalTrigger, self).__init__()
        self.talk_queue = talk_queue
        self.logger = logging.getLogger(LOGGER_TAG)

    def run(self):
        self.logger.info("Starting off External Command listener at {}:{} ...".
                         format(TRIGGER_SRV_HOST, TRIGGER_SRV_PORT))
        server = CustomizedTCPServer(server_address=(TRIGGER_SRV_HOST, TRIGGER_SRV_PORT),
                                     RequestHandlerClass=ExternalTriggerHandler,
                                     talk_queue=self.talk_queue)
        server.serve_forever()
