import pickle 
from sklearn.svm import SVC 
from sklearn.preprocessing import LabelEncoder
from encryption import Encryptor

data = pickle.loads(open("./pickle/embeddings.pickle","rb").read())

le = LabelEncoder()
labels = le.fit_transform(data['names'])

classifier = SVC(C=1.0,kernel="linear",probability=True)
classifier.fit(data["embeddings"],labels)

f = open("./pickle/classifier.pickle","wb")
f.write(pickle.dumps(classifier))
f.close()

f = open("./pickle/label.pickle","wb")
f.write(pickle.dumps(le))
f.close()
print(" train done")

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)

enc.encrypt_file("./pickle/label.pickle")
print("File label encrypted")
enc.encrypt_file("./pickle/classifier.pickle")
print("File classifier encrypted")
enc.encrypt_file("./pickle/embeddings.pickle")
print("File embeddings encrypted")
