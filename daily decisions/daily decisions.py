while True:
    print ("daily desicions)
    print ("")
    print ("je gaat gamen, maar wel spel speel je?")
    print ("")
    print ("A, league of legends")
    print ("B, rocket league")
    print ("C, rust")
    print ("D, dark souls 3")
    print ("E, lego star wars voor de wii")

    scriptinput = input()
    if scriptinput == "a" or scriptinput == "A":
        print ("dat is wel een beetje treurig je speelt waarschijnlijk yasuo")
        script = True    

    elif scriptinput == "b" or scriptinput == "B"   scriptinput == "d" or scriptinput == "D":
        print ("beetje matig maar niet zo erg als league of legends")
    
    elif scriptinput == "c" or scriptinput == "C":
        print ("")

    print ("ik werk in de supermarkt")
    print ("in welke supermarkt denk jij dat ik werk")
    print ("A, albert heijn")
    print ("B, vomar")
    print ("C, dirk")
    print ("D, jumbo")

    scriptinput = input()
    if scriptinput == "b" or scriptinput == "B":
        print ("ja ik ben 16 jaar oud")
        script = True    

    elif scriptinput == "c" or scriptinput == "C" or scriptinput == "a" or scriptinput == "A" or scriptinput == "d" or scriptinput == "D":
        print ("fout natwoord ik ben 16 jaar oud")

        print("wil dit script herstarten? Y/N")

    scriptinput = input()
    if scriptinput == "y" or scriptinput == "Y":
        print ("het script word gerestart")
        script = True    

    elif scriptinput == "n" or scriptinput == "N":
        print ("thanks for running")
        print ("")
        exit()