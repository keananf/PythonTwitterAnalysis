NAME = twitter-analysis

env-conda: environment-conda.yml
	conda env create -f environment-conda.yml --name ${NAME}

env-pip: environment-pip.txt
	virtualenv -p python3 ${NAME}
	${NAME}/bin/pip3 install -r environment-pip.txt
