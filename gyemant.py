
def gyemant(magassag):
    
    if(magassag % 2 != 1):
        print("Csak páratlan szám lehet a magasság!")
    else:        
        i = 1
        darab = 1
        nemerteel = True
        while(i <= magassag):
            csillag = ""
            j = 0
            while(j < darab):
                csillag = csillag + "*"
                j += 1
            i += 1
            if(darab == magassag):
                nemerteel = False

            if(nemerteel):
                darab += 2
            else:
                darab -= 2

            print(csillag.center(magassag)) 
    
   
def main():
    gyemant(3)

#############################################################################

if __name__ == "__main__":
    main()