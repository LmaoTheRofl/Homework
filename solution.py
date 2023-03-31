#NikitaZharkovO3144
with open("input.txt", "r") as input_file:
    h = input_file.readlines()
    n =  int(h[0].replace('\n', ''))
    a = h[1].replace('\n', '').split()
    a = [int(i) for i in a]
    x = int(h[-1])
result = 0
for i in a[:len(a) - 1]:
    result = (result+i)*x
result+=a[-1]
output_file = open("output.txt", "w")
output_file.write(str(result))
output_file.flush()
output_file.close()
