# ##############################[Character Maps]#####################################
def gloss(input_text):
    character_map = {
        "A": "ᴀ",
        "B": "ʙ",
        "C": "ᴄ",
        "D": "ᴅ",
        "E": "ᴇ",
        "F": "ғ",
        "G": "ɢ",
        "H": "ʜ",
        "I": "ɪ",
        "J": "ᴊ",
        "K": "ᴋ",
        "L": "ʟ",
        "M": "ᴍ",
        "N": "ɴ",
        "O": "ᴏ",
        "P": "ᴘ",
        "Q": "ǫ",
        "R": "ʀ",
        "S": "s",
        "T": "ᴛ",
        "U": "ᴜ",
        "V": "ᴠ",
        "W": "ᴡ",
        "X": "x",
        "Y": "ʏ",
        "Z": "ᴢ",
    }

    converted_text = ""
    for char in input_text:
        if char in character_map:
            converted_text += character_map[char]
        else:
            converted_text += char

    return converted_text


def latex(input_text):
    character_map = {
        "A": r"\textsc{a}",
        "B": r"\textsc{b}",
        "C": r"\textsc{c}",
        "D": r"\textsc{d}",
        "E": r"\textsc{e}",
        "F": r"\textsc{f}",
        "G": r"\textsc{g}",
        "H": r"\textsc{h}",
        "I": r"\textsc{i}",
        "J": r"\textsc{j}",
        "K": r"\textsc{k}",
        "L": r"\textsc{l}",
        "M": r"\textsc{m}",
        "N": r"\textsc{n}",
        "O": r"\textsc{o}",
        "P": r"\textsc{p}",
        "Q": r"\textsc{q}",
        "R": r"\textsc{r}",
        "S": r"\textsc{s}",
        "T": r"\textsc{t}",
        "U": r"\textsc{u}",
        "V": r"\textsc{v}",
        "W": r"\textsc{w}",
        "X": r"\textsc{x}",
        "Y": r"\textsc{y}",
        "Z": r"\textsc{z}",
        "Ø": r"\textsc{ø}",
    }

    converted_text = ""
    for char in input_text:
        if char in character_map:
            converted_text += character_map[char]
        else:
            converted_text += char

    return converted_text


def learn(input_text):
    word_map = {
        "PLURAL": "ᴘʟ",
        "ACCUSATIVE": "ᴀᴄᴄ",
        "GNOMIC": "ɢɴᴏ",
        "1STPERSON": "1sɢ",
    }

    words_and_markers = input_text.split()  # Split the gloss by spaces
    converted_words_and_markers = []

    for item in words_and_markers:
        components = item.split("-")  # Split each item by hyphens
        converted_components = []
        for component in components:
            if component in word_map:
                converted_components.append(word_map[component])
            else:
                converted_components.append(component)
        converted_words_and_markers.append("-".join(converted_components))

    return " ".join(converted_words_and_markers)


Choice = input(
    "Would you like your output to be generated for typesetting in LaTeX or in Latin characters? "
)

if Choice not in ["latex", "latin", "learn"]:
    print("Invalid choice. Please choose 'LaTeX' or 'Latin'.")

if Choice == "latex":
    GlossInput = input(
        "Type in your gloss. Everything should be in uppercase letters except for root words: "
    )
    output_text = latex(GlossInput)
    Source = input("Please provide the parsed text of the source language: ")
    Translation = input("Finally, please provide the translation of the sentence: ")

    print(
        "------[Here is your gloss. Copy and paste this into your TeX editor using the {expex} package]------"
    )

    print(r"\ex")
    print(r"\begingl")
    print(r"\gla " + Source + "//")
    print(r"\glb " + output_text + "//")
    print(r"\glft " + Translation + "//")
    print(r"\endgl")
    print(r"\xe")

if Choice == "latin":
    GlossInput = input(
        "Type in your gloss. Everything should be in uppercase letters except for root words: "
    )
    print("------[Here is your gloss]------")
    output_text = gloss(GlossInput)
    print(output_text)

if Choice == "learn":
    GlossInput = input(
        "Type in your gloss. Everything should be in uppercase letters except for root words: "
    )
    print("------[Here is your gloss]------")
    output_text = learn(GlossInput)
    print(output_text)
