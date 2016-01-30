#!/usr/bin/env python
 
import socket
import sys
from process_Information import ProcessInformation 
import _thread

class Server(object):
    
    _communication_protocol = None
    _ip = None
    _port = None
    _buffer_size = None
    _running = False

    def __init__(self, ip, port, buffer_size, communication_protocol):
        self._ip= ip
        self._port= port
        self._buffer_size= buffer_size
        self._communication_protocol= communication_protocol

    def start_TCP(self):
        #instanciando socket
        _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _socket.bind((self._ip, self._port))
        _socket.listen(5)

        print ('--INICIANDO SERVIDOR!')
        print ('Ip: ', self._ip)
        print ('Port: ', self._port)
        print ('Buffer size: ', self._buffer_size)

        self.__running= True

        while 1:

            print ("Aguardando cliente...")
            conn, addr = _socket.accept()
            
            print ('--CONEXAO ESTABELECIDA')
            print ('Cliente: ', addr)
            print ('Conexão Servidor/Cliente: ', conn)
            
            _thread.start_new_thread(manager_connection, tuple([_socket, conn, addr, self._buffer_size]))

    def start_UDP(self):
        _socket = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) 
        _socket.bind((self._ip, self._port))
        print ("sock:",_socket)
        while True:
            print ("Whille")
            data, addr = _socket.recvfrom(2048) # buffer size is 1024 bytes
            print ("Address: ", addr)
            print ("received message:", data)
            _data = "Blue" #Set data to Blue Command
            print ("enviando resposta!!")
            a = _socket.sendto(_data.encode(), addr) #send command to arduino
            print ("RESPOSTA ENVIADA - result: ", a)

    def start(self):
        print ('Protocolo de Comunicação: ', self._communication_protocol)
        if (self._communication_protocol == 'TCP'):
            self.start_TCP()
        else:
            if (self._communication_protocol == 'UDP'):
                self.start_UDP()
            else: 
                print ('Protocolo de comunicação Invalido!')

    def shut_down_server(self):
        self._running = False

def manager_connection(_socket, conn, addr, buffer_size):
    print ("THREAD")

    data = conn.recv(buffer_size)
    #data = "asd"

    print ("Informação Recebida(", addr[0],"):", data.decode())
    print ("TRATAR INFORMAÇÃO....")
    
    process = ProcessInformation()
    status = process.process_information(data.decode())


    if (status == process.SUCESSO):
        message = '1'
    elif(status == process.FALHA_HORARIO_INVALIDO):
        message = '2'
    elif(status == process.FALHA_CRACHA_NAO_CADASTRADO):
        message = '3'
    elif(status == process.FALHA_NO_PROCESSO):
        message = '0'
    print ("MESSAGE: ", message )
    if(conn.send(message.encode())):
        print ("Mensagem de confirmação enviada")
    else:
        print ("ERRO: Mensagem de confirmação não pode ser enviada!")
    conn.close()    
    _thread.exit()

if __name__ == '__main__':
    print ("Iniciando....")
    ip= '192.168.1.101'
    port= 5010
    buffer_size= 100
    communication_protocol= "TCP"
    server = Server(ip, port, buffer_size, communication_protocol)
    server.start()
