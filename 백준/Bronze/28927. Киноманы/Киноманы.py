max = list(map(int, input().split()))
mel = list(map(int, input().split()))
max_time = 0
mel_time = 0
time = [3,20,120]
for i in range(3):
    max_time+=max[i]*time[i]
    mel_time+=mel[i]*time[i]
if max_time>mel_time:
    print("Max")
elif max_time<mel_time:
    print("Mel")
else:
    print("Draw")