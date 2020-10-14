# Comment_Adivine

•	The project's domain background — the field of research where the project is derived;

The project’s domain traces back to a Customer Experience company that wants to feed from customer’s feedback and to provide their clients with customer insight. They want to somehow predict the topic of a customer’s comment. 
Based on the comments characteristics a supervised approach would be more convenient as the comments aren’t long enough to take a unsupervised approach.
At the moment, comments are being manually labeled and sent to the client, they spend too much time labeling comments, therefore ,clients doesn’t have their customer’s feedback until much later when it might be too late to improve the customer experience.

•	A problem statement — a problem being investigated for which a solution will be defined;

The company can not provide in real-time the issues that the comments are attend to. Comments must be manually reviewed everyday and labeled by a person, the amount of comments per day is too big and can’t be handled anymore by people. They need to provide real-time labeled comments so their clients can understand which are the main negative comments on specific topics right now.

•	The datasets and inputs — data or inputs being used for the problem;

The dataset used are comments from different hospital’s clients in Spanish language from 2017 to 2019 obtained through a tablet terminal where the customer’s are asked how was their experience at the Hospital.
The Dataset contains the Name of the hospital, the comment and the topic of the comment. I will use this data to train a model after preprocessing some details.

•	A solution statement — the solution proposed for the problem given;

Using a supervised machine learning algorithm and text analytics I would train a model with labeled comments to predict the label of each comment based on the the principles of TFIDF (short for term frequency–inverse document frequency). TFIDF measures not only the term count of a comment, but also the frequency compensating the most and less used terms along the dataframe. This will create a matrix of terms and their respectively label. 


•	A benchmark model — some simple or historical model or result to compare the defined solution to;

Vector models proven very efficient in these kind of excersies such as LinearSVC and SGDClassifier:
 
I believe a vector based algorithm is a good approach for this issue as it will transport a matrix of term frequency vectors to a 2 or 3 dimensional plane where the comments with similar term frequency of words would  be close to each other and share the same label.


•	A set of evaluation metrics — functional representations for how the solution can be measured;

The solution for the problem is to predict a realtime comment’s topic/label related to hospital affairs such as (Food, Waiting Time, Stuff, Cleaning, Facility etc.).
This is important for reporting as they can update their client with categorized comments about what’s wrong in the hospital and which comments are the most frequent. Therefore, the metric needed to evaluate the performance of the model must be the “Recall” and “Precision”, as the classes are unbalanced “Accuracy” wouldn’t work for our model. We need to make sure that the models predicts most of the comments correctly and with high precision or error in each Label.

•	An outline of the project design — how the solution will be developed and results obtained.

1 Step would be to processing the text (removing punctuation, stopwords, lemmatization and stemming of words and vectorizing using TFIDF).
2. Compare different sklearn algorithms and see their accuracy.
3. Calculate the accuracy of the model on different n-grams distributions to create the training vocabulary. Depending on the length of comments a small n-gram could benefit the performance.
4. Train the mode. LinearSVC.
5. Visualize test predictions in different formats to evaluate results.
6. Deploy model in API and create Lambda to receive input, which can be inputted in two different ways:
     a. by typing a single comment using an API with a lambda function or
      b. by uploading a CSV with comments using an API as well.
   Then you will receive as output the comment’s label or a csv with the predicted label and the comment itself.
