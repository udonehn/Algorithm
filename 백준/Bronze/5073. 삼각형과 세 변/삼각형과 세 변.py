if __name__=="__main__":
    while True:
        A,B,C = map(int, input().split())
        if A==0 and B==0 and C==0:
            break
        if max(A,B,C)>=sum([A,B,C])-max(A,B,C):
            print("Invalid")
        elif A==B==C:
            print("Equilateral")
        elif (A==B) or (A==C) or (B==C):
            print("Isosceles")
        else:
            print("Scalene")