# Fairify Authors

* Sumon Biswas, Carnegie Mellon University (sumonb@cs.cmu.edu)
* Hridesh Rajan, Iowa State University (hridesh@iastate.edu)

## Index
> 1. [Models](models/)
> 2. Datasets
  >> * [German Credit (GC)](data/german)
  >> * [Adult Census (AC)](data/adult)
  >> * [Bank Marketing (BM)](data/bank)
  >> * [Bank Deposit (BD)](data/deposit)
  >> * [Creditcard Fraud (CF)](data/fraud)
> 3. Verification source code
  >> * [Verify models](src/)
  >> * [Verify models with scaled experiment](stress/)
  >> * [Verify relaxed queries](relaxed/)
  >> * Verify relaxed queries
  >  >> * [Targeted queries 1](targeted/)
  >  >> * [Targeted queries 2](targeted2/)
  >> * [Utilities](utils/)
> 4. Appendix
  >> * [Supplementary results](/Appendix-Result.pdf)

## Dataset Attributes

- German Credit 
> Check [here](data/german/german.doc)

- Adult Census
> Check [here](data/adult/adult.names)

- Bank Marketing
> Check [here](data/bank/bank-additional-names.txt)

- Bank Deposit 
> age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome,deposit

- Creditcard Fraud
> "Time","V1","V2","V3","V4","V5","V6","V7","V8","V9","V10","V11","V12","V13","V14","V15","V16","V17","V18","V19","V20","V21","V22","V23","V24","V25","V26","V27","V28","Amount","Class"

## MLP Models

- German Credit 

Script for extracting model information could be find [here](models/german/model_sum.py).

Model tensorflow definition could be find [here](src/GC/models.py).

Model training scripts could be find [here](src/GC/train1.py).

Pretrained-models could be find [here](models/german/).

| Model Name        | Model Structure  | Number of Neurons |
| ----------------- | ---------------- | ------------------ |
| Model 1           | D-R-D-S     | 51              |
| Model 2           | D-R-D-S      | 101              |
| Model 3           | D-R-D-S      | 10              |
| Model 4           | [D-R]*2-D-S      | 11              |
| Model 5           | [D-R]*5-D-S      | 125              |

D: Dense Layer

R: ReLU

S: Sigmoid

- Adult Census

Script for extracting model information could be find [here](models/adult/model_sum.py).

Model tensorflow definition could be find [here](src/AC/models.py).

Model training scripts could be find [here](src/AC/train1.py).

Pretrained-models could be find [here](models/adult/).

| Model Name        | Model Structure  | Number of Neurons |
| ----------------- | ---------------- | ------------------ |
| Model 1           | [D-R]*2-D-S     | 25              |
| Model 2           | D-R-D-S         | 101              |
| Model 3           | D-R-D-S         | 51              |
| Model 4           | [D-R]*2-D-S      | 201              |
| Model 5           | [D-R]*2-D-S      | 129              |
| Model 6           | [D-R]*2-D-S      | 25              |
| Model 7           | [D-R]*5-D-S      | 125              |
| Model 8           | [D-R]*2-D-S      | 11              |
| Model 9           | [D-R]*4-D-S      | 13              |
| Model 10           | [D-R]*4-D-S      | 21              |
| Model 11           | [D-R]*4-D-S      | 41              |
| Model 12           | [D-R]*5-D-S      | 125              |

D: Dense Layer

R: ReLU

S: Sigmoid

- Bank Marketing

Script for extracting model information could be find [here](models/bank/model_sum.py).

Model tensorflow definition could be find [here](src/BM/models.py).

Model training scripts could be find [here](src/BM/train1.py).

Pretrained-models could be find [here](models/bank/).

| Model Name        | Model Structure  | Number of Neurons |
| ----------------- | ---------------- | ------------------ |
| Model 1           | [D-R]*2-D-S     | 81              |
| Model 2           | [D-R]*2-D-S         | 49              |
| Model 3           | D-R-D-S         | 101              |
| Model 4           | [D-R]*3-D-S      | 301              |
| Model 5           | [D-R]*2-D-S      | 33              |
| Model 6           | [D-R]*2-D-S      | 19              |
| Model 7           | [D-R]*2-D-S      | 129              |
| Model 8           | [D-R]*2-D-S      | 115              |

D: Dense Layer

R: ReLU

S: Sigmoid


- Bank Deposit 

Script for extracting model information could be find [here](models/deposit/model_sum.py).

Model tensorflow definition could be find [here](src/BD/models.py).

Model training scripts could be find [here](src/BD/train1.py).

Pretrained-models could be find [here](models/deposit/).

| Model Name        | Model Structure  | Number of Neurons |
| ----------------- | ---------------- | ------------------ |
| Model 1           | [D-R]*2-D-S     | 25              |
| Model 2           | D-R-D-S         | 101              |
| Model 3           | D-R-D-S         | 51              |
| Model 4           | [D-R]*2-D-S      | 201              |
| Model 5           | [D-R]*2-D-S      | 129              |
| Model 6           | [D-R]*2-D-S      | 25              |
| Model 7           | [D-R]*5-D-S      | 125              |
| Model 8           | [D-R]*2-D-S      | 11              |
| Model 9           | [D-R]*4-D-S      | 13              |
| Model 10           | [D-R]*4-D-S      | 21              |
| Model 11           | [D-R]*4-D-S      | 41              |
| Model 12           | [D-R]*5-D-S      | 125              |

D: Dense Layer

R: ReLU

S: Sigmoid

L: LeakyReLU

## Installation

To run Fairify, we need to install Python 3 environment. The current version has been tested on Python 3.7. It is recommended to install Python virtual environment for the tool. Furthermore, we used bash shell scripts to automate running benchmark and Python scripts. Below are step-by-step instructions to setup environment and run the tool. 

### Environment Setup

Follow these steps to create a virtual environment and clone the Fairify repository.

2. Clone this repository and move to the directory:

```
git clone https://github.com/sumonbis/Fairify
cd Fairify/
``` 

1. Run this on command line to create a virtual environment:

```
conda create --name fenv python=3.8
conda activate fenv
```

Run the following command to update pip on Python: `python3 -m pip install --upgrade pip`. Alternatively, you can follow the [Python documentation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) to install virtual environment on your machine. 

3. Navigate to the cloned repository: `cd fairify/` and install required packages:

```
pip install -r requirements.txt
```

To run the tool, please refer to the [installation file](/INSTALL.md) for detailed instructions. 

### Cite the paper as
```
@inproceedings{biswas23fairify,
  author = {Sumon Biswas and Hridesh Rajan},
  title = {Fairify: Fairness Verification of Neural Networks},
  booktitle = {ICSE'23: The 45th International Conference on Software Engineering},
  location = {Melbourne, Australia},
  month = {May 14-May 20},
  year = {2023},
  entrysubtype = {conference}
}
```