import json5


def text_analysis(text, maxlen, forbidden_words):
    result = {}
    result.update([('length', len(text))])

    result.update([('pure_length',
                    len(''.join(text.split()))
                        )])

    result.update([('origin_text', text)])

    pure_text = []
    for word in text.split():
        if word in forbidden_words:
            pure_text.append('***')
        else:
            pure_text.append(word)
    result.update([('pure_text', ' '.join(pure_text))])

    pure_short_text = ''
    if len(text) > maxlen:
        pure_short_text = text[:maxlen] + '...'
    else:
        pure_short_text = text
    result.update([('pure_short_text', pure_short_text)])

    with open('result.json', 'w') as json:
        json5.dump(result, json)


text_i = input()
maxlen_i = int(input())
forbidden_words_i = input().split()
text_analysis(text_i, maxlen_i, forbidden_words_i)
