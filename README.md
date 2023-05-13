# Bird-Species-Classification

## Related works

The 2nd best model has provided their code. They first clean the audio data and then transform the audio data into spectrogram. They use the spectrogram as the input of the model. They deploy the PCA to do the classification.

Our goal is to deploy some deep learning models to do the classification. 

- []ResNet
- []LSTM
- []Transformer

## Dataset

In this competetion, only the labels of training set are provided, but the test set's labels are unknown. Then we divide the original training set into smaller training set and validation set and testing set for our experiments.

## Data Preprocessing

### Audio Data vs Image

## Tensorflow

https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM

## Evaluation

Receiver Operating Characteristic Curve


## AST for Kaggle

python3 gen_weight_file.py --data_path ./data/datafiles/train.json
python3 gen_weight_file.py --data_path ./data/datafiles/test.json 
python3 gen_weight_file.py --data_path ./data/datafiles/eval.json 

scp run.sh shyu0@linux9:/research/dept8/fyp22/lj2202/eleg5491/ast/egs/kaggle
scp "shyu0@linux9:/research/dept8/fyp22/lj2202/eleg5491/ast/egs/kaggle/log*" ./

srun --gres=gpu:1 -w gpu38 -p gpu_8h --pty /bin/bash 
conda activate eleg5491

cd eleg5491/ast/egs/kaggle/
sbatch ./run.sh 