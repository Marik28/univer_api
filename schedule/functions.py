def transliterate(russian_text: str) -> str:
    legend = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'e',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'sch',
        'ъ': "'",
        'ы': 'y',
        'ь': "'",
        'э': 'e',
        'ю': 'yu',
        'я': 'ya',
    }
    transliterated_text = []
    for char in russian_text:
        if char.lower() in legend:
            transliterated_char = legend[char.lower()]
            if char.isupper():
                transliterated_char = transliterated_char.capitalize()
            transliterated_text.append(transliterated_char)
        else:
            transliterated_text.append(char)
    return ''.join(transliterated_text)