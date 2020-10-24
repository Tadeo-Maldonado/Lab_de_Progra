echo "Selecciona 1 para codificar, cualquier otra tecla para decodificar"
read num
if [ $num == 1 ]; then
#La ruta se establece (ejemplo) C:/Users/mxcal/desktop/practica5
	echo "Escribe la ruta completa donde se encuentra el archivo a cifrar"
	read ruta
	cd $ruta
	echo "Como se llama el archivo?"
	read nombre
#Apartado para averiguar cheksum
	echo "Desea realizar el checksum del archivo" Oprima 1 para confirmar, 2 para seguir?
	read check
	if [ $check == 1 ]; then
		md5sum $nombre > valor.txt
		echo "El cheksum de $nombre es igual a:"
		cat valor.txt
	fi
#Creacion del archivo de codificación
	echo "Como se llamara el archivo resultante?"
	read archivo
	base64 < $nombre > $archivo.txt 
else
        echo "Escribe la ruta completa donde se encuentra el archivo a decifrar"
        read ruta
        cd $ruta
        echo "Como se llama el archivo?"
        read nombre
        echo "Como se llamara el archivo resultante?"
        read archivo
        base64 -d < $nombre > $archivo
fi
