poetry show --tree
poetry version
poetry init
poetry shell
#inside shell: pip list
poetry add click@^8.1.0
poetry show
poetry add --dev pytest@latest
poetry add --dev black flake8 pre-commit tox
python reminder.py add go to the gym

pytest tests.py

black tests.py --check

black tests.py

git diff

#lint
flake8 --version

flake8 reminder.py

create a tox.ini file with exception for flake8

#to install hook configured in pre-commit yaml
pre-commit install

git init

pre-commit run --all-files

#run the tests
#like pytest tests.py
tox

