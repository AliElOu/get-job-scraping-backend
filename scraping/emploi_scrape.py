from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import base64

chrome_options = Options()
chrome_options.add_argument("--headless")  

def encode_link(link):
    encoded_bytes = base64.urlsafe_b64encode(link.encode("utf-8"))
    encoded_str = str(encoded_bytes, "utf-8")
    return encoded_str

def decode_link(encoded_str):
    decoded_bytes = base64.urlsafe_b64decode(encoded_str)
    decoded_str = str(decoded_bytes, "utf-8")
    return decoded_str


def scrap_jobs():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.emploi.ma/recherche-jobs-maroc')
    jobs = []
    for _ in range(1,26):
        job = driver.find_elements(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div/div[2]/div[2]/div[{_}]')

        job_link = driver.find_elements(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div/div[2]/div[2]/div[{_}]/div/h3/a')
        job_link = job_link[0].get_attribute('href')

        job_img = driver.find_elements(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div/div[2]/div[2]/div[{_}]/picture/a/img')
        if len(job_img) == 0 :
            job_img = driver.find_elements(By.XPATH, f'/html/body/main/div[2]/div/div[2]/div/div[2]/div[2]/div[{_}]/picture/img')
        job_img = job_img[0].get_attribute('src')

        job_text = job[0].text
        job_text = job_text + f"\n{job_img}" + f"\n{job_link}"
        jobs.append(job_text)
    driver.quit()
    return data_organization(jobs)


def data_organization(arg):
    data = [jb.split("\n") for jb in arg]
    output = [{'image':j[-2], 'title': j[0], 'company': j[1], 'location': [l for l in j if l.split()[0] == "Région"][0], 'desc': j[2], 'link': encode_link(j[-1])} for j in data]
    return output

if __name__ == '__main__': 
    decode_link("aHR0cHM6Ly93d3cuZW1wbG9pLm1hL29mZnJlLWVtcGxvaS1tYXJvYy9idXNpbmVzcy1kZXZlbG9wZXItaGYtbWFycmFrZWNoLTgzODAyODk")
