# Flight-price-prediction-app

**Deployed Machine learning model(lightGBM) with an accuracy of over 87% for flight price prediction**.
It takes 5 inputs from the user 
1. *Cabin* (Cabin type)
2. *Departure City* (Departure city / city where flight is to be taken)
3. *Departure Date* (the date of flight )
4. *Arrival City* (city where flight has to land)
5. *Departure hours* (the approximate integer/ nearest integer to flight departure timing)

**The output of the model is float point value of flight Price upto 4 decimal places**.

*Note : The internal model is based on a *optimal_time parameter* , which assumes that time of booking the flight is 4 hours before departure.
So, according to model, the cheapest flight prices are 4 hours before actual flight takeoff. 
Please book your flights accordingly.

# Dataset
The model has been trained with a dataset having *14 attributes* and over *3 million+ data points*.
The model took only five parameters , same as input parameters, for final training as according to 
feature importance map, only these *5 parameters* were found to useful .

# Model
The model *LightGBM* is decision tree based model, optimized with a gradient boosting method to enhance performance.
The model used adam_optimizer as learning parameter and learning_rate was *0.01*.
It had *20,000 estimators*.
The *max_depth* parameter of decision tree was set to *8*.
It had an evaluation_metric as *rmse (root mean square error)*.

# Evaluation
We used mean_squared_error and mean_absolute_error for final evaluation of the model.

*Thanks*

**This project was the final part of Data Analyst Internship at Technocolabs Softwares India.** 

*Please, feel free to fork this repo and tinker with the code.*

*Don't forget to give a star to this repo, if you liked it :)*

