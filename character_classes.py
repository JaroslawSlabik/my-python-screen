
class Character:
    name = "null"
    char = []

    def __init__(self):
        self.char = [["#", "#", "#"],
                     ["#", "#", "#"],
                     ["#", "#", "#"],
                     ["#", "#", "#"],
                     ["#", "#", "#"],
                     ["#", "#", "#"]
                    ]
    #END __init__

    def get(self, number_line = 0, start_pos = 0, lenght = 3):
        var_string = ""
        for index in range(start_pos, lenght):
            var_string += self.char[number_line][index]
        return var_string
    #END get

#END Character

class Char_1(Character):
    def __init__(self):
        self.name = "1"
        self.char = [[" ", "#", " "],
                     ["#", "#", " "],
                     [" ", "#", " "],
                     [" ", "#", " "],
                     [" ", "#", " "],
                     ["#", "#", "#"]
                    ]
    #END __init__
#END Char_1

class Char_2(Character):
    def __init__(self):
        self.name = "2"
        self.char = [["#", "#", "#"],
                     ["#", " ", "#"],
                     [" ", " ", "#"],
                     [" ", "#", " "],
                     ["#", " ", " "],
                     ["#", "#", "#"]
                    ]
    #END __init__
#END Char_2

class Char_3(Character):
    def __init__(self):
        self.name = "3"
        self.char = [[" ", "#", " "],
                     ["#", " ", "#"],
                     [" ", "_", "#"],
                     [" ", " ", "#"],
                     ["#", " ", "#"],
                     [" ", "#", " "]
                    ]
    #END __init__
#END Char_3

class Char_4(Character):
    def __init__(self):
        self.name = "4"
        self.char = [[" ", " ", "#"],
                     [" ", "#", " "],
                     ["#", "#", "#"],
                     [" ", " ", "#"],
                     [" ", " ", "#"],
                     [" ", " ", "#"]
                    ]
    #END __init__
#END Char_4

class Char_5(Character):
    def __init__(self):
        self.name = "5"
        self.char = [["#", "#", "#"],
                     ["#", " ", " "],
                     ["#", "#", "#"],
                     [" ", " ", "#"],
                     [" ", " ", "#"],
                     ["#", "#", "#"]
                    ]
    #END __init__
#END Char_5

class Char_6(Character):
    def __init__(self):
        self.name = "6"
        self.char = [["#", "#", "\\"],
                     ["#", " ", " "],
                     ["#", "#", "#"],
                     ["#", " ", "#"],
                     ["#", " ", "#"],
                     ["#", "#", "#"]
                    ]
    #END __init__
#END Char_6

class Char_7(Character):
    def __init__(self):
        self.name = "7"
        self.char = [["#", "#", "#"],
                     [" ", " ", "#"],
                     [" ", "#", " "],
                     [" ", "#", " "],
                     [" ", "#", " "],
                     [" ", "#", " "]
                    ]
    #END __init__
#END Char_7

class Char_8(Character):
    def __init__(self):
        self.name = "8"
        self.char = [["#", "#", "#"],
                     ["#", " ", "#"],
                     ["#", "#", "#"],
                     ["#", " ", "#"],
                     ["#", " ", "#"],
                     ["#", "#", "#"]
                    ]
    #END __init__
#END Char_8

class Char_9(Character):
    def __init__(self):
        self.name = "9"
        self.char = [["#", "#", "#"],
                     ["#", " ", "#"],
                     ["#", "#", "#"],
                     [" ", " ", "#"],
                     [" ", " ", "#"],
                     ["#", "#", "#"]
                    ]
    #END __init__
#END Char_9

class Char_0(Character):
    def __init__(self):
        self.name = "0"
        self.char = [["#", "#", "#"],
                     ["#", " ", "#"],
                     ["#", "|", "#"],
                     ["#", "|", "#"],
                     ["#", " ", "#"],
                     ["#", "#", "#"]
                    ]
    #END __init__
#END Char_0

class Char_Minus(Character):
    def __init__(self):
        self.name = "-"
        self.char = [[" ", " ", " "],
                     [" ", " ", " "],
                     [" ", " ", " "],
                     ["-", "-", "-"],
                     [" ", " ", " "],
                     [" ", " ", " "]
                    ]
    #END __init__
#END Char_Minus










def buildCharacter(character_name):
    if character_name == "1":
        return Char_1()
    if character_name == "2":
        return Char_2()
    if character_name == "3":
        return Char_3()
    if character_name == "4":
        return Char_4()
    if character_name == "5":
        return Char_5()
    if character_name == "6":
        return Char_6()
    if character_name == "7":
        return Char_7()
    if character_name == "8":
        return Char_8()
    if character_name == "9":
        return Char_9()
    if character_name == "0":
        return Char_0()
    if character_name == "-":
        return Char_Minus()



    return Character()
#END buildCharacter

