#       1ª QUESTÃO      #

from sys import stdin

def main():
    number = stdin.readlines().split("\n")
    print (number)
    new_list = list(filter(lambda x: x != '%', number))
    even_counter = 0
    for i in new_list:
        m = str(new_list[0::2]).replace("'", "").replace('[', '').replace(']', '').split(',')
        even_counter += 1
    print (m)


if __name__ == '__main__':
    main()