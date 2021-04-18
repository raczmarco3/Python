

def binary(num):
    maradek = ""
    while(num > 0):   
        maradek = maradek + str(num % 2)             
        num = num // 2
    return maradek[::-1]

def main():
    print(binary(13))

#############################################################################

if __name__ == "__main__":
    main()