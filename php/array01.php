<?php
	print_r("01 - Array"); 
	$array = array("palavras" => array(1=>"a",2=>"b",3=>"c"), "numeros" => array(1=>"1",2=>"2"));

	print_r($array);
	print_r("");

	print("02 - Array_keys"); 
	print_r(array_keys($array["palavras"], "c"));

	$array = array("azul", "vermelho", "verde", "azul", "azul");
	print_r(array_keys($array, "azul"));

?>
