clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log* && rm -fr .cache && rm -rf .pytest_cache

venv:
	virtualenv -p python3 ~/.virtualenvs/simple_xntwist_ui && . ~/.virtualenvs/simple_xntwist_ui/bin/activate && pip3 install -r requirements.txt

run:
	~/.virtualenvs/simple_xntwist_ui/bin/python simple_xntwist_ui/simple_xntwist_ui.py

test: clean
	~/.virtualenvs/simple_xntwist_ui/bin/python -m pytest
