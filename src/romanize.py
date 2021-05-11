import os

LOWER_MAPPING = {
    'ա': 'a',
    'բ': 'b',
    'գ': 'g',
    'դ': 'd',
    'ե': ('ye', 'e'),
    'զ': 'z',
    'է': 'e',
    'ը': 'uh',
    'թ': "t'",
    'ժ': 'zh',
    'ի': 'i',
    'լ': 'l',
    'խ': 'kh',
    'ծ': 'ts',
    'կ': 'k',
    'հ': 'h',
    'ձ': 'dz',
    'ղ': 'gh',
    'ճ': 'ch',
    'մ': 'm',
    'յ': 'y',
    'ն': 'n',
    'շ': 'sh',
    'ո': ('vo', 'o'),
    'չ': 'ch',
    'պ': 'p',
    'ջ': 'j',
    'ռ': 'rr',
    'ս': 's',
    'վ': 'v',
    'տ': 't',
    'ր': 'r',
    'ց': "ts'",
    'փ': "p'",
    'ք': "k'",
    'օ': 'o',
    'ֆ': 'f',
    'և': ('yev', 'ev'),
}

# special case these
# 'ՈՒ/ու': 'u',
# 'և/և': 'yev/ev',   # ord() /1415


def romanize(armenian_word: str) -> str:
    """Romanize a lower cased Armenian word"""

    # special case
    # 'ՈՒ/ու': 'u',
    new_word = []
    prev = None
    for i, char in enumerate(armenian_word):
        #  Handle ու case, process either prev ո or current ու
        if prev == 'ո':
            if char == 'ւ':
                new_word.append('u')
            else:
                mapped = LOWER_MAPPING[prev]
                if i - 1 == 0:
                    new_word.append(mapped[0])
                else:
                    new_word.append(mapped[1])
        
        # Process all other chars, including if prev ո but no current ու
        if char not in ['ո', 'ւ']:   
            mapped = LOWER_MAPPING[char]    
            if type(mapped) == tuple:
                if i == 0:
                    new_word.append(mapped[0])
                else:
                    new_word.append(mapped[1])
            else:     
                new_word.append(mapped)

        prev = char

    if prev == 'ո':  # reach end of string but wasn't a ու|u
        mapped = LOWER_MAPPING[prev]
        if i == 0:
            new_word.append(mapped[0])
        else:
            new_word.append(mapped[1])        

    return ''.join(new_word)

def romanize_text_file(file_path):
    with open(file_path, encoding="utf8") as f:
        print("FILE: ", file_path)
        print("_________________")
        words = f.readlines()
    for word in words:
        word = word.strip()
        print(word + ": " + romanize(word))
        print('------------')
        
def main():
    for filename in os.listdir('armenian_lists'):
        if filename.endswith(".txt"):
            file_path = f"armenian_lists\{filename}"
            romanize_text_file(file_path)

if __name__ == '__main__':
    main()    
