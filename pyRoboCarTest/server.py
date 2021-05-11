import socket


class Server:

    def __init__(self, host='0.0.0.0', port=8000):
        """

        :param host:
        :param port:
        """
        self.host = host
        self.port = port

        self.conn_tuple = (self.host, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._bind()
        self._listen()

    def __del__(self):
        """ destructor

        """
        self.socket.close()

    def _bind(self):
        """

        """
        self.socket.bind(self.conn_tuple)

    def _listen(self):
        """

        """
        self.socket.listen()

    def accept(self):
        """

        """
        return self.socket.accept()

    def accept_io_stream(self):
        """

        :return:
        """
        return self.socket.accept()[0].makefile('wb')


if __name__ == '__main__':
    server = Server()
    server.accept_io_stream()
