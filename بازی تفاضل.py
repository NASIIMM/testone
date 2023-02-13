def game(number):
    if int(number[1])>int(number[0]):
        print(int(number[1])-int(number[0]))
    else :
        print(int(number[0])-int(number[1]))
game(input())