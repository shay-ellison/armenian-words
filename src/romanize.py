import csv
import os
import sys
from typing import List

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

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SRC_DIR)

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


def romanize_text_file(filepath: str, save=False):
    """Romanize the Armenian words in a words csv file (eng, arm, cat)"""
    words = {}

    # Read in the Armenian words
    armenian_words = []
    romanized_words = []

    with open(filepath, 'r', encoding="utf8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for line in reader:
            eng_word = line[0].strip().lower()
            arm_word = line[1].strip().lower()
            category = line[2]
            armenian_words.append(arm_word)
            romanized_word = romanize(arm_word)
            romanized_words.append(romanized_word)
            words[arm_word] = (eng_word, romanized_word)

    if save:
        path_to, filename = os.path.split(filepath)
        filename, extension = os.path.splitext(filename)

        # Save out the Armenian words
        out_filename = "armenian_words.txt"
        out_filepath = os.path.join(path_to, out_filename)
        with open(out_filepath, 'w', encoding='utf-8') as out_file:
            out_file.writelines(word + '\n' for word in armenian_words)


        out_filename = "romanized_words.txt"
        out_filepath = os.path.join(path_to, out_filename)
        with open(out_filepath, 'w', encoding='utf-8') as out_file:
            out_file.writelines(word + '\n' for word in romanized_words)

        # Write a new CSV with everything
        out_filename = "eng_arm_rom.csv"
        with open(out_filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ENGLISH', 'ARMENIAN', 'ROMANIZED'])
            for arm_word, other_words in words.items():
                eng_word, romanized_word = other_words
                # eng, arm, romanized
                writer.writerow([eng_word, arm_word, romanized_word])

    return romanized_words
 
def main():

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "words.txt"
    file_path = os.path.join(PROJECT_DIR, filename)
    # clean_words_file(file_path, save=True)
    # print("=== Cleaned Words File ===")
    romanize_text_file(file_path, save=True)
    print("=== Romanized Words File ===")


if __name__ == '__main__':
    main()
