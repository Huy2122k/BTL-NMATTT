
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

