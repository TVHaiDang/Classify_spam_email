from project.lib import read_write_file

from sklearn.feature_extraction.text import CountVectorizer


def get_dataset(path):
    dataset = read_write_file.read_file(path)
    return dataset


def get_train_test_data(dataset):
    features = []
    labels = []
    for line in dataset:
        labels.append(line.split(" ")[0])
        features.append(" ".join(line.split()[1:]))
    return features, labels

def transform_word_2_vec(features,labels):
    cv = CountVectorizer()
    int_labels = []
    features = cv.fit_transform(features)
    for label in labels:
        if(label=='spam'):
            int_labels.append(1)
        else:
            int_labels.append(0)
    return features, int_labels



dataset = get_dataset('dataset/new_data.txt')
x,y = get_train_test_data(dataset)
features, labels = transform_word_2_vec(x,y)
print(features)
print(labels)
