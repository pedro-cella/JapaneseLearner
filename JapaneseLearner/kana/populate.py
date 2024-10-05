from kana.models import Hiragana, Katakana

hiragana = [
    {'romaji': 'a', 'kana': 'あ'},
    {'romaji': 'i', 'kana': 'い'},
    {'romaji': 'u', 'kana': 'う'},
    {'romaji': 'e', 'kana': 'え'},
    {'romaji': 'o', 'kana': 'お'},
    # Ka-Ko
    {'romaji': 'ka', 'kana': 'か'},
    {'romaji': 'ki', 'kana': 'き'},
    {'romaji': 'ku', 'kana': 'く'},
    {'romaji': 'ke', 'kana': 'け'},
    {'romaji': 'ko', 'kana': 'こ'},
    # Sa-So
    {'romaji': 'sa', 'kana': 'さ'},
    {'romaji': 'shi', 'kana': 'し'},
    {'romaji': 'su', 'kana': 'す'},
    {'romaji': 'se', 'kana': 'せ'},
    {'romaji': 'so', 'kana': 'そ'},
    # Ta-To
    {'romaji': 'ta', 'kana': 'た'},
    {'romaji': 'chi', 'kana': 'ち'},
    {'romaji': 'tsu', 'kana': 'つ'},
    {'romaji': 'te', 'kana': 'て'},
    {'romaji': 'to', 'kana': 'と'},
    # Na-No
    {'romaji': 'na', 'kana': 'な'},
    {'romaji': 'ni', 'kana': 'に'},
    {'romaji': 'nu', 'kana': 'ぬ'},
    {'romaji': 'ne', 'kana': 'ね'},
    {'romaji': 'no', 'kana': 'の'},
    # Ha-Ho
    {'romaji': 'ha', 'kana': 'は'},
    {'romaji': 'hi', 'kana': 'ひ'},
    {'romaji': 'fu', 'kana': 'ふ'},
    {'romaji': 'he', 'kana': 'へ'},
    {'romaji': 'ho', 'kana': 'ほ'},
    # Ma-Mo
    {'romaji': 'ma', 'kana': 'ま'},
    {'romaji': 'mi', 'kana': 'み'},
    {'romaji': 'mu', 'kana': 'む'},
    {'romaji': 'me', 'kana': 'め'},
    {'romaji': 'mo', 'kana': 'も'},
    # Ya-Yu-Yo
    {'romaji': 'ya', 'kana': 'や'},
    {'romaji': 'yu', 'kana': 'ゆ'},
    {'romaji': 'yo', 'kana': 'よ'},
    # Ra-Ro
    {'romaji': 'ra', 'kana': 'ら'},
    {'romaji': 'ri', 'kana': 'り'},
    {'romaji': 'ru', 'kana': 'る'},
    {'romaji': 're', 'kana': 'れ'},
    {'romaji': 'ro', 'kana': 'ろ'},
    # Wa-N
    {'romaji': 'wa', 'kana': 'わ'},
    {'romaji': 'wo', 'kana': 'を'},
    {'romaji': 'n', 'kana': 'ん'},
]

katakana = [
    {'romaji': 'a', 'kana': 'ア'},
    {'romaji': 'i', 'kana': 'イ'},
    {'romaji': 'u', 'kana': 'ウ'},
    {'romaji': 'e', 'kana': 'エ'},
    {'romaji': 'o', 'kana': 'オ'},
    # Ka-Ko
    {'romaji': 'ka', 'kana': 'カ'},
    {'romaji': 'ki', 'kana': 'キ'},
    {'romaji': 'ku', 'kana': 'ク'},
    {'romaji': 'ke', 'kana': 'ケ'},
    {'romaji': 'ko', 'kana': 'コ'},
    # Sa-So
    {'romaji': 'sa', 'kana': 'サ'},
    {'romaji': 'shi', 'kana': 'シ'},
    {'romaji': 'su', 'kana': 'ス'},
    {'romaji': 'se', 'kana': 'セ'},
    {'romaji': 'so', 'kana': 'ソ'},
    # Ta-To
    {'romaji': 'ta', 'kana': 'タ'},
    {'romaji': 'chi', 'kana': 'チ'},
    {'romaji': 'tsu', 'kana': 'ツ'},
    {'romaji': 'te', 'kana': 'テ'},
    {'romaji': 'to', 'kana': 'ト'},
    # Na-No
    {'romaji': 'na', 'kana': 'ナ'},
    {'romaji': 'ni', 'kana': 'ニ'},
    {'romaji': 'nu', 'kana': 'ヌ'},
    {'romaji': 'ne', 'kana': 'ネ'},
    {'romaji': 'no', 'kana': 'ノ'},
    # Ha-Ho
    {'romaji': 'ha', 'kana': 'ハ'},
    {'romaji': 'hi', 'kana': 'ヒ'},
    {'romaji': 'fu', 'kana': 'フ'},
    {'romaji': 'he', 'kana': 'ヘ'},
    {'romaji': 'ho', 'kana': 'ホ'},
    # Ma-Mo
    {'romaji': 'ma', 'kana': 'マ'},
    {'romaji': 'mi', 'kana': 'ミ'},
    {'romaji': 'mu', 'kana': 'ム'},
    {'romaji': 'me', 'kana': 'メ'},
    {'romaji': 'mo', 'kana': 'モ'},
    # Ya-Yu-Yo
    {'romaji': 'ya', 'kana': 'ヤ'},
    {'romaji': 'yu', 'kana': 'ユ'},
    {'romaji': 'yo', 'kana': 'ヨ'},
    # Ra-Ro
    {'romaji': 'ra', 'kana': 'ラ'},
    {'romaji': 'ri', 'kana': 'リ'},
    {'romaji': 'ru', 'kana': 'ル'},
    {'romaji': 're', 'kana': 'レ'},
    {'romaji': 'ro', 'kana': 'ロ'},
    # Wa-N
    {'romaji': 'wa', 'kana': 'ワ'},
    {'romaji': 'wo', 'kana': 'ヲ'},
    {'romaji': 'n', 'kana': 'ン'},
]


def populate_database():    
    for h in hiragana:
        Hiragana.objects.create(**h)
        
    for k in katakana:
        Katakana.objects.create(**k)
        
if __name__ == '__main__':
    populate_database()