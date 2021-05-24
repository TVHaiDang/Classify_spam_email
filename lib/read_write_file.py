def read_file(path):
    with open(path, encoding='utf-8') as f:
        data = f.read().split('\n')
    return data


def write_file(path, corpus):
    with open(path, 'w', encoding='utf-8') as f:
        for line in range(len(corpus)):
            if (line !=len(corpus)-1):
                f.write(corpus[line]+'\n')
            else:
                f.write(corpus[line])

def append_file_to_corpus(file):
    corpus = []
    for line in file:
        corpus.append(line)
    return corpus