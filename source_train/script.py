from __future__ import print_function

import argparse
import os
import pandas as pd
import sklearn
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer

allow_pickle = True
from sklearn.externals import joblib

## TODO: Import any additional libraries you need to define a model
from sklearn.svm import LinearSVC

# Provided model load function
def model_fn(model_dir):
    """Load model from the model_dir. This is the same model that is saved
    in the main if statement.
    """
    print("Loading model.")
    
    
    # load using joblib
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    print("Done loading model.")
    
    return model


## TODO: Complete the main code
if __name__ == '__main__':
    
    # All of the model parameters and training parameters are sent as arguments
    # when this script is executed, during a training job
    
    # Here we set up an argument parser to easily access the parameters
    parser = argparse.ArgumentParser()

    # SageMaker parameters, like the directories for training data and saving models; set automatically
    # Do not need to change
    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--data-dir', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
    
    ## TODO: Add any additional arguments that you will need to pass into your model
    
    # args holds all passed-in arguments
    args = parser.parse_args()

    # Read in csv training file
    training_dir = args.data_dir
    train_data = pd.read_csv(os.path.join(training_dir, "train_Pipe.csv"), header=None, names=None)
    
    #Pipeline
    train_x = [str(x) for x in pd.read_csv(os.path.join(training_dir, "train_Pipe.csv"), header=None, names=None)[1].values]
    train_y = [str(x) for x in pd.read_csv(os.path.join(training_dir, "train_Pipe.csv"), header=None, names=None)[0].values]
    
    # NOPipeline
    #train_x=pd.read_csv(os.path.join(training_dir, "train.csv"),header=None, names=None).loc[:,1:].values
    #train_y=pd.read_csv(os.path.join(training_dir, "train.csv"),header=None, names=None).loc[:,0].values
    
    # Labels are in the first column. Unused
    #train_y = train_data.iloc[:,0].values
    #train_x = train_data.iloc[:,1].values
    

    
    ## --- Your code here --- ##
    

    ## TODO: Define a model 
    
    model = Pipeline([("tfidf",TfidfVectorizer(vocabulary=None,analyzer='word',ngram_range=(1,2))),("clf",LinearSVC())])
    #model = LinearSVC()

    
    
    ## TODO: Train the model
    model.fit(train_x, train_y)
    
    
    ## --- End of your code  --- ##
    

    # Save the trained model
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))
    

    #Takes a string separated by commas and split it to create a list of strings.
def predict_fn(input_data, model):
    input_data = input_data.split(",")
    prediction = ",".join(model.predict(input_data))
    return prediction


def input_fn(input_data, content_type):
    return input_data;

def output_fn(prediction_output, accept):
    return prediction_output;
        
