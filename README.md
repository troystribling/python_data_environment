## Required Packages

```
brew install pyenv
brew install pyenv-virtualenv
```

## Initialize pyenv and pyenv-virtualenv

Add the following to .zshrc
```
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
Reinitialize shell,

```
source .zshrc
```

## Install python

```
pyenv install 3.5.2
```

## Create Virtual Environment in Project Directory

```
pyenv virtualenv 3.5.2 data
```

## Activate Virtual Environment

```
pyenv activate data
```

## Install Packages

```
pip install -r requirements.txt
```

## Start Editing

The project assumes that the python working directory is ```(project directory)/projects```. If ```atom``` is used start from the command line in this directory.
