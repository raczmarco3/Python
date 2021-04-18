

def test(s):
    s2 = ""
    m = []
    for i in s:
        if i == "(" or i == ")" or i == "{" or i == "}" or i == "[" or i == "]":
            s2 = s2 + i

    if s2[0] == ")" or s2[0] == "}" or s2 == "]":
        return False
    elif len(s2) % 2 != 0:
        return False

    n = "({["

    for i in s2:
        if len(m) == 0:
            m.append(i)
        else:
            if i in n:
                m.append(i) 
            else:
                x = m.pop()
                if i == ")" and (x == "{"  or x == "["):
                    return False
                elif i == "}" and (x == "("  or x == "["):
                    return False
                elif i == "]" and (x == "{"  or x == "("):
                    return False    
    return True



def main():
    print(test("((5+3)*2+1)") == True)
    print(test("{[(3+1)+2]+}") == True)
    print(test("(3+{1-1)}") == False)
    print(test("[1+1]+(2*2)-{3/3}") == True)
    print(test("(({[(((1)-2)+3)-3]/3}-3)") == False)


#############################################################################

if __name__ == '__main__':
    main()