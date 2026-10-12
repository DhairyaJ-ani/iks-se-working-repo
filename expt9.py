import pandas as pd

# Sanskrit Digital Dictionary 

sanskrit_dict = {
    "गच्छति": {
        "Transliteration": "gacchati",
        "Meaning": "Goes",
        "Root (Dhatu)": "गम् (gam)",
        "Grammar": "Verb"
    },
    "ज्ञानम्": {
        "Transliteration": "jñānam",
        "Meaning": "Knowledge",
        "Root (Dhatu)": "ज्ञा (jñā)",
        "Grammar": "Noun, Neuter"
    },
    "सूर्यः": {
        "Transliteration": "sūryaḥ",
        "Meaning": "Sun",
        "Root (Dhatu)": "सूर् (sūr)",
        "Grammar": "Noun, Masculine"
    },
    "वृक्षः": {
        "Transliteration": "vṛkṣaḥ",
        "Meaning": "Tree",
        "Root (Dhatu)": "वृक्ष (vṛkṣa)",
        "Grammar": "Noun, Masculine"
    },
    "मित्रम्": {
        "Transliteration": "mitram",
        "Meaning": "Friend",
        "Root (Dhatu)": "मि (mi)",
        "Grammar": "Noun, Neuter"
    },
    "विद्यालयः": {
        "Transliteration": "vidyālayaḥ",
        "Meaning": "School",
        "Root (Dhatu)": "विद्या (vidyā)",
        "Grammar": "Noun, Masculine"
    },
    "लिखति": {
        "Transliteration": "likhati",
        "Meaning": "Writes",
        "Root (Dhatu)": "लिख् (likh)",
        "Grammar": "Verb"
    },
    "पठति": {
        "Transliteration": "paṭhati",
        "Meaning": "Reads",
        "Root (Dhatu)": "पठ् (paṭh)",
        "Grammar": "Verb"
    },
    "जलम्": {
        "Transliteration": "jalam",
        "Meaning": "Water",
        "Root (Dhatu)": "जल (jala)",
        "Grammar": "Noun, Neuter"
    },
    "गजः": {
        "Transliteration": "gajaḥ",
        "Meaning": "Elephant",
        "Root (Dhatu)": "गज (gaja)",
        "Grammar": "Noun, Masculine"
    },
    "पुस्तकम्": {
        "Transliteration": "pustakam",
        "Meaning": "Book",
        "Root (Dhatu)": "पुस्तक (pustaka)",
        "Grammar": "Noun, Neuter"
    },
    "गुरुः": {
        "Transliteration": "guruḥ",
        "Meaning": "Teacher",
        "Root (Dhatu)": "गुरु (guru)",
        "Grammar": "Noun, Masculine"
    },
    "बालकः": {
        "Transliteration": "bālakaḥ",
        "Meaning": "Boy",
        "Root (Dhatu)": "बाल (bāla)",
        "Grammar": "Noun, Masculine"
    },
    "बालिका": {
        "Transliteration": "bālikā",
        "Meaning": "Girl",
        "Root (Dhatu)": "बाल (bāla)",
        "Grammar": "Noun, Feminine"
    },
    "फलम्": {
        "Transliteration": "phalam",
        "Meaning": "Fruit",
        "Root (Dhatu)": "फल (phala)",
        "Grammar": "Noun, Neuter"
    },
    "गृहम्": {
        "Transliteration": "gṛham",
        "Meaning": "House",
        "Root (Dhatu)": "गृह (gṛha)",
        "Grammar": "Noun, Neuter"
    },
    "नदी": {
        "Transliteration": "nadī",
        "Meaning": "River",
        "Root (Dhatu)": "नद् (nad)",
        "Grammar": "Noun, Feminine"
    },
    "चन्द्रः": {
        "Transliteration": "candraḥ",
        "Meaning": "Moon",
        "Root (Dhatu)": "चन्द् (cand)",
        "Grammar": "Noun, Masculine"
    },
    "अग्निः": {
        "Transliteration": "agniḥ",
        "Meaning": "Fire",
        "Root (Dhatu)": "अग् (ag)",
        "Grammar": "Noun, Masculine"
    },
    "भवति": {
        "Transliteration": "bhavati",
        "Meaning": "Becomes / Is",
        "Root (Dhatu)": "भू (bhū)",
        "Grammar": "Verb"
    }
}

print("===== Sanskrit Digital Dictionary =====")
print("Type 'exit' to quit.\n")

while True:
    word = input("Enter a Sanskrit word: ")

    if word.lower() == "exit":
        print("Thank you for using the Sanskrit Digital Dictionary.")
        break

    if word in sanskrit_dict:
        print("\nWord Analysis")
        print("-" * 30)
        print("Word:", word)

        df = pd.DataFrame([sanskrit_dict[word]])
        print(df.to_string(index=False))
    else:
        print("Word Not present in dict..")

    print()