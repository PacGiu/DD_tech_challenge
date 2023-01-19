pip install modules/mle/mle_package
pip install modules/ds/docker/ds_package
flask --app modules/deployment/api/app.py run --host 44.201.84.158 # TODO: IP should be read from config
python3 modules/deployment/example_request.py