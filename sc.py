from selenium import webdriver
from bs4 import BeautifulSoup
 
id = "아이디"
password = "비번"
data = []
Playlist_f = []
Subject = ""
Number = ""
Teacher = ""
Content = ""
Target = ""
Day = ""
Day_f = []
Target_f = []
Number_f = []
Subject_f = []
Teacher_f = []
Content_f = []
Playlist_f = []
 
driver = webdriver.Chrome('경로')
driver.get('https://gyeseong.riroschool.kr/user.php')
delay = 3
driver.implicitly_wait(delay)
 
driver.find_element_by_name('mid').send_keys(id)
driver.find_element_by_name('mpass').send_keys(password)
driver.find_element_by_xpath('//*[@id="main_content"]/form/div/div[5]/a').click()
 
driver.find_element_by_xpath('/html/body/div[4]/div[2]/ul/li[2]/a').click()
 
 
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.close()
 
for i in range(2,12):
    Playlist = soup.find_all('tr')[i].get_text()
    Playlist = Playlist.split("\n", 5)
    Number = Playlist[1]
    Content = Playlist[2]
    Content = Content.replace("마감 2019년 ","")
    Target = Content[:3]
    Subject = Content[4:6]
    Content = Content.split("- ",1)
    Content = Content[1] 
    Teacher = Playlist[3]
    Day = Playlist[4]
    
    Content_f.append(Content)
    Subject_f.append(Subject)
    Day_f.append(Day)
    Teacher_f.append(Teacher)
    Target_f.append(Target)
    Playlist_f.append(Playlist)
    Number_f.append(Number)
    
print(Playlist_f)
print(Number_f)
print(Target_f)
print(Subject_f)
print(Teacher_f)
print(Day_f)
print(Content_f)
