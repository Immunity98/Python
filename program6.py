#входные данные: число (факториал какого-то числа)
#выходные данные: число (то, с которого этот факториал получился)
#пример. входные данные: 120, результат: 5 (max =1000) ==> точные числа
print ('Enter any chislo factorial')
a = int(input())
i=1
s=1
if a>1000:
          exit()
if (a % 6) ==0 or ((a==1) or (a==2)): 
          while s <a:
                    if s<a:
                              a=a/i
                              i=i+1
          if i>1:
                    i=i-1
          if a<=0:
                    a=1
                    i=1
          print ('chislo factorial=', i)
else:
          print ('Error #144')
input()

