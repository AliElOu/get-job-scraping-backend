from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
#chrome_options.add_argument("--headless")  


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
    return jobs


def data_organization(arg):
    data = [jb.split("\n") for jb in arg]
    output = [{'image':j[-2], 'title': j[0], 'company': j[1], 'location': [l for l in data[0] if l.split()[0] == "Région"][0], 'desc': j[2], 'link': j[-1]} for j in data]
    return output

print(data_organization(scrap_jobs()))