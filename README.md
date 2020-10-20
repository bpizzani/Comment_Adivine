# Comment_Adivine

## About The Project
This project builds a supervised model to provide real-time labeled comments. After preprocessing the comments received from customers on different Hospitals,the model aims to predicts the labels of the comments based on the principle of TFIDF using a supervised model based on vector: LinearSVC.

## Built With
•	AWS SageMaker
•	Python

## Getting Started
You will need access to Amazon Web Services Notebook instance and clone this project there. Open the terminal in the SakeMaker Notebook and type
```bash
cd SageMaker
git clone https://github.com/bpizzani/Comment_Advine.git
```

## Prerequisites
To build the model and preprocess the data you will need the following knowledge:

•	AmazonWebServices – SageMaker

•	API and Lambda functions

•	Machine Learning concepts

•	Sklearn

•	NLTK

•	Spacy

## Installation
1.	Clone the repo
```bash 
git clone https://github.com/bizzani/Comment_Advine.git
```
2.	Install pip packages:

•	Spacy

•	NLTK

•	Numpy

•	Pandas

•	Sklearn

•	Matplotlib

```bash
pip install <packages>
!python -m spacy download es
```
  
## Usage
Once you have clone the project into ASW Sagemaker Notebook you can access the .ipynb file and run the preprocessing code and build the sklearn LinearSVC estimator and carry on the deployment. 

Once the predictor (estimator.deploy()) has been created we create a Lambda Function and invoke the endpoint setting the endpoint name to the predictor endpoint name (predictor.endpoint).

Lambda function code is also included in this project.

Finally, we create an API linked to our lambda function in AWS API, and we will get the API url that we would need to copy and paste into the “Index.html” file in the where: action= “link”. More instructions are provided in the Comment_Adiviner.ipynb file.

The lambda functions will take a string and send it to the model, the prediction function has been modified so that predict_fn() would preprocess the input and put in an a format the model can make a prediction (array) and return as string of predictions to pass back to the Web App and Lambda.

To make predictions we access “Index.html” and upload a CSV file containing reviews on each row. Then click Submit and we we receive a table with predictions on each comment.

You can use the file test_data_WebbApp.xlsx to thest the Web App.
I also created my own domain and uploaded the Web App to my domain, so anyone could access this URL and make predicitons:
https://www.brunopizzani.com/Comment_Adiviner_CSV.html

## License
Distributed under the MIT License. See LICENSE for more information.

## Contact
Your Name – bpizzani92@gmail.com
Project Link: https://github.com/bpizzani/Comment_Adiviner
