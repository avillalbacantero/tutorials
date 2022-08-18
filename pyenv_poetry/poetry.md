# Install Poetry

With the global Python version you want to use activated via pyenv:

`pip install poetry`

Place this in ~/.zshrc:
`export PATH=$PATH:$SOME/.poetry/bin`

# Use poetry in a project
`poetry init`

and add you main and dev dependencies. Then:

`poetry install`

It creates a virtual environment. To see it, do:

`poetry env info`
`poetry env info --path`
