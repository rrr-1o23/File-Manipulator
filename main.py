
import sys
import os

def main():

    manipulate = Manipulate()
    manipulate.execute()


class Manipulate:
    args = sys.argv

    def execute(self):
        helper = Helper()

        if (helper.validate() != True):
            print("\nError : You have entered the command and arguments incorrectly\n")

        elif (helper.isfile() != True):
            print("\n^^^^^^^^^^^^^^^^^^^^^^^^^\nThe file does not exist!!\n^^^^^^^^^^^^^^^^^^^^^^^^^\n")

        elif (self.args[1] == "reverse"):
            self.reverse()
            print("\n --------------------- \n| You have succeeded! |\n ---------------------")
            
        elif (self.args[1] == "copy"):
           self. copy()

        elif (self.args[1] == "duplicate-contents"):
            self.duplicate_contents()
            
        else:
            self.replace_string()


    # ---.py reverse inputpath outputpath
    def reverse(self):
        inputpath = self.args[2]
        outputpath = self.args[3]

        with open(inputpath) as f:
            contents = f.read()
        
        contents = contents[::-1]

        with open(outputpath, 'w') as f:
            f.write(contents)

    # ---.py copy inputpath outputpath
    def copy(self):
        inputpath = self.args[2]
        outputpath = self.arguments[3]

        with open(inputpath) as f:
            contents = f.read()

        with open(outputpath, 'w') as f:
            f.write(contents)

    # ---.py duplicate-contents inputpath n
    def duplicate_contents(self):
        inputpath = self.args[2]
        n = int(self.args[3])

        with open(inputpath) as f:
            contents = f.read()

        with open(inputpath, 'w') as f:
            f.write(contents * n)

    # ---.py replace-string inputpath needle newstring
    def replace_string(self):
        inputpath = self.args[2]
        target_s = self.arguments[3]
        newstring = self.arguments[4]

        with open(inputpath) as f:
            contents = f.read()

        with open(inputpath, 'w') as f:
            f.write(contents.replace(target_s, newstring))


class Helper:
    args = sys.argv
    
    argsLen = len(args) # 引数の数
    
    # コマンドと引数の確認
    def validate(self):
        if (len(sys.argv) == 1):
            return False
        elif (self.args[1] == "reverse" and self.argsLen == 4):
            return True
        elif (self.args[1] == "copy" and self.argsLen == 4):
            return True
        elif (self.args[1] == "duplicate-contents" and self.argsLen == 4 and self.isint()):
            return True
        elif (self.args[1] == "repalce-string" and self.argsLen == 5):
            return True
        else:
            return False

    def isint(self):
        n = self.args[3]

        try:
            int(n, 10)
        except ValueError:
            return False
        else:
            return True
    
    def isfile(self):
        inputpath = self.args[2]
        is_file = os.path.isfile(inputpath)

        if is_file:
            return True
        else:
            return False


main()