import unittest
from unittest.result import TestResult

from romanize import romanize

class TestRomanize(unittest.TestCase):

    def test_test_bank(self):
        TEST_BANK_ARM = [
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

        TEST_BANK_ROMAN = [
            'ankyun', 'mrjyun', 'khndzor', 'kamar', 'bazuk', 'banak', 'yerekha', 'payusak', 
            'gndak', 'nvagakhumb', 'avazan', 'zambyugh', 'baghnik\'', 'mahchakal', 'meghu', 'zang', 
            'hataptugh','t\'rrchun', 'beran', 'takhtak', 'navak', 'voskor', 'girk\'', 'skutegh', 'shish', 
            'tup\'', 'tgha', 'ughegh', 'argelak', 'chyugh', 'aghyus', 'kamurj', 'khozanak', 'duyl', 'lamp', 'kochak',
            'tort\'', 'tesakhts\'ik', 'k\'art', 'sayl', 'karrk\'', 'katu', 'shght\'a', 'panir', 'krtsk\'avandak', 'kzak', 'yekeghets\'i', 'shrjan',
            'zhamats\'uyts\'', 'amp', 'verarku', 'manyak', 'sanr', 'lar', 'kov', 'bazhak', 'varaguyr', 'bardz', 'shun', 'durr',
            'artahosk\'', 'gzrots\'', 'zgest', 'kat\'il', 'akanj', 'dzu', 'sharzhich', 'achk\'', 'demk\'', 'ferma', 'p\'etur', 'mat',
            'dzuk', 'drosh', 'hatak', 'chanch', 'votk\'', 'patarrak\'agh', 't\'rrchun', 'shrjanak', 'partez', 'aghjik', 'dzerrnots\'',
            'ayts', 'atrchanak', 'mazer', 'murch', 'dzerrk\'', 'glkhark'
        ]
        i = 0
        while i < len(TEST_BANK_ARM):
            assert(romanize(TEST_BANK_ARM[i]), TEST_BANK_ROMAN[i])
            print("Correctly romanized " + TEST_BANK_ARM[i] + " ---> "+ TEST_BANK_ROMAN[i])
            i += 1


    def test_corner_cases(self):
        assert(romanize('հաշիվ'), 'hashiv')
        assert(romanize('հասկանում'), 'haskanum')
        assert(romanize('ո'), 'vo')
        assert(romanize('ու'), 'u')
        assert(romanize('ոո'), 'voo')
        assert(romanize('ևև'), 'yevev')
        assert(romanize('եե'), 'yee')

if __name__ == '__main__':
    unittest.main()