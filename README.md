# Loan-Approval
In this project I made ML models to classify the rate of approving loans to customers and when it should be accepted and where not. There I conducted EDA to see the properties of target customers and basing on the obtained data structure, 
I tried several ML models to achieve the best result. The best result was given by Random Forest with accuracy 93% and precision 91%. Precision here is more important because in maximizing it we are more sure to work with the customers that are able 
to give the money back which minimizes the risk for the bank of losing money.

My goals for this pet-projects are:

1) Improve evaluating metrics further
2) Deploy the model and create interface that shows if you can take a loan online

Upd: I succesfully deployed the project using streamapp and later will provide screenshots for prove

Right now I am still working on ML part as I experience a problem of lacking of data as there is no enough info about some categories of users.
For example: We can see that over 80 % dta about house owning are rent and mortgage
![Image alt](https://github.com/{Alexandrbel204}/{Loan-Approval}/raw/{main}/{pictures}/person_education.png)

and because of that almost all people with their own house or other category will receive be unfairly rejected
