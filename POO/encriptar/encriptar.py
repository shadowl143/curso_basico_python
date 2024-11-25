

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text  = input("palabra: ")
text_encrypt: str = ""
counter = 0
count_next:int = 3
# print(text[7])

## recorrer
for t in text.lower():
    # obtener la letra que quieres cambiar
    letter = t[counter]
    #conocer la posicion de la letra en la lista obtener su indice.
    search_letter = abecedario.index(letter)
    print(search_letter)
    if(search_letter + 2) > len(abecedario):
        search_letter = 0
    text_encrypt += abecedario[search_letter + 3]

print(text_encrypt)
    