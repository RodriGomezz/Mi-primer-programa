for i in range(1,101):
    output = ""
    if i % 3 == 0:
        output += 'fizz'
    if i % 5 == 0:
        output += 'buzz'
    if output == "":
        output = i
    print(output)