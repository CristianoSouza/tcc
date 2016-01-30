#!/usr/bin/env python


''' 
 *  Programa : Biblioteca escrita em python com funcionalidades para manipular banco de dados postgres do sistema de controle de prensença academico.
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

import psycopg2
import sys
import _thread
import time



class ProcessInformation(object):
    
    SUCESSO = 1
    FALHA_CRACHA_NAO_CADASTRADO = 2
    FALHA_HORARIO_INVALIDO = 3
    FALHA_NO_PROCESSO = 4
    FALHA_CRACHA_JA_CADASTRADO = 4

    connection= None
    list_ids_aulas = []
    id_aluno = None
    response = None
    rfid_code = None
    id_rfid = None
    id_sala = None

    def connect_database(self):
        try:
            self.connection = psycopg2.connect(database='applicationManager', user='postgres')
            print (self.connection)
        except (psycopg2.DatabaseError, e):
            print ('Error %s' % e) 
            sys.exit(1)

    def insert(self, codeRFID):
        self.connect_database()

        print ("INSERIR DADO:")
        code = (codeRFID)
        if (self.check_badge(code) != self.SUCESSO):
            print ("cadastrar cracha!")
            try:
                cur= self.connection.cursor()

                a = cur.execute(("INSERT INTO \"academicManager_rfid\" (rfid_code) VALUES (%s)"), [codeRFID])
                print (a)            
                
                self.connection.commit()
                return self.SUCESSO
            except (psycopg2.DatabaseError, e):
                print ('Error %s' % e) 
                return False
        else:
            print ("cracha jah esta cadastrado!")
            return self.FALHA_CRACHA_JA_CADASTRADO

    def check_badge(self, codeRFID):

        print ("select id rfid:")
        code = (codeRFID)

        cur= self.connection.cursor()
        
        try:
            cur.execute(("Select * from \"academicManager_rfid\" where rfid_code LIKE (%s)"), [codeRFID])

            rows = cur.fetchall()
            print ("\nRows: \n")
            if (rows):
                print ("Existe!")
                for row in rows:
                    print ("   ", row[1])
                    self.id_rfid = row[0]
                return self.SUCESSO
            else:
                print ("Não Existe")
                return False
        except:
            print ("Não foi possivel fazer consulta em academicManager_rfid!")
            return self.FALHA_CRACHA_NAO_CADASTRADO

    def get_id_aluno_by_rfid(self):

        print ("Select id aluno:")

        cur= self.connection.cursor()
        
        try:
            cur.execute(("Select * from \"academicManager_aluno\" where rfid_code_id = (%s)"), [self.id_rfid])

            rows = cur.fetchall()
            print ("\nRows: \n")
            if (rows):
                print ("Existe!")
            else:
                print ("Não Existe")
                return 0
            for row in rows:
                print ("   ", row[1])
                self.id_aluno = row[0]
                return

        except:
            print ("Não foi possivel fazer consulta em academicManager_aluno!")

    def get_id_aula_by_aluno(self):

        print ("select id disciplina:")

        cur= self.connection.cursor()

        print ("id aluno: ", self.id_aluno)
        
        try:
            cur.execute(("Select * from \"academicManager_alunodisciplina\" where aluno_id = (%s)"), [self.id_aluno])

            rows = cur.fetchall()
            print ("\nRows: \n")
            if (rows):
                print ("Existe!")
            else:
                print ("Não Existe")

            for row in rows:
                print ("ID: ", row[2])
                cur.execute(("Select * from \"academicManager_aula\" where disciplina_id = (%s) AND sala_id = (%s)"), [row[2],self.id_sala])

                rows2 = cur.fetchall()
                for row2 in rows2:
                    print ("ID aula: ", row2)
                    self.list_ids_aulas.append(row2)
            print ("LISTA>:", self.list_ids_aulas)
    
        except:
            print ("Não foi possivel fazer consulta em academicManager_alunodisciplina!") 

    def check_duplicate(self, id_aula):

        print ("Verificar se a presença jah esta armazenada:")

        cur= self.connection.cursor()

        print ("id aluno: ", self.id_aluno)
        print ("id aula: ", id_aula)
        
        try:
            cur.execute(("Select * from \"academicManager_chamada\" where aula_id = (%s) AND aluno_id = (%s) AND presence= (%s)"), [id_aula, self.id_aluno, "P"])

            rows = cur.fetchall()
            print ("\nRows: \n")
            if (rows):
                print ("Existe!")
                return True
            else:
                print ("Não Existe")
                return False

        except:
            print ("Não foi possivel fazer consulta em academicManager_chamada!") 

    def check_time_aulas(self):

        print ("verificar horario das aulas:")
        print ("LISTA>--:", self.list_ids_aulas)
        for list in self.list_ids_aulas:
            print ("Data Aula: ", list[2].strftime("%Y/%m/%d"))
            data_atual = time.strftime("%Y/%m/%d")
            print ("Data atual: ", data_atual)
            if (data_atual == list[2].strftime("%Y/%m/%d") ):
                print ("Dia atual!")
                hora_inicio_aula = list[4].strftime("%H:%M:%S")
                hora_fim_aula = list[3].strftime("%H:%M:%S")
                print ("Hora Inicio Aula: ", hora_inicio_aula)
                print ("Hora Fim Aula: ", hora_fim_aula)
                hora_atual = time.strftime("%H:%M:%S")
                print ("Hora atual: ", hora_atual)

                if ( (hora_atual > hora_inicio_aula) & (hora_atual < hora_fim_aula)):
                    print ("Horario de aula valido!")
                    #if (self.check_duplicate(list[0])):
                     #   print ("Presença jah esta registrada!")
                    #else:
                    print ("Pode realizar a gravação da presença")
                    if (self.confirm_presence(list[0]) == self.SUCESSO):
                        return self.SUCESSO
                    else: 
                        return self.FALHA_NO_PROCESSO
                else:
                    print ("Não possui aula neste horario!")  
            else: 
                print ("Aluno não possui nenhuma aula hoje!");
        return self.FALHA_HORARIO_INVALIDO

    def confirm_presence(self, id_aula):
        print ("Confirmando Presença:")

        hora_atual = time.strftime("%H:%M:%S")
        print ("Hora atual: ", hora_atual)
        print ("id Aluno: ", self.id_aluno)
        print ("id_aula: ", id_aula)
        cur= self.connection.cursor()
        
        try:
            cur.execute(("UPDATE \"academicManager_chamada\" SET presenca = 'P', horario_leitura = (%s) WHERE aluno_id = (%s) AND aula_id = (%s)"),[hora_atual,self.id_aluno, id_aula])
        except:
            print ("Não foi possivel fazer update em academicManager_chamada!")
            return self.FALHA_NO_PROCESSO

        self.connection.commit()
        print ("COMMIT;")
        return self.SUCESSO

    def process_information (self, rfid_code, id_sala):
        self.connect_database()
        self.rfid_code = rfid_code
        self.list_ids_aulas = []
        self.id_sala = id_sala
        
        print ("status ", self.check_badge(self.rfid_code))

        if (self.check_badge(rfid_code) == self.SUCESSO): 
        
            print ("ID_RFID: ", self.id_rfid)
            print ("Cracha valido!")
            self.get_id_aluno_by_rfid()
            self.get_id_aula_by_aluno()
            print ("LISTA ->:", self.list_ids_aulas)
            return self.check_time_aulas() 
        else:
            print ("Cracha nao cadastrado!")
            return self.FALHA_CRACHA_NAO_CADASTRADO

    def get_id_arduino(self, id_arduino):

        print ("Select id arduino:")

        cur= self.connection.cursor()
        
        try:
            cur.execute(("Select * from \"academicManager_arduino\" where id_arduino = (%s)"), [id_arduino])

            rows = cur.fetchall()
            print ("\nRows: \n")
            if (rows):
                print ("Existe!")
            else:
                print ("Não Existe")
                return 0
            for row in rows:
                print ("   ", row[1])
                return row[0]

        except:
            print ("Não foi possivel fazer consulta em academicManager_arduino!")

    def get_sala_by_arduino(self, id_arduino):

        print ("Select id sala:")

        cur= self.connection.cursor()
        
        try:
            cur.execute(("Select * from \"academicManager_sala\" where arduino_id = (%s)"), [id_arduino])

            rows = cur.fetchall()
            print ("\nRows: \n")
            if (rows):
                print ("Existe!")
            else:
                print ("Não Existe")
                return 0
            for row in rows:
                print ("   ", row[1], " - ", row[2], " - ", row[3])
                return row[0]

        except:
            print ("Não foi possivel fazer consulta em academicManager_sala!")

    def start_arduino (self, id_arduino):
        self.connect_database()
        
        id = self.get_id_arduino(id_arduino)
        
        id_sala = self.get_sala_by_arduino(id)
        
        return id_sala

