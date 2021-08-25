# IMPORTING LIBERERES

def predict(data):
    import pandas as pd
    import numpy
    from sklearn.model_selection import train_test_split

    # SETTING UP DATA
    # file = pd.ExcelFile('data.xlsx').parse()
    X = pd.ExcelFile('data2.xlsx').parse()
    # print(X.head(600))
    Y = pd.ExcelFile('Y.xlsx').parse()
    # print("Y is :")
    # print(Y.head(600))
    # print("File Type is :")
    # print(type(file))
    # print(file['V1'])
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)
    # print(len(X_test))
    from sklearn.svm import SVC
    model = SVC(C=512,gamma=0.5)
    model.fit(X_train,Y_train)
    print(model.score(X_test,Y_test))
    print('predictng')
    return model.predict(data)

# arr = [[2.660713,2.624278,2.700593,0.4912516,0.4782521,0.4925644]]
# predict(arr)