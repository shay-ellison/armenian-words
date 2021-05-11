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
    'ու': "u',
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


TEST_BANK = [
    'անկյուն', 'մրջյուն', 'խնձոր', 'կամար', 'բազուկ', 'բանակ', 'երեխա', 'պայուսակ', 
    'գնդակ', 'նվագախումբ', 'ավազան', 'զամբյուղ', 'բաղնիք', 'մահճակալ', 'մեղու', 'զանգ', 
    'հատապտուղ', 'թռչուն', 'բերան', 'տախտակ', 'նավակ', 'ոսկոր', 'գիրք', 'սկուտեղ', 'շիշ', 
    'տուփ', 'տղա', 'ուղեղ', 'արգելակ', 'ճյուղ', 'աղյուս', 'կամուրջ', 'խոզանակ', 'դույլ', 'լամպ', 'կոճակ', 
    'տորթ', 'տեսախցիկ', 'քարտ', 'սայլ', 'կառք', 'կատու', 'շղթա', 'պանիր', 'կրծքավանդակ', 'կզակ', 'եկեղեցի', 'շրջան', 
    'ժամացույց', 'ամպ', 'վերարկու', 'մանյակ', 'սանր', 'լար', 'կով', 'բաժակ', 'վարագույր', 'բարձ', 'շուն', 'դուռ', 
    'արտահոսք', 'գզրոց', 'զգեստ', 'կաթիլ', 'ականջ', 'ձու', 'շարժիչ', 'աչք', 'դեմք', 'ֆերմա', 'փետուր', 'մատ', 
    'ձուկ', 'դրոշ', 'հատակ', 'ճանճ', 'ոտք', 'պատառաքաղ', 'թռչուն', 'շրջանակ', 'պարտեզ', 'աղջիկ', 'ձեռնոց', 
    'այծ', 'ատրճանակ', 'մազեր', 'մուրճ', 'ձեռք', 'գլխարկ'
]


def main():
    def tryword(word):
        print(word + ":", romanize(word))

    tryword("հաշիվ")
    tryword("հասկանում")
    tryword("ո")
    tryword("ու")
    tryword("ոո")
    tryword("ևև")
    tryword("եե")

    for word in TEST_BANK:
        tryword(word)

if __name__ == '__main__':
    main()    
