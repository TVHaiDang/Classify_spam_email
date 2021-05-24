import re
date_pattern = []
phone_pattern = []
link_pattern = []
currency_pattern = []
emoticon_pattern = []

date_string = ' date '
phone_string = ' phone '
link_string = ' link '
currency_string = ' currency '
emoticon_string = ' emoticon '

# Regex for date
date_pattern.append(u'\d{1,2}/\d{1,2}/\d{2,4}')
date_pattern.append(u'\d{1,2}-\d{1,2}-\d{2,4}')
date_pattern.append(u'\+\d{1,2}:\d{1,4}')
date_pattern.append(u'\d{1,2}/\d{1,4}')
date_pattern.append(u'\d{1,2}-\d{1,4}')
date_pattern.append(u'\d{1,2}h\d{0,2}')
# Regex for phone
phone_pattern.append(u'\+\d{10,12}')
phone_pattern.append(u'\d{3,5}\.\d{3,4}\.\d{3,5}')
phone_pattern.append(u'\d{8,12}')
phone_pattern.append(u'1800\d{4}')
phone_pattern.append(u'195')
phone_pattern.append(u'900')
phone_pattern.append(u'1342')
phone_pattern.append(u'191')
phone_pattern.append(u'888')
phone_pattern.append(u'333')
phone_pattern.append(u'1414')
phone_pattern.append(u'1576')
phone_pattern.append(u'8170')
phone_pattern.append(u'9123')
phone_pattern.append(u'9118')
phone_pattern.append(u'266')
phone_pattern.append(u'153')
phone_pattern.append(u'199')
phone_pattern.append(u'9029')
phone_pattern.append(u'8049')
phone_pattern.append(u'1560')
phone_pattern.append(u'9191')
# Regex for link
link_pattern.append(u'www\..*')
link_pattern.append(u'http://.*')
# Regex for currency
currency_pattern.append(u'[0-9|\,\.]{3,}VND')
currency_pattern.append(u'[0-9|\.]{3,}VND')
currency_pattern.append(u'[0-9|\.]{3,}d')
currency_pattern.append(u'[0-9|\.]{3,}đ')
currency_pattern.append(u'[0-9|\.]{3,}tr')
currency_pattern.append(u'[0-9|\.]{3,}Tr')
currency_pattern.append(u'[0-9|\.]{3,}TR')
# Regex for emoticon
emoticon_pattern.append(u'o.O')
emoticon_pattern.append(u'O.o')
emoticon_pattern.append(u'\(y\)')
emoticon_pattern.append(u'\(Y\)')
emoticon_pattern.append(u':v')
emoticon_pattern.append(u':V')
emoticon_pattern.append(u':3')
emoticon_pattern.append(u'-_-')
emoticon_pattern.append(u'\^_\^')
emoticon_pattern.append(u'<3')
emoticon_pattern.append(u':-\*')
emoticon_pattern.append(u':\*')
emoticon_pattern.append(u":'\(")
emoticon_pattern.append(u':p ')
emoticon_pattern.append(u':P')
emoticon_pattern.append(u':d')
emoticon_pattern.append(u':D')
emoticon_pattern.append(u':-\?')
emoticon_pattern.append(u'>\.<')
emoticon_pattern.append(u'><')
emoticon_pattern.append(u':-\w ')
emoticon_pattern.append(u':\)\)')
emoticon_pattern.append(u';\)\)')
emoticon_pattern.append(u'=\)\)')
emoticon_pattern.append(u':-\)')
emoticon_pattern.append(u':\)')
emoticon_pattern.append(u':\]')
emoticon_pattern.append(u'=\)')
emoticon_pattern.append(u':-\(')
emoticon_pattern.append(u':\(')
emoticon_pattern.append(u':\[')
emoticon_pattern.append(u'=\(')

stop_list = ['.', ',', '/', '?', ';', ':', '&', '@', '!', '`', "'", '"', '>', '<', '*', '%', '#', '(', ')', '[', ']',
             '-', '_', '=', '+', '{', '}', '~', '$', '^', '*', '|', '\\']

def entity_tagging(corpus):
    corpus_new = []
    for line in corpus:
        sent = []
        for word in line.split():
            for date_pat in date_pattern:
                word = re.sub(date_pat, date_string, word)
            for currency_pat in currency_pattern:
                word = re.sub(currency_pat, currency_string, word)
            for phone_pat in phone_pattern:
                word = re.sub(phone_pat, phone_string, word)
            for link_pat in link_pattern:
                word = re.sub(link_pat, link_string, word)
            for emoticon_pat in emoticon_pattern:
                word = re.sub(emoticon_pat, emoticon_string, word)
            sent.append(word)
        sent = ' '.join(sent)
        for item in stop_list:
            sent = sent.replace(item, ' ')
        sent = sent.lower()
        sent = sent.split()
        for i in range(len(sent)):
            if sent[i].isdigit():
                sent[i] = 'number'
        corpus_new.append(' '.join(sent))
    return corpus_new