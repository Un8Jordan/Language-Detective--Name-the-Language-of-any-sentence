import math
from collections import Counter
#from samples import SAMPLES


# Step 1: Create character trigrams
def char_trigrams(text):
    text = " " + text.lower() + " "
    chunk = []

    for i in range(len(text) - 2):
        chunk = text[i:i + 3]

        if chunk.isalpha()or " " in chunk:
            chunk.append(chunk)

    return Counter(chunk)


# Step 2: Create language profiles
PROFILES={}

for language in SAMPLES:
    PROFILES[language] = char_trigrams(SAMPLES[language])
    

def rank_languages(text):
    mystery = char_trigrams(text)
    scores = {}

    for language in PROFILES:
        scores[language] = cosine(mystery, PROFILES[language])
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)


def detect(text):
    return rank_languages(text)

# Step 6: Guessing Game
CASE_FILEs = [
    ("The library is closed on Sundays.", "English"),
    ("La biblioteca está cerrada los domingos.", "Spanish"),
    ("La bibliothèque est fermée le dimanche.", "French"),
    ("Die Bibliothek ist sonntags geschlossen.", "German"),
    ("La biblioteca è chiusa la domenica.", "Italian"),
    ("A biblioteca está fechada aos domingos.", "Portuguese"),
    ("図書館は日曜日に閉まっています。", "Japanese"),
    ("图书馆在星期天关闭。", "Chinese"),
    ("Библиотека закрыта по воскресеньям.", "Russian"),
    ("المكتبة مغلقة أيام الأحد.", "Arabic"),
    ("The sky is blue.", "English"),
    ("La biblioteca está cerrada los domingos.", "Spanish"),
    ("Mera naam John hai.", "Hinglish"),
    ("मेरा नाम जॉन है।", "Hindi"),
    ("माझं नाव जॉन आहे.", "Marathi"),
    ("माझं नाव जॉन आहे.", "Marathi"),
    ("माझं नाव जॉन आहे.", "Marathi"),
]

you = 0
detective = 0

print("==========================================")
print("          LANGUAGE DETECTIVE              ")
print("==========================================")

for i, (text, answer) in enumerate(CASE_FILEs):
    print("\n Case", i, ":", text)
    guess = input("What language is this? ").strip().title()
