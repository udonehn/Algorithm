# [Platinum IV] Fleecing the Raffle - 13359 

[문제 링크](https://www.acmicpc.net/problem/13359) 

### 성능 요약

메모리: 114844 KB, 시간: 140 ms

### 분류

조합론, 수학

### 문제 설명

<p>A tremendously exciting raffle is being held, with some tremendously exciting prizes being given out. All you have to do to have a chance of being a winner is to put a piece of paper with your name on it in the raffle box. The lucky winners of the p prizes are decided by drawing p names from the box. When a piece of paper with a name has been drawn it is not put back into the box – each person can win at most one prize.</p>

<p>Naturally, it is against the raffle rules to put your name in the box more than once. However, it is only cheating if you are actually caught, and since not even the raffle organizers want to spend time checking all the names in the box, the only way you can get caught is if your name ends up being drawn for more than one of the prizes. This means that cheating and placing your name more than once can sometimes increase your chances of winning a prize.</p>

<p>You know the number of names in the raffle box placed by other people, and the number of prizes that will be given out. By carefully choosing how many times to add your own name to the box, how large can you make your chances of winning a prize (i.e., the probability that your name is drawn exactly once)?</p>

### 입력 

 <p>The input consists of a single line containing two integers n and p (2 ≤ p ≤ n ≤ 10<sup>6</sup>), where n is the number of names in the raffle box excluding yours, and p is the number of prizes that will be given away.</p>

### 출력 

 <p>Output a single line containing the maximum possible probability of winning a prize, accurate up to an absolute error of 10<sup>−6</sup>.</p>

