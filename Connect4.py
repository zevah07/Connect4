def tablerovacio():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def soltarFichaEnColumna(ficha, col, tablero):
		for row in range(6, 0, -1):
				if tablero[row - 1][col - 1] == 0:
						tablero[row -1][col -1] = ficha
						return

def completarTableroEnOrden(secuencia, tablero):
	c = 0
	for col in secuencia:
		if c % 2 != 0:
			soltarFichaEnColumna(2, col, tablero)
		else:
			soltarFichaEnColumna(1, col, tablero)
		c += 1
	return tablero

def dibujarTablero(tablero):
		for row in tablero:
			print(row)

def tiroValido(secuencia):
    	for col in secuencia:
		if col<1 & col >7:
			return False
	return True
    def contenidoColumna(nrocol, tablero):
    	col = []
	for row in tablero:
		cell = row[nrocol - 1]
		col.append(cell)
	return col

def contenidoFilas(nro_row, tablero):
	rows = []
	for col in tablero:
		cell = col[nro_row - 1]
		rows.append(cell)
	return rows

def ContenidoTodasLasColumnas(tablero):
	col = []
	for nrocol in range(0, 7):
		col.insert(7,contenidoColumna(nrocol,tablero))
	return col

secuencia = [1, 2, 3, 1]
tablero = tablerovacio()
if tiroValido(secuencia):
	tablero = completarTableroEnOrden(secuencia, tablero)
	dibujarTablero(tablero)
	print("La secuencia es valida")
else:                                                        
	print("Para que la secuencia sea valida los valores tienen que estar comprendidos entre el 1 y el 7") 
print(contenidoColumna(2, tablero))