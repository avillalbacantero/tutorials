# Install pyenv on Ubuntu:

1. Build dependencies:

`sudo apt-get install -y make build-essential libssl-dev zlib1g-dev
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl`

2. Install pyenv

`curl https://pyenv.run | bash`

Put pyenv on PY_ENV and PATH (follow the prompted instructions once installed)

# Use pyenv:

Install a Python version and make it your global Python version:

`pyenv install 3.9.10`

`pyenv versions`

`pyenv global 3.9.10`