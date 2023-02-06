import requests
import csv

def get_data():
    data = requests.get(
        "https://jobs.siemens.com/api/jobs?page=1&location=Deutschland&keywords=Python&sortBy=relevance&limit=100&stretch=0&stretchUnit=MILES&internal=false")

    jresponse = data.json()

    with open('job_scrape.csv', 'w', encoding="utf8") as csv_file:
        csv_writer = csv.writer(csv_file, )
        csv_writer.writerow(['Job_Title', 'Job_ID', 'City', 'Job_Type', 'Job_Level', 'Job_Description'])
        print("Total number of positions for 'Python Developer Role' found at Siemens = {}".format(jresponse['count']))
        for job in jresponse['jobs']:
            jd = job['data']
            py_lib = str(jd['description'])
            csv_writer.writerow([jd['title'], jd['req_id'], jd['city'], jd['tags5'][0], jd['tags2'][0], py_lib])


get_data()
