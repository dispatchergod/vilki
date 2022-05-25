from Calculator import Calculator
from Parcer import Parser
from re import search


uri_1 = "https://www.marathonbet.es/su/popular/Tennis+-+2398"
uri_2 = "https://m.retiva-bet777.com/line/Tennis/"

parser_1 = Parser(uri_1)
res_1 = parser_1.create_dict()
parser_2 = Parser(uri_2)
res_2 = parser_2.create_dict()

print("Marathon: {}" .format(len(parser_1.create_dict())),
      "-----------------------",
      "Retiva: {}" .format(len(parser_2.create_dict())))

for i in res_1:
    arr = i.split(".")
    for j in res_2:
        if search(arr[0], j):
            calc = Calculator(float(res_1[i][0]), float(res_2[j][1]))
            res = calc.raschet_vilki()

            if float(res[2].split(" ")[2]) < 0:
                break
            print("Пара: ", i, "-----", j)

            print(res[0] + "\n" + res[1] + "\n" + res[2])
            break
