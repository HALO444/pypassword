import random
print()
h = r''' ____                                            _ 
|  _ \  __ _  ___  ___ __      __ ___   _ __  __| |
| |_) |/ _` |/ __|/ __|\ \ /\ / // _ \ | '__|/ _` |
|  __/| (_| |\__ \\__ \ \ V  V /| (_) || |  | (_| |
|_|    \__,_||___/|___/  \_/\_/  \___/ |_|   \__,_|
                                                   
  ____                                 _               
 / ___|  ___  _ __    ___  _ __  __ _ | |_  ___   _ __ 
| |  _  / _ \| '_ \  / _ \| '__|/ _` || __|/ _ \ | '__|
| |_| ||  __/| | | ||  __/| |  | (_| || |_| (_) || |   
 \____| \___||_| |_| \___||_|   \__,_| \__|\___/ |_|   
'''
print(h)
print()
number_of_chr = 12
#add or not
chr_sp = 1
chr_num = 1
chr_e = 1
chr_E = 1
chr_emoji = 0
#list
"""emojis = [
    "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇", "😉", "😌", "😍", "😘",
    "😎", "🥰", "😋", "😛", "😜", "🤪", "😝", "🤑", "🤗", "🤭", "🤫", "🤔", "🤐", "🤨",
    "😒", "😓", "😔", "😕", "🙃", "🤑", "😲", "☹️", "🙁", "😖", "😞", "😟", "😤", "😢",
    "😭", "😠", "😡", "🤬", "😷", "🤒", "🤕", "🤢", "🤮", "🤧", "🥵", "🥶", "🥴", "😵",
    "🤯", "🤠", "🥳", "😎", "🤓", "🧐", "🤩", "😏", "😈", "👿", "👹", "👺", "💀", "👻",
    "👽", "🤖", "💩", "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "😿", "😾", "🙈", "🙉",
    "🙊", "👶", "👦", "👧", "👨", "👩", "👴", "👵", "👨‍⚕️", "👩‍⚕️", "👨‍🎓", "👩‍🎓", "👨‍🏫", "👩‍🏫",
    "👨‍⚖️", "👩‍⚖️", "👨‍🌾", "👩‍🌾", "👨‍🍳", "👩‍🍳", "👨‍🔧", "👩‍🔧", "👨‍🏭", "👩‍🏭", "👨‍💼", "👩‍💼",
    "👨‍🔬", "👩‍🔬", "👨‍💻", "👩‍💻", "👨‍🎨", "👩‍🎨", "👨‍🚒", "👩‍🚒", "👨‍✈️", "👩‍✈️", "👨‍🚀", "👩‍🚀",
    "👩‍⚖️", "💂‍♀️", "💂‍♂️", "👮‍♀️", "👮‍♂️", "👷‍♀️", "👷‍♂️", "💼", "🤵", "👰", "👸", "🤴", "🧝‍♀️", "🧝‍♂️",
    "🧛‍♀️", "🧛‍♂️", "🧟‍♀️", "🧟‍♂️", "🧙‍♀️", "🧙‍♂️", "🧚‍♀️", "🧚‍♂️", "🧜‍♀️", "🧜‍♂️", "🧞‍♀️", "🧞‍♂️", "🧝‍♀️", "🧝‍♂️",
    "👯‍♀️", "👯‍♂️", "💃", "🕺", "🕴️", "🚶‍♀️", "🚶‍♂️", "🏃‍♀️", "🏃‍♂️", "💪", "👈", "👉", "☝️", "👆",
    "🖕", "👇", "✌️", "🤞", "🖖", "🤘", "🤙", "👌", "👍", "👎", "✊", "👊", "🤛", "🤜", "🤚",
    "👋", "🤟", "✍️", "👏", "👐", "🤲", "🙌", "🤝", "🙏", "💅", "👂", "👃", "👀", "👁️‍🗨️", "👅",
    "👄", "💋", "🧠", "👤", "👥", "🗣️", "🤔", "🤭", "🐶", "🐱", "🐭", "🐹", "🐰", "🦊",
    "🦝", "🐻", "🐼", "🦘", "🦡", "🐨", "🐯", "🦁", "🐮", "🐷", "🐽", "🐸", "🐵", "🙈",
    "🙉", "🙊", "🐒", "🐔", "🐧", "🐦", "🐤", "🐣", "🐥", "🦆", "🦢", "🦉", "🦚", "🦜",
    "🐸", "🐢", "🦎", "🐍", "🐲", "🐉", "🦕", "🦖", "🐳", "🐋", "🐬", "🦭", "🐟", "🐠",
    "🐡", "🦈", "🐙", "🦑", "🦞", "🦀", "🦐", "🦪", "🐚", "🦆", "🍏", "🍎", "🍐", "🍊",
    "🍋", "🍌", "🍉", "🍇", "🍓", "🍈", "🍒", "🍑", "🍍", "🥥", "🥝", "🍅", "🍆", "🥑",
    "🥦", "🥒", "🥕", "🌽", "🌶️", "🌶️", "🥬", "🥔", "🍠", "🥐", "🥯", "🍞", "🥖", "🥨",
    "🧀", "🍖", "🍗", "🥩", "🥓", "🍔", "🍟", "🍕", "🌭", "🥪", "🌮", "🌯", "🥙", "🍳",
    "🍲", "🥘", "🍿", "🍱", "🍘", "🍙", "🍚", "🍛", "🍜", "🍝", "🍠", "🍢", "🍣", "🍤",
    "🍥", "🍡", "🥟", "🥠", "🍦", "🍧", "🍨", "🍩", "🍪", "🎂", "🍰", "🧁", "🥧", "🍫",
    "🍬", "🍭", "🍮", "🍯", "🍼", "🥛", "☕", "🍵", "🍶", "🍾", "🍷", "🍸", "🍹", "🍺",
    "🍻", "🥂", "🥃", "🍽️", "🍴", "🥄"
]"""
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
simple_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?', '`', '~']


def number_ofchr():
  global number_of_chr
  number_of_chr = int(input('Enter Password lenth(least 12 characters ):'))
  if number_of_chr < 12:
    print('Give least 12 characters')
    number_ofchr()
  spchr()  
def spchr():
  print()
  sp_chr = input('Do you need special characters (e.g., !, @, #, $, %, etc.) [y/n] :')
  if sp_chr == 'y' or sp_chr == 'n' :
     global chr_sp
     if sp_chr == 'y':
       chr_sp = 1
       numchr()
     else:
       chr_sp = 0
       numchr()
  else:
    print('Unvalid input')
    spchr()
def numchr():
  print()
  num_chr = input(('Do you need Number characters (e.g., 1, 2,..,9 etc.) [y/n] :'))
  if num_chr == 'y' or num_chr == 'n' :
     global chr_num
     if num_chr == 'y':
       chr_num = 1
       echr()
     else:
       chr_num = 0
       echr()
  else:
    print('Unvalid input')
    num_chr()
def echr():
  print()
  e_chr = input(('Do you need simple letters  (e.g., a, b,..,z etc.) [y/n] :'))
  if e_chr == 'y' or e_chr == 'n' :
     global chr_e
     if e_chr == 'y':
       chr_e = 1
       Echr()
     else:
       chr_e = 0
       Echr()
  else:
    print('Unvalid input')
    echr()  
def Echr():
  print()
  E_chr = input(('Do you need Capital letters  (e.g., A, B,..,Z etc.) [y/n] :'))
  if E_chr == 'y' or E_chr == 'n' :
     global chr_E
     if E_chr == 'y':
       chr_E = 1
       check()
     else:
       chr_E = 0
       check()
  else:
    print('Unvalid input')
    Echr() 
"""def emojichr():
  print()
  emoji_chr = input(('Do you need Emojis  (e.g., 😎,😋,...,🐉 etc.) [y/n] :'))
  if emoji_chr == 'y' or emoji_chr == 'n' :
     global chr_emoji
     if emoji_chr == 'y':
       chr_emoji = 1
       check()
     else:
       chr_emoji = 0
       check()
  else:
    print('Unvalid input')
    emojichr() """
check_list=[]  
non_check_list = [] 
set_password_list = [] 
set = 0
non_set = 0
def check():
  print()
  global check_list
  if chr_sp == 1:
    check_list.append(1)
  if chr_num == 1:
    check_list.append(2)
  if chr_e == 1:
    check_list.append(3)
  if chr_E == 1:
    check_list.append(4)
  if chr_emoji == 1:
    check_list.append(5)
  global set
  global non_set
  set = number_of_chr // len(check_list)
  
  non_set = number_of_chr - set *len(check_list)
  x = 0
  
  while non_set != 0:
    non_check_list.append(check_list[0])
    non_set = non_set - 1
    
    x = x + 1
    
  create_set()   
password_set = []  
random_set_password_list = []  
password_10 = 20    
def create_set():
  global password_10
  while password_10 != 0 :
    password_10 = password_10 - 1
    global check_list
    loop = set
    global set_password_list
    global emojis
    global capital_letters
    global simple_letters
    global number_list
    global special_chars
    set_password_list = []
    while loop != 0 :
      for chr in check_list :
        if chr == 1:
         set_password_list.append(random.choice(special_chars))
        if chr == 2:
         set_password_list.append(random.choice(number_list))
        if chr == 3:
         set_password_list.append(random.choice(simple_letters))
        if chr == 4:
         set_password_list.append(random.choice(capital_letters))
        
        #if chr == 5:
        #emoji_choice = random.randint(0,353)
        #set_password_list.append(emojis[emoji_choice])
        
      loop = loop - 1  

    while non_check_list != []:
          if non_check_list[0] == 1:
            set_password_list.append(random.choice(special_chars))
          if non_check_list[0] == 2:
            set_password_list.append(random.choice(str(number_list)))
          if non_check_list[0] == 3:
            set_password_list.append(random.choice(simple_letters))
          if non_check_list[0] == 4:
            set_password_list.append(random.choice(capital_letters))
          break   
    
    lenth = len(set_password_list)
    global password_set
    password_set = []
    
    while len(password_set) != len(set_password_list):
      x = random.randint(0,lenth -1)
      if x not in password_set :
        password_set.append(x)

    global random_set_password_list  
    random_set_password_list = []   
    for random_num in password_set:
      str(random_num)
      random_set_password_list.append(set_password_list[random_num]) 
    print('-------------------------------------------------------------')
    print()
    print('    |-     ',end='')
    for number in random_set_password_list:
      print(number,end="")
    print()
     
  
  
  

   
  
number_ofchr()
