#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics


def plant_classification():
    iris_data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris_data.data, iris_data.target, test_size=0.20, random_state=0)
    GaussianNB_model = naive_bayes.GaussianNB()
    GaussianNB_model.fit(X_train, y_train)
    return metrics.accuracy_score(y_test, GaussianNB_model.predict(X_test))


def main():
    print(f"Accuracy is {plant_classification()}")


if __name__ == "__main__":
    main()
