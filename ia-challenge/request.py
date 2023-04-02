import requests

url = 'http://127.0.0.1:5000/predict'
input_data = {
   "loan_amnt": 10000.0,
   "term": "36 months",
   "int_rate": 11.44,
   "installment": 329.48,
   "grade": "B",
   "sub_grade": "B4",
   "emp_title": "Marketing",
   "emp_length": "10+ years",
   "home_ownership": "RENT",
   "annual_inc": 117000.0,
   "verification_status": "Not Verified",
   "issue_d": "Jan-2015",
   "loan_status": "Fully Paid",
   "purpose": "vacation",
   "title": "Vacation",
   "dti": 26.24,
   "earliest_cr_line": "Jun-1990",
   "open_acc": 16.0,
   "pub_rec": 0.0,
   "revol_bal": 36369.0,
   "revol_util": 41.8,
   "total_acc": 25.0,
   "initial_list_status": "w",
   "application_type": "INDIVIDUAL",
   "mort_acc": 0.0,
   "pub_rec_bankruptcies": 0.0,
   "address": "0174 Michelle Gateway"
}


response = requests.post(url, json=input_data)
print(response.json())
