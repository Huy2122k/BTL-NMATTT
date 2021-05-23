# Liveness Detection

* Code này nhận diện mặt thật (có chiều sâu) hay hình ảnh, video( không có chiều sâu)

* Nhanh hơn khi máy có GPU 

* Có thể đổi model thành Resnet50 với accuracy cao hơn 

<br>
<br>

* Cài đặt gói ( sử dụng python 3.8):


pip install imutils

pip install keras

pip install --upgrade h5py

pip install opencv-python


* Sử dụng:

Nếu chỉ sử dụng mô hình train sẵn, có thể đến luôn bước kiểm tra mặt thật, giả .
Muons hiệu năng cao hơn thì trai mô hình.


* Train mô hình: làm lần lượt



// tạo fake dataset dùng ảnh hoặc video

B1: Mở webcam.bat để thu video cho dataset, ấn "q" để thoát webcam, video sẽ lưu vào ouput.mp4 ở cùng thư mục 


B2: Mở preprocess.bat để chia video thành các ảnh chụp các khung hình từ video ouput.mp4.(lúc này là video fake) (images will be stored in ./dataset/fake )

//tạo Real dataset dùng mặt thật 

B1:  Mở webcam.bat để thu video cho dataset, ấn "q" để thoát webcam, video sẽ lưu vào ouput.mp4 ở cùng thư mục 


B2: Mở preprocess.bat để chia video thành các ảnh chụp các khung hình từ video ouput.mp4.(lúc này là video real(images will be stored in ./dataset/ real)

//trainning

B1: chạy trainLiveness.bat và chờ train


* Kiểm tra khuôn mặt là thật hay ảnh, video

Mở runLiveness.bat và đợi, sử dụng 

