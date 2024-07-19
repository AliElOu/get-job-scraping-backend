import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from firebase.firebase_config import db


def scrape_jobs():
    pass


def save_to_firestore(jobs):
    for job in jobs:
        job_ref = db.collection('jobs').document(job['link'])
        if not job_ref.get().exists:
            job_ref.set(job)
        else:
           print("duplicated")

if __name__ == '__main__':
    jobs = scrape_jobs()
    save_to_firestore(jobs)
