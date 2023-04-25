class StringUtility:    

    def __init__(self, string):
        self.string = string
        return None
    
    def __str__(self):
        return self.string
    
    def vowels(self):
        count = 0
        for i in range(len(self.string)):
            if self.string[i] == "a" or self.string[i] == "e" or self.string[i] == "i" or  self.string[i] == "o" or self.string[i] == "u":
                count = count + 1
        if count < 5:
            return str(count)
        if count >= 5:
            return "many"
    
    def bothEnds(self):
            if len(self.string) <= 2:
                return ""
            elif len(self.string) > 2:
                return self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
    
    def fixStart(self):
        if len(self.string) > 1:
            string = self.string[0]
            for i in range(1, len(self.string)):
                if self.string[i] == self.string[0]:
                    string = string + "*"
                else:
                    string = string + self.string[i]
            return string
        elif len(self.string) <= 1:
            return self.string
        
    def asciiSum(self):
        sum = 0
        for i in range(len(self.string)):
            sum = sum + ord(self.string[i])
        return int(sum)
    
    def cipher(self):
        string = ""
        for i in range(len(self.string)):
            if self.string[i].isalpha():
                letter = ord(self.string[i]) + len(self.string)
                if ord(self.string[i]) + len(self.string) > ord("z") and self.string[i].islower():
                    while (letter > ord("z")):
                        letter = letter - 26
                if ord(self.string[i]) + len(self.string) > ord("Z") and self.string[i].isupper():
                    while (letter > ord("Z")):
                        letter = letter - 26
                string = string + chr(letter)
            else:
                string = string + self.string[i]
        return string
