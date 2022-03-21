# under the root folder 'CodeGen'
# raw dataset path: my_data/raw
python3 -m codegen_sources.preprocessing.preprocess \
my_data/raw/raw_for_train \                               
--langs python javascript \                         
--mode monolingual \                                                            
--bpe_mode fast_bpe \ 
--local True \       
--train_splits 1 \                               

#The pipeline extracts source code from json, 
#tokenizes it, extracts functions, applies bpe, 
#binarizes the data and creates symlink with appropriate name to be used directly in XLM. 

#The folder that ends with .XLM-syml is the data path you give for XLM traning. 
#You will have to add the test and valid parallel we provide in "Run an evaluation" data to that folder.


#sample command below
"""
python -m codegen_sources.preprocessing.preprocess \
<DATA_PATH> \                            # folder containing json.gz
--langs java cpp python  \               # languages to process
--mode monolingual_functions \           # dataset mode
--bpe_mode=fast_bpe \                    # BPE mode. by default it is fast_BPE. can be roberta_bpe
--local=True \                           # Run on your local machine if True. If False run on a cluster (requires submitit setup)
--train_splits=1                         # Number of trainings splits
"""