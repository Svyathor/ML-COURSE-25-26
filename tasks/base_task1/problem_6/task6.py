def check(x: str, file: str):
    words = x.split()
    word_count = {}

    for word in words:
        word_lower = word.lower()
        word_count[word_lower] = word_count.get(word_lower, 0) + 1

    sorted_words = sorted(word_count.items())

    with open(file, 'w') as f:
        for word, count in sorted_words:
            f.write(f"{word} {count}\n")

