# DS Module

## Description

As the data scientist in your team, you must train a classification model to predict the label (0 or 1) for the customers.
This involves:

* doing EDA, feature engineering and model selection.
* creating a model Python class to represent your model, following the framework provided by the machine learning engineer.
* creating a few Docker images to:
    * train and store your model
    * serve your EDA as a document that can be viewed by others

## Implementation Requirements

### EDA

You should explore the data found in the `companydata` database and prepare a few visualizations using the tool of your choice.
You should also provide the exploration code you used for the initial model architecture selection, where you can also include some thoughts or commentary about your decisions if relevant.

These should go in the `eda` folder. A good solution that meets these requirements is a PDF export of a Jupyter notebook.

### Data Science Package

You should create a pip-installable package, called `data_science`, whose goal is to represent the final model.

Your package will be dependent on the pip-installable package found in the `mle` module, called `machine_learning_engineering`. 
* **Note:** You don't have to set it as an _actual_ package dependency, since it doesn't exist in PyPi, it's just for the purposes of this assessment!

In particular, you should create on your package a class that extends the `MLEModel` class defined by the MLE. You can think of this class as a simplified _ML Ops_ framework - from the perspective of the Machine Learning Engineer, as long as you implement the non-implemented methods defined in the parent class, then he can guarantee that the model is suitable for deployment.

Your model doesn't need to be complicated at all, after all this is a mock problem with 4 features. We are mostly interested in seeing how you approach the modelling problem and in assessing your software engineering expertise. However, feel free to use any deep learning framework if you want to show off!

Your package will be used by the `deployment` module to load the model, and serve new predictions.

### Docker Image for Modelling

You should create a Docker image that:

* installs your `data_science` package and any necessary requirements.
* waits until the `feature_store` table is available on the database.
  * **Note:** make sure your code doesn't crash if this table doesn't exist - you will have to manually run the `DE` ETLs to get this data! (see _Running the Final System_ section on the top-level README file)
* connects to the database using the **ds_user credentials** (check the `de` module to figure out what these are!)
* uses the data science package to train and store a model.

The "end-to-end" functionality should ideally go on a `main.py` file that is run inside the Docker container.

Finally, you must add this file to the `docker-compose.yml` file, making sure you are passing the right environment variables, and that you are mounting a `volume` so that you final model is accessible by the `deployment` module, outside the model training container. 