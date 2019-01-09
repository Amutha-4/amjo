def contando_sString_igual(String1, String2):
    resposta = ""
    tamanho1 = len(String1)
    tamanho2 = len(String2)
    for i in range(tamanho1):
        for j in range(tamanho2):
            lcs_temp = 0
            igual = ''
            while i + lcs_temp < tamanho1 and j + lcs_temp < tamanho2 and String1[i + lcs_temp] == string2[j + lcs_temp]:
                igual += String2[j+lcs_temp]
                lcs_temp += 1
            if len(igual) > len(resposta):
                resposta = igual
    return len(resposta)


while True:
    a = input()
    b = input()
    if a is None or b is None:
        break
    else:
        print(contando_sString_igual(a, b))
