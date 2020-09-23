
def print_line(line_ch, num):
    for i in range(1, num+1):
        print(line_ch, end='')
    print("")

def gugu(dan):
    for i in range(1, 10):
        print(dan, " * ", i, " = ", dan*i)

# main 시작

print_line('=', 10)
gugu(2)

for i in range(3, 10):
    print_line('-', 20)
    gugu(i)

print_line('=', 10)
