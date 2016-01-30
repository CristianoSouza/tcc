#!/usr/bin/env python

''' 
 *  Programa : Servidor python com comunicação por socket
 *  Autor : Cristiano Antonio de Souza
 *  Email : cristianoantonio.souza10@gmail.com
'''

'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
 
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
    string_recebida = data.decode()
    print ("Informação Recebida(", addr[0],"):", string_recebida)
    print ("TRATAR INFORMAÇÃO....")
    sub_strings = string_recebida.split("-")
    print (sub_strings)
    
    modo_operacao = sub_strings[0]
    sala =  sub_strings[1]
    rfid_code =  sub_strings[2]

    if(sub_strings[0] == "INICIALIZACAO"):
        print ("Conexao de inicializacao")
        modo_operacao = sub_strings[1]
        process = ProcessInformation()
        sala = process.start_arduino(sub_strings[2])
        print ("SALA: ", sala)
        rfid_code =  sub_strings[3]
        message = str(sala)
        print ("MESSAGE: ", message )
        if(conn.send(message.encode())):
            print ("Mensagem de confirmação enviada")
        else:
            print ("ERRO: Mensagem de confirmação não pode ser enviada!")


    if(modo_operacao == "INSERCAO"):
        print ("MODO INSERCAO!")
        process = ProcessInformation()
        status = process.insert(rfid_code)
        if not (status):
            print ("FALHA NO PROCESSO")
            message = '0'
        elif(status == process.SUCESSO): 
            print ("INSERCAO SUCESSO")
            message = '1'
        elif(status == process.FALHA_CRACHA_JA_CADASTRADO):
            print ("CRACHA JAH CADASTRADO")
            message = '5'
    else:
        print ("MODO NORMAL")
        process = ProcessInformation()
        status = process.process_information(rfid_code, sala)

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
    #ip= '192.168.1.100'
    ip= '192.168.25.2'
    port= 5010
    buffer_size= 1024
    communication_protocol= "TCP"
    server = Server(ip, port, buffer_size, communication_protocol)
    server.start()
