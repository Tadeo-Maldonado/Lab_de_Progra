echo "Este codigo sirve para saber si un numero es impar o par"
echo "Ingrese un número"
read numero

contenedor= echo $(($numero % 2))

if ($contenedor=0);
then
	echo "Numero par"
else
	echo "Numero impar"
fi
