import sys
import os
import emploi_scrape
import rekrute_scrape
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from firebase.firebase_config import db


def scrape_jobs():
    jobs1 = emploi_scrape.scrap_jobs()
    jobs2 = rekrute_scrape.scrap_jobs()
    jobs = jobs1 + jobs2
    return jobs


def save_to_firestore(jobs):
    for job in jobs:
        try:
            job_ref = db.collection('jobs').document(job['link'])
            if not job_ref.get().exists:
                job_ref.set(job)
                print("saved")
            else:
                print("duplicated")
        except Exception as e:
            print("Error ! : ",e)
        

if __name__ == '__main__':
    jobs = scrape_jobs()
    save_to_firestore(jobs)