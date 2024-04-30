from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    Doc
)


def get_lemmas(text):
    """
    Функция для получения лемм из текста с использованием библиотеки Natasha.

    Ссылка на библиотеку: https://github.com/natasha/natasha
    """
    segmenter = Segmenter()
    morph_vocab = MorphVocab()

    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)
    syntax_parser = NewsSyntaxParser(emb)

    doc = Doc(text)

    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)

    for token in doc.tokens:
        token.lemmatize(morph_vocab)

    return [_.lemma for _ in doc.tokens]


def count_words(text):
    """
    Подсчет частоты слов в тексте
    """
    lemmas = get_lemmas(text)

    word_count = {}

    for lemma in lemmas:
        if not lemma.isalpha():
            continue
        if lemma in word_count:
            word_count[lemma] += 1
        else:
            word_count[lemma] = 1

    word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    result = ''
    for word, count in word_count:
        result += f'{word}: {count}\n'

    return result


def remove_extra_spaces(text):
    text = ' '.join(text.split())

    punctuation = ",.!?;:()<>\"\'"

    for char in punctuation:
        text = text.replace(' ' + char, char)
    return text

def to_lemma(text):
    """
    Приведет каждое слово в тексте к лемме
    """
    lemmas = get_lemmas(text)
    return remove_extra_spaces(' '.join(lemmas))

