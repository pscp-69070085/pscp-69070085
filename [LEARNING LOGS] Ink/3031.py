"""INK"""
import math as m
def main():
    """main"""
    S, N = map(int, input().split())
    for _ in range(N):
        x,y = map(int, input().split())
        radius = m.sqrt((x)**2+y**2)
        time = ((radius**2)*(3.1416))/S
        print(m.ceil(time))

main()
