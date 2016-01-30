<?php

echo "teste01.php";
echo "teste01.php";
if(!($sock = socket_create(AF_INET, SOCK_STREAM, 0)))
{
    $errorcode = socket_last_error();
    $errormsg = socket_strerror($errorcode);
     
    die("Couldn't create socket: [$errorcode] $errormsg \n");
}
 
echo "Socket created";

// Se conecta ao IP e Porta:
socket_connect($sock,"192.168.0.250", 8080);
echo "Conectou";
//falta testar se conseguiu conectar.

print ("Servidor rodando!");

$sensor = socket_read($sock);
     echo $sensor;  
     socket_close($sock);

//  ---*/

?>
