import sys
import os
import emploi_scrape
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from firebase.firebase_config import db


def scrape_jobs():
    jobs = emploi_scrape.scrap_jobs()
    return jobs


def save_to_firestore(jobs):
    for job in jobs:
        try:
            job_ref = db.collection('jobs').document(job['link'])
            if not job_ref.get().exists:
                job_ref.set(job)
            else:
                print("duplicated")
        except:
            print("Error !")
        

if __name__ == '__main__':
    jobs = scrape_jobs()
    save_to_firestore(jobs)