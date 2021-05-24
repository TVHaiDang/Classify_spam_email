from project.lib import read_write_file, entity_tagging, models, word_embedding
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# def parser_agrs():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--classifier", type = str, default = None)
#     return parser.parse_args()
# def get_request():
#     parser = parser_agrs()
#     classifier = parser.classifier
#     return classifier


f = read_write_file.read_file('dataset/data_sample.txt')


corpus = read_write_file.append_file_to_corpus(f)
corpus_new = entity_tagging.entity_tagging(corpus)
read_write_file.write_file('dataset/new_data.txt', corpus_new)
dataset = read_write_file.read_file('dataset/new_data.txt')
features, labels = word_embedding.get_train_test_data(dataset)
features_vec, labels_vec = word_embedding.transform_word_2_vec(features, labels)
x_train, x_test, y_train, y_test = train_test_split(features_vec, labels_vec)
model_bayes = models.naive_bayes_model(x_train, y_train)
model_svm = models.svm_model(x_train, y_train)

y_pred = model_svm.predict(x_test)
print("The accuracy: ",accuracy_score(y_test, y_pred))
print(y_pred[0])

# print(corpus)
