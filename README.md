# PythonTwitterAnalysis
Python program to analyse twitter datasets

## Running the virtual environment:
## for [conda](http://conda.pydata.org/miniconda.html), [install instructions](http://conda.pydata.org/docs/install/quick.html))
With conda installed, in the directory of the project files:
this makes the virtual environment with the name 'twitter-analysis'
```
make env
```

or, if you want to make the environment with a different name:
```
make env NAME=the-name-you-want
```

Next, to enter the virtual environment, type `source activate <environment-name>`, the name will be 'twitter-analysis' by default; and to exit type `source deactivate`.

## Without Conda
To run a virtual environment which is completely self-contained, you can use the included venv folder. This contains its own binaries for python3, pip3 and all the required packages.

use
```
source venv/bin/activate
```
to enter the virtual environment, and
```
deactivate
```
to exit.
