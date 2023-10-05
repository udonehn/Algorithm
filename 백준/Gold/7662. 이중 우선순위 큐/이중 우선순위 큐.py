import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()


def pop(heap, heap_dict, current_dict, min_or_max):
    while True:
        pop_number = min_or_max * heappop(heap)
        heap_dict[pop_number] -= 1
        if current_dict[pop_number] - heap_dict[pop_number] == 1:
            break
    current_dict[pop_number] -= 1
    return pop_number


if __name__ == "__main__":
    for _ in range(int(input())):
        min_heap = []
        max_heap = []
        min_heap_dict = {}
        max_heap_dict = {}
        current_dict = {}
        current_values_count=0

        for _ in range(int(input())):
            line = input().split()
            command = line[0]
            number = int(line[1])
            if command == "I":
                if number in current_dict:
                    current_dict[number] += 1
                    max_heap_dict[number] += 1
                    min_heap_dict[number] += 1
                else:
                    current_dict[number] = 1
                    max_heap_dict[number] = 1
                    min_heap_dict[number] = 1
                heappush(min_heap, number)
                heappush(max_heap, -number)
                current_values_count+=1
            else:
                if current_values_count==0:
                    continue
                if number == -1:
                    pop(min_heap, min_heap_dict, current_dict, 1)
                elif number == 1:
                    pop(max_heap, max_heap_dict, current_dict, -1)
                current_values_count-=1

        if current_values_count==0:
            print("EMPTY")
        elif current_values_count==1:
            number = pop(max_heap, max_heap_dict, current_dict, -1)
            print(number, number)
        else:
            print(pop(max_heap, max_heap_dict, current_dict, -1), end=" ")
            print(pop(min_heap, min_heap_dict, current_dict, 1))