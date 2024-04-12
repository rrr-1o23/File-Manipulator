# def main():

'''
追加したい機能:
duplicate-contents -> 最後の引数が数字に変換可能か検証するvalidatorの作成 済

最初のファイル読み込み時に, ファイルを上書き可能に, もしくはそのまま -> 処理に移る

ファイルがディレクトリに存在するか検証するvalidator
(ファイル・ディレクトリの存在確認 : os.path.exists(./hogehoge...) )
'''

def main():
    s_divisionList = get_command_argument()

    # コマンドと引数にエラーがあれば再入力
    while(validator(s_divisionList) == False):
        print("\nError : There is a mistake in the command and arguments.\n")
        s_divisionList = get_command_argument()


    command = s_divisionList[0]

    if (command == "reverse"):
        reverse(s_divisionList)
    
    if (command == "copy"):
        copy(s_divisionList)
    
    if (command == "duplicate-contents"):
        duplicate_contents(s_divisionList)

    if (command == "replace-string"):
        replace_string(s_divisionList)


# コマンドと引数をリストに格納
def get_command_argument():

    print("Please enter the command.")

    s = input() + " "

    space_pos = [i for i, x in enumerate(s) if x == ' '] # スペースのインデックスを取得

    # print(space_pos)

    s_division = [] # 入力からのコマンドと引数を格納

    start_pos = 0
    for i in range(len(space_pos)):

       s_division.append(s[start_pos:space_pos[i]])
       # スタートポジションの移動
       start_pos = space_pos[i]+1 

    # print("s_division :", s_division)

    return s_division

# コマンドの綴りと引数の数が正しいか確認
def validator(s_divisionList):
    listLen = len(s_divisionList)
    command = s_divisionList[0]

    if (command == "reverse" and listLen == 3):
        return True
    
    elif (command == "copy" and listLen == 3):
        return True
    
    elif (command == "duplicate-contents" and listLen == 3 and isint(s_divisionList)):
        return True
    
    elif (command == "replace-string" and listLen == 4):
        return True
    
    else:
        return False

# 以下各コマンド(reverse, copy, duplicate-contents, replace-string)の処理

def reverse(s_divisionList):

    inputpath = s_divisionList[1]
    outputpath = s_divisionList[2]
    contents = ''

    with open(inputpath) as f:
        contents = f.read()

    # print("\ncontents:", contents, "\n")

    contents = contents[::-1] # ファイルの内容を反転

    with open(outputpath, 'w') as f:
        f.write(contents)


def copy(s_divisionList):
    inputpath = s_divisionList[1]
    outputpath = s_divisionList[2]

    with open(inputpath) as f:
        contents = f.read()

    # ファイルの内容をそのままコピー
    with open(outputpath, 'w') as f:
        f.write(contents)


def duplicate_contents(s_divisionList):
    inputpath = s_divisionList[1]
    n = int(s_divisionList[2])

    with open(inputpath) as f:
        contents = f.read()

    # 複製された内容をinputpathにn回複製
    with open(inputpath, 'w') as f:
        f.write(contents * n)


def replace_string(s_divisionList):
    inputpath = s_divisionList[1]
    needle = s_divisionList[2]
    newstring = s_divisionList[3]

    # print("needle: ", needle, "newstring: ", newstring)

    with open(inputpath) as f:
        contents = f.read()

    # ファイル内のneedleをnewstringへ置換
    with open(inputpath, 'w') as f:
        f.write(contents.replace(needle, newstring))

def isint(s_divisionList):
    n = s_divisionList[2]

    try:
        int(n, 10)
    except ValueError:
        return False
    else:
        return True


main()