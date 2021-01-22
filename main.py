k = 100
todos_os_valores = [15, 22, 14, 26, 32, 9, 16, 8]
todos_os_valores = [x+1 for x in range(k)]
todos_os_valores.sort()
solucoes = 0
print(todos_os_valores)
print("soma",k)

def somar_lista(valores):
  soma = 0
  for i in range(len(valores)):
    soma += valores[i]
  return soma

def resolver(valores,k,subset=[], atual=0):
  global solucoes
  for i in range(len(valores)-atual):
    atual += i
    subset.append(valores[atual])
    if somar_lista(subset) == k:
      print(subset)
      solucoes += 1
    if somar_lista(subset) < k:
      resolver(valores,k,subset,atual+1)   
    atual -= i   
    subset.pop()

resolver(todos_os_valores,k)
print("Existem",solucoes,"combinações que somam",k)
