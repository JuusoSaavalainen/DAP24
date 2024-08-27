#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet = "abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words


def load_finnish():
    finnish_url = "https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename = "src/kotus-sanalista_v1.xml"
    load_from_net = False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines = []
            for line in data:
                lines.append(line.decode('utf-8'))
        doc = "".join(lines)
    else:
        with open(filename, "rb") as data:
            doc = data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))


def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines = map(lambda s: s.rstrip(), data.readlines())
    return lines


def get_features(a):
    return np.array([[word.count(char) for char in alphabet] for word in a])


def contains_valid_chars(s):
    if any(c not in alphabet_set for c in set(s)):
        return False
    return True


def get_features_and_labels():
    fin = load_finnish()
    fin = [word.lower() for word in fin]
    fin = list(filter(contains_valid_chars, fin))
    X_fin = get_features(fin)
    y_fin = np.zeros(len(fin))

    eng = load_english()
    eng = list(filter(lambda s: s[0].islower(), eng))
    eng = [word.lower() for word in eng]
    eng = list(filter(contains_valid_chars, eng))
    X_eng = get_features(eng)
    y_eng = np.ones(len(eng))

    return np.concatenate([X_fin, X_eng]), np.concatenate([y_fin, y_eng])


def word_classification():
    X, y = get_features_and_labels()
    model = MultinomialNB()
    model.fit(X, y)
    kf = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    return cross_val_score(model, X, y, cv=kf)


def main():
    print("Accuracy scores are:", word_classification())


if __name__ == "__main__":
    main()
