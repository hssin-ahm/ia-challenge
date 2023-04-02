## Automatisation des processus de crédit bancaire API

This is a Flask API that makes prediction using a pre-trained TensorFlow model. It takes in input data in JSON format and returns the prediction as a JSON object.

### how to use

1. Clone the repository to your local machine
2. Install the required packages by running pip install -r requirements.txt
3. Download the pre-trained model and save it in the project directory with the name data_project_model.h5
4. Start the Flask server by running python app.py
5. Use a tool like Postman to send a POST request to http://localhost:3000/predict with input data in JSON format. The input data should include the following fields: loan_amnt, term, int_rate, installment, sub_grade, emp_length, home_ownership, annual_inc, verification_status, purpose, dti, delinq_2yrs, earliest_cr_line, inq_last_6mths, open_acc, pub_rec, revol_bal, revol_util, total_acc, initial_list_status, application_type, mort_acc, pub_rec_bankruptcies, address.
6. The API will return the prediction in JSON format.

### Examples

### Input

```json
{
  "loan_amnt": 10000,
  "term": "36 months",
  "int_rate": 13.56,
  "installment": 339.31,
  "sub_grade": "C1",
  "emp_length": "10+ years",
  "home_ownership": "RENT",
  "annual_inc": 55000,
  "verification_status": "Not Verified",
  "purpose": "credit_card",
  "dti": 18.24,
  "delinq_2yrs": 0,
  "earliest_cr_line": "Sep-2003",
  "inq_last_6mths": 1,
  "open_acc": 7,
  "pub_rec": 0,
  "revol_bal": 12345,
  "revol_util": 37.5,
  "total_acc": 22,
  "initial_list_status": "w",
  "application_type": "Individual",
  "mort_acc": 0,
  "pub_rec_bankruptcies": 0,
  "address": "3079 Taylor Street, Riverside CA 92506"
}
```

### Output

```json
[0.1890790467262268]
```
