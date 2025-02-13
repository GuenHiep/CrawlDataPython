import requests
from bs4 import BeautifulSoup

# URL của trang web bạn muốn crawl
url = 'https://baomoi.com'

# Gửi yêu cầu HTTP GET đến trang web
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    # Phân tích cú pháp HTML bằng BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Ví dụ: Lấy tiêu đề của trang web
    title = soup.title.string
    print(f'Tiêu đề trang web: {title}')
    
    # Ví dụ: Lấy tất cả các liên kết (thẻ <a>) trong trang
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        text = link.get_text()
        print(f'Liên kết: {text} -> {href}')
else:
    print(f'Không thể truy cập trang web. Mã trạng thái: {response.status_code}')