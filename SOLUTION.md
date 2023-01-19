# DareData Challenge

## Candidate: Paco Giudice

Proof of Automatic deploy and API running on EC2 instance:
https://youtu.be/iYinTu4D4u4

## How to run the solution locally 

* Make sure to have Docker Desktop (or equivalent) running
* cd into the repo directory
* Fill in your AWS credentials in .env_template file AND rename it .env
* RUN: docker-compose up
* Wait for around 5 minutes for the container to complete setup
* Go to http://localhost:8082/ (or other port shown in console log) in your browser
* Login airflow / airflow
* Run DAGs (wait for each completion): client -> sales -> processing
* When the DAGs are completed the model will be automatically trained and stored in “./modules/ds/models” . Metrics are printed into the console.

## Approach

My approach to the task was to focus on making the full stack functional, and refining details in a secondary stage. The DE part is not my expertise, so I knew I would need to tackle it first. Once the full system got functional, I used the remaining time to focus on clean(er) code and some EDA for the model.

The tech stack was mostly suggested by the learning material I was provided. The simplest way for me to implement a deploy solution with GH aciton was SSH and EC2. Flask was picked as a very simple a quick tool to implement. I had to try my hand with nginx, for the first time, mostly because I was not able to run flaks in daemon mode and getting the correct IP to make the requests.

## Timeline of the implementation

Day1:
* Reading contents (2h)
* Setup docker-contain (.env) to run functional components (1h)
* Running Airflow, gather data, look at the data (1h)
* Testing functional parts of other modules (1h)
* Prepare bare minimum DS module to run full pipeline (2h)
  * Pick and run simple ML model
  * Setup Docker
  * Prepare ds_package
  * Prepare run_training.py
* Prepare bare minimum API with Flask to call model (1h)

Day 2:
* Spinning EC2
* Try to set up GH Action Deploy (1h) - FAILED - fix later
* Review and clear code (1h)
* Extra_task from DE, create new Airflow DAG (1h) 
* Extra_task from MLE, logging (few mins)
* Preparing initial documentation (1h)
* Back to Github Action deploy - fixed (1h)
* Prepare black linting GH action (few minutes)
* Added ngnix to run deamon of flask in deploy GH action (2h)
* Prepared proof

Day 3:
* Clean up / refactor / test / documentation (2h)
* Prepare EDA (3h)
* Finale review (1h)

Challenges:
* GH Action not working on deploy (unclear credential setup)
* Not finding the way to print logs from Airflow through Docker to console
* Understand what is needed to deploy in deamon (nginx, gunicorn3)
* Accepting that I won't build a model that learns a random label

## Evaluation Checklist

*  [ x ] Fully implement your module (DS, DE or MLE, depending on the challenge you've received)
*  [ x ] Implement the extra tasks (1 for each other module)
*  [ x ] Implement the deployment module
*  [ x ] Include your module in the `docker-compose.yml` file, and ensure it works
*  [ x ] Include a `SOLUTION.md` document in the root of the repository, containing:
  *  [ x ] A description of the final solution and deployment, decisions taken, etc.
  *  [ x ] Screenshots of the deployed model in action
  *  [ x ] A high-level implementation timeline

## Improvements: Ain't Nobody Got Time for That

Here some items I would have like to work on, but decided to let go for time constrains. I hope this does not damage too much my final solution, and if any of these is highly necessary, please let me know and I ll allocate some time to it.
*  Set up GH deploy trigger to test API
*  Include tests with pytest
*  Making Airflow print in the terminal console
*  Making Airflow to fetch all historical sales data (if any) to aggregate (past_month function used instead)
*  Implement one-shot encoder rather that mapping to ints (not a distance feature)
*  The training kick in only when feature_store is fully populated, currenlty the SELECT query happens once every 30sec
*  Store training logs and metrics for each model training, within model object
*  Various minor TODO left around the repo

## Figures provided

*  FIG_1.png : Airflow DAG displays AVG/COUNT in log. (DE extra task)
*  FIG_2.png: successful deploy on EC2 and test request response

## Closure

Thanks for the task!