import requests
from bs4 import BeautifulSoup

# URL của trang web cần thu thập dữ liệu
URL = "https://vnexpress.net/"

# Gửi yêu cầu HTTP GET để lấy nội dung trang web
response = requests.get(URL)

# Kiểm tra xem yêu cầu có thành công không (status code 200)
if response.status_code == 200:
    # Phân tích cú pháp HTML của trang web
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Lấy tất cả các thẻ tiêu đề (ví dụ: h1, h2, h3)
    titles = soup.find_all(['h1', 'h2', 'h3'])
    
    print("Các tiêu đề trên trang:")
    for title in titles:
        print(title.get_text().strip())  # Lấy nội dung văn bản từ thẻ và loại bỏ khoảng trắng
else:
    print(f"Lỗi khi truy cập trang web. Mã lỗi: {response.status_code}")
