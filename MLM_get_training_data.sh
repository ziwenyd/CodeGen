# under the root folder 'CodeGen'
# raw dataset path: my_data/raw
python3 -m codegen_sources.preprocessing.preprocess my_data/raw \                               
--langs python javascript \                         
--mode monolingual \                             
--local True \                                      
--bpe_mode fast_bpe \ 
--train_splits 0 \                               

#The pipeline extracts source code from json, 
#tokenizes it, extracts functions, applies bpe, 
#binarizes the data and creates symlink with appropriate name to be used directly in XLM. 

#The folder that ends with .XLM-syml is the data path you give for XLM traning. 
#You will have to add the test and valid parallel we provide in "Run an evaluation" data to that folder.


#sample command below
python -m preprocessing.preprocess 
absolute_path_to_TranscCoder/data/test_dataset # path to the root folder where you have the json
--lang1 java # languages to prepocess
--lang2 python #
--lang3 cpp # can be None if you want to preprocess only 2 languages
--keep_comments True # True if you want to keep code comments in you code, False to remove them
--bpe_train_size 0 # Set the size of the training data subset on which the bpe codes are trained. 0 -> parameter disabled and all training data are used
--test_size 10 # size of test/validation sets , usually 1000, here 10 to test the command on the json samples
--local True # True if you want to launch the pipeline locally , False to launch on remote machine. In that case it uses submitit
