n = int(input())
h = {}
for _ in range(n):
    commands = list(input().split())
    if commands[0] == "add":
        h[commands[1]] = commands[2]
    elif commands[0] == "find":
        if commands[1] in h:
            print(h[commands[1]])
        else:
            print("None")
    else:
        h.pop(commands[1])