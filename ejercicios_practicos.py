# Ordenar lista de menor a mayor
def ordenar_lista(lista):
  return sorted(lista)

# Contar palabras en un archivo
def contar_palabras(file_name):
  with open(file_name, 'r') as file:
    palabras = file.read()
    return len(palabras.split())
  

if __name__ == "__main__":
  print(ordenar_lista([5,4,6,7,8,9,10,2,0,3,1]))
  print(contar_palabras("texto.txt"))