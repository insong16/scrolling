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
    driver.find_element(By.XPATH, '//*[@id="id"]').send_keys('22-10105')
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="pw"]').send_keys('kis60516!')
    time.sleep(0.5)

    login_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/section/div[2]/div[2]/form/button')  # 로그인 버튼의 XPath 사용
    login_button.click()
    
    # 로그인 후 페이지 로드 대기
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]')))
except Exception as e:
    print(f"로그인 실패: {e}")
    driver.quit()
    exit()
    
    # 수행평가 페이지로 이동
    try:
        # 수행평가 버튼 클릭 (정확한 XPath 확인 필요)
        driver.find_element(By.XPATH, '//*[@id="container"]/div/ul[4]/li[1]/svg').click()  # 예: '//*[@id="menu"]/ul/li[1]/a'
        
        # 수행평가 페이지 로드 대기
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[2]/table/tbody/tr[2]/td[3]/a[2]')))  # 예: '//*[@id="container"]/div/div[2]/table/tbody/tr[3]/td[3]/a[2]'
        
        # 수행평가 항목 리스트 가져오기
        rows = driver.find_elements(By.XPATH, '//*[@id="container"]/div/div[2]/table/tbody/tr')
        
        print("수행평가 데이터:")
        for row in rows:
            try:
                title = row.find_element(By.XPATH, './td[3]/a[2]').text  # 제목의 XPath
                due_date = row.find_element(By.XPATH, './td[7]/strong').text  # 마감일의 XPath
                print(f"제목: {title}, 마감일: {due_date}")
            except Exception as e:
                print(f"수행평가 데이터 가져오기 실패: {e}")
    
    except Exception as e:
        print(f"수행평가 페이지로 이동 실패: {e}")
    
    # 메인 페이지로 돌아가기 (필요한 경우)
    driver.get('https://gyeseong.riroschool.kr/main_page_url')  # 실제 메인 페이지 URL로 교체
    
except Exception as e:
    print(f"오류 발생: {e}")

finally:
    driver.quit()