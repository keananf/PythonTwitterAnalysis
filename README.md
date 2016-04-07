# PythonTwitterAnalysis
Python program to analyse twitter datasets

## Running the virtual environment:
# for [conda](http://conda.pydata.org/miniconda.html), [install instructions](http://conda.pydata.org/docs/install/quick.html))
With conda installed, in the directory of the project files:
this makes the virtual environment with the name 'twitter-analysis'
```
make env-conda
```

or, if you want to make the environment with a different name:
```
make env-conda NAME=the-name-you-want
```

Next, to enter the virtual environment, type `source activate <environment-name>`, the name will be 'twitter-analysis' by default; and to exit type `source deactivate`.

# Without Conda
To run a virtual environment using pip3 and python3 (will need virtualenv installed) use

```
make env-pip NAME=the-name-you-want
```
and to enter the virtual environment,
```
source the-name-you-want
```
and then to exit,
```
deactivate
```
