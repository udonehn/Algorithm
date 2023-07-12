import sys
N = sys.stdin.readline().strip()
TF=True
for i in list(N):
  if int(i)!=0:
    if int(N)%int(i)!=0:
      TF=False
      break
if TF==True:
  print(N)
else:
  k=10
  while True:
    NN=int(N)*k
    for i in range(k):
      NNN=NN+i
      count=0
      TF=False
      for j in str(N):
        if int(j)==0:
          count+=1
        else:
          if NNN%int(j)==0:
            count+=1
      if count==len(str(N)):
        TF=True
        break
    if TF==True:
        break
    k=k*10
  print(NNN)