
### Description
Mã hóa file sử dụng sinh trắc khuôn mặt

### TODO List

1. -[x] ~~Sử dụng Caffe Model cho nhận diện mặt~~
2. -[x] ~~Sử dụng OpenFace pretrained models cho mã hóa khuôn mặt thành các vector nhúng~~
3. -[x] ~~Sử dụng mã hóa AES để mã hóa và giải mã file~~
4. -[x] ~~Train với SVM cho việc nhận diện mặt từ các vector nhúng~~ 
5. -[x] ~~Giao diện đơn giản dễ sử dụng~~

### Cơ chế

- Sử dụng mật khẩu để đăng nhập , nếu mật khẩu đúng => hiện webcam check khuôn mặt => đúng người dùng => vào hệt thống
- Khi vào hệ thống có chức năng chọn đường dẫn file cần mã hóa, giải mã
- Mã hóa sẽ ko cần xác thực nhưng quá trình giải mã sẽ hiện lên webcam, cần khuôn mặt user để xác thực
- Toàn bộ danh sách vector khuôn mặt mã hóa của user được nhúng trong file pickle được mã hóa bởi mật khẩu
- Quá trình mã hóa file sử dụng mã hóa AES. 

### Cách dùng
**Create Database**



lần dùng đầu tiên:

- lưu một vài ảnh chân dung ngẫu nhiên của người lạ trong thư mục ./dataset/unknown 
- chạy train.py sau đó hướng mặt các góc khác nhau rồi bấm "q" cho đến khi train xong 
- sử dụng mật khẩu mặc định là 2122000 cho , có thể thay đổi trong menu.py

sau khi đăng nhập vào hệ thống có thể thay đổi khuôn mặt, mật khẩu.

### pip list (thiếu cái nào tự bổ sung)

-absl-py                 0.12.0
-astunparse              1.6.3
-asyncio                 3.4.3
-cachetools              4.2.1
-certifi                 2020.12.5
-chardet                 4.0.0
-cycler                  0.10.0
-flatbuffers             1.12
-gast                    0.3.3
-google-auth             1.29.0
-google-auth-oauthlib    0.4.4
-google-pasta            0.2.0
-grpcio                  1.32.0
-h5py                    2.10.0
-idna                    2.10
-imutils                 0.5.4
-joblib                  1.0.1
-Keras                   2.4.3
-Keras-Preprocessing     1.1.2
-kiwisolver              1.3.1
-Markdown                3.3.4
-matplotlib              3.4.1
-numpy                   1.19.5
-oauthlib                3.1.0
-opencv-contrib-python   4.5.1.48
-opencv-python           4.5.1.48
-opt-einsum              3.3.0
-Pillow                  8.2.0
-pip                     19.2.3
-protobuf                3.15.8
-pyasn1                  0.4.8
-pyasn1-modules          0.2.8
-pycryptodome            3.10.1
-pyparsing               2.4.7
-pypiwin32               223
-PyQt5                   5.15.4
-PyQt5-Qt5               5.15.2
-PyQt5-sip               12.8.1
-python-dateutil         2.8.1
-pywin32                 300
-PyYAML                  5.4.1
-requests                2.25.1
-requests-oauthlib       1.3.0
-rsa                     4.7.2
-scikit-learn            0.23.1
-scipy                   1.6.3
-setuptools              41.2.0
-six                     1.15.0
-tensorboard             2.5.0
-tensorboard-data-server 0.6.0
-tensorboard-plugin-wit  1.8.0
-tensorflow              2.4.1
-tensorflow-estimator    2.4.0
-termcolor               1.1.0
-threadpoolctl           2.1.0
-typing-extensions       3.7.4.3
-urllib3                 1.26.4
-Werkzeug                1.0.1
-wheel                   0.36.2
-wrapt                   1.12.1
