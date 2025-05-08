from pickle import load
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import make_scorer, fbeta_score
from sklearn.model_selection import RandomizedSearchCV
import pickle

def inference(data: list):
    if isinstance(data, list):
        data = pd.DataFrame(data, columns = ['person_age', 'person_income', 'person_emp_exp', 'loan_amnt',
       'loan_int_rate', 'loan_percent_income', 'cb_person_cred_hist_length',
       'credit_score', 'person_gender_male',
       'person_education_Bachelor', 'person_education_Doctorate',
       'person_education_High School', 'person_education_Master',
       'person_home_ownership_OTHER', 'person_home_ownership_OWN',
       'person_home_ownership_RENT', 'loan_intent_EDUCATION',
       'loan_intent_HOMEIMPROVEMENT', 'loan_intent_MEDICAL',
       'loan_intent_PERSONAL', 'loan_intent_VENTURE',
       'previous_loan_defaults_on_file_Yes'])

    with open('../models/v1/pipe.pcl', 'rb') as fid:
        pipe = load(fid)

    model = pickle.load(open('../models/v1/rf_model.pcl', 'rb'))

    x = pipe.transform(data)
    y_pr = model.predict(x)
    return y_pr

def main():
    test_sample = [[22.0, 71948.0, 0, 35000.0, 16.02, 0.49, 3.0, 561,
                    False, False, False, False, True, False, False, True, False, False, False, True, False, False]]
    a = inference(test_sample)
    print('Your loan is:')
    print('Approved' if a[0] == 1 else 'Rejected')


if __name__ == '__main__':
    main()