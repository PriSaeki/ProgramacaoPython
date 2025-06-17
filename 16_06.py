def teste():
  try:  
    l = [1,2,3]
    n = int(input('Digite um valor inteiro'))
    n2 = int(input('Digite um valor inteiro'))
    print(n/n2)
    n3 = int(input('Digite um valor inteiro'))
    s = n + n3
    print(s)
    print(l[3])
  except ZeroDivisionError as erro:
    print(erro)
  except ValueError as erro:
    print(erro)   
  except TypeError as erro:
    print(erro)  
  except IndexError as erro:
    print(erro)  
  else:
    print('Isso tb pode ser que carregue...')  
  finally:
    print('Fim de carregamento ...')      


while True:
      teste()    
