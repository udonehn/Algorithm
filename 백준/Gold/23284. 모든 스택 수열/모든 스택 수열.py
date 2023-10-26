def print_answer(answer):
    stack=[]
    index=1
    for push_or_pop in answer:
        if push_or_pop==0:
            print(stack.pop(), end=' ')
        else:
            stack.append(index)
            index+=1
    print()

def solve(N, index, push_status, pop_status, answer):
    if len(answer)==N*2:
        print_answer(answer)
        return
    if pop_status<push_status:  #case: pop
        solve(N, index, push_status, pop_status+1, answer+[0])
    if index<=N:    #case: push
        solve(N, index+1, push_status+1, pop_status, answer+[1])

if __name__=="__main__":
    solve(int(input()), 1, 0, 0, [])