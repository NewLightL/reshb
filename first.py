"""python question/first.py"""

def delimetr(a: int, base: int) -> int:
    char = ""
    while a // base != 0:
        char += str(a % base)
        a //= base
    char += str(a % base)
    return int(char[::-1])


a = int(input())
sum_el = 0
counter = 0
while a != 0:
    d = delimetr(a, 7)
    if d % 10 == 5:
        sum_el += a
        counter += 1
    a = int(input())

if counter > 0:
    print(int(sum_el / counter))
else:
    print("NO")