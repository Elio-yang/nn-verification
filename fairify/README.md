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

## NN Model in Z3 

Model related functions and z3 solver implementation of model structure could be find [here](utils/), each file will start with [Dataset]-[Model Index]-Functions.py. In each file, there will be two functions ``layer_net`` and ``net`` for real network operation, and there will be a ``z3_net`` for solver related implementation. 

For z3 implemented neural network operations (e.g. activation functions) could be finf [here](utils/verif_utils.py), if extra operation are included, modify this file to support it. 



## Installation

To run Fairify, we need to install Python 3 environment. The current version has been tested on Python 3.7. It is recommended to install Python virtual environment for the tool. Furthermore, we used bash shell scripts to automate running benchmark and Python scripts. Below are step-by-step instructions to setup environment and run the tool. 

### Environment Setup

Follow these steps to create a virtual environment and clone the Fairify repository. 

Notice: there isn't any specific requirement for system, only need a virtual environment with ``Python 3.8``.

1. Clone this repository and move to the directory:

```
git clone https://github.com/Elio-yang/nn-verification
cd nn-verification/
``` 

2. Run this on command line to create a virtual environment:

```
conda create --name fenv python=3.8
conda activate fenv
```

Run the following command to update pip on Python: `python3 -m pip install --upgrade pip`. Alternatively, you can follow the [Python documentation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) to install virtual environment on your machine. 

3. Navigate to the cloned repository: `cd fairify/` and install required packages:

```
pip install -r requirements.txt
```

## Verify 

Locate the verify scipts in [src](src/):

1. Verify Sex fairness on AC: [verify-ac-sex.py](src/AC/Verify-AC-sex.py)
2. Verify Reace fairness on AC: [verify-ac-race.py](src/AC/Verify-AC-race.py)
3. Verify Marital fairness on AC: [verify-ac-sex.py](src/AC/Verify-AC-marital.py)
4. Verify Age fairness on BD: [verify-bd-age.py](src/BD/Verify-BD-age.py)
5. Verify Education fairness on BD: [verify-bd-edu.py](src/BD/Verify-BD-edu.py)
6. Verify Housing fairness on BD: [verify-bd-housing.py](src/BD/Verify-BD-housing.py)
7. Verify Marital fairness on BD: [verify-bd-marital.py](src/BD/Verify-BD-marital.py)
8. Veridy Age fairness on BM: [verify-bm-age.py](src/BM/Verify-BM-age.py)
9. Veridy Loan fairness on BM: [verify-bm-loan.py](src/BM/Verify-BM-loan.py)
10. Verify V24 fairness on CF: [verify-cf-v24.py](src/CF/Verify-CF-v24.py)

Output will just be in the same directory, start with protected attribute. Detailed meaning of record in the output will be talked in the next section.

You could modify the verify python file to test other ``protected attribute``. You can also change the verification ``timeout`` in each file to provide longer time searching and verifing.


## Output

Sample output could be find [here](src/AC/sex-AC-1.csv), the first line of this file has indicated the meaning of numbers in this column. For example, the notation here would be 

```
Partition_ID,Verification,SAT_count,UNSAT_count,UNK_count,h_attempt,h_success,B_compression,S_compression,ST_compression,H_compression,T_compression,SV-time,S-time,HV-Time,H-Time,Total-Time,C-check,V-accurate,Original-acc,Pruned-acc,Acc-dec,C1,C2
```

and a sample verification result would look like this:

```
1,sat,1,0,0,0,0,0.56,0.0,0.56,0,0.56,51.657,52.12,0,0.0,52.12,1,1,0.8524,1.0,-,[51.  0.  8. 11.  6.  0.  0.  1.  1.  0. 19. 73. 39.],[51.  0.  8. 11.  6.  0.  0.  1.  0.  0. 19. 73. 39.]
```

We could match this result to the most important columns:

``Partition_ID = 1``:  The first trial


``Verification = sat``: Satisfied

``SAT_count = 1``: How many SAT cases

``UNSAT_count``: How many UNSAT cases

``UNK_count``: How many UNKOWN cases

And ``C1``, ``C2`` give you the counter-example:

``C1 = [51.  0.  8. 11.  6.  0.  0.  1.  1.  0. 19. 73. 39.]``

``C2 = [51.  0.  8. 11.  6.  0.  0.  1.  0.  0. 19. 73. 39.]``

In this case, C1[8]!=C2[8], but C1[!8]=C2[!8], but the network predict different result, showing unfair on attribute[8], in this case ``age``.


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