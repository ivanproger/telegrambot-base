```zsh
# this is just copy repo
git clone https://... telegram-bot && cd telegram-bot

# this is just install python virtual environment
python -m venv .venv
. .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# this will create .env file with secret keys, but you should change the values
cat env_sample > .env
```