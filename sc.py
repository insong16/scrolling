from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 셀레니움 설정
chrome_options = Options()
chrome_options.add_argument('--headless')  # 브라우저를 숨김 모드로 실행
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 크롬드라이버의 경로 설정 (다운로드한 크롬드라이버의 경로)
chromedriver_path = r'C:\Users\a0105\OneDrive\바탕 화면\파이썬 연습\p j c\chromedriver.exe'  # 또는 'C:\\Users\\a0105\\OneDrive\\바탕 화면\\파이썬 연습\\p j c\\chromedriver.exe'
service = Service(chromedriver_path)

# 브라우저 실행
driver = webdriver.Chrome(service=service, options=chrome_options)

# 리로스쿨 웹사이트 열기
driver.get('https://gyeseong.riroschool.kr/user.php?action=signin')


# 로그인 정보 입력
try:
    username_field = driver.find_element(By.NAME, '//*[@id="container"]/div/section/div[2]/div[2]/form/div[1]')  # 사용자명 필드의 이름 속성 사용
    password_field = driver.find_element(By.NAME, '//*[@id="container"]/div/section/div[2]/div[2]/form/div[2]')  # 비밀번호 필드의 이름 속성 사용

    username_field.send_keys('22-10105')  # 사용자명 입력
    password_field.send_keys('kis60516!')  # 비밀번호 입력

    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')  # 로그인 버튼의 XPath 사용
    login_button.click()
    
    # 로그인 버튼 클릭
    login_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/section/div[2]/div[2]/form/button')  # 로그인 버튼 XPath (예시)
    login_button.click()    
    
    # 로그인 후 페이지 로드 대기
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]')))
except Exception as e:
    print(f"로그인 실패: {e}")
    driver.quit()
    exit()

# 수행평가 데이터 가져오기
try:
    element = driver.find_element(By.XPATH, '//*[@id="container"]/div/ul[4]/li[1]/span')  # 예시 XPath
    print("수행평가 데이터:")
    print(element.text)
except Exception as e:
    print(f"수행평가 데이터 가져오기 실패: {e}")

# 이동수업출석부 데이터 가져오기
try:
    element = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]/ul/li[7]/ul/li[1]')  # 예시 XPath
    print("이동수업출석부 데이터:")
    print(element.text)
except Exception as e:
    print(f"이동수업출석부 데이터 가져오기 실패: {e}")

# 브라우저 종료
driver.quit()
