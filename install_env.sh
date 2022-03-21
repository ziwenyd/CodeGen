#pwd: /CodeGen
conda create --name codeGen_env python=3.6.9
# if `conda activate env` not working and shows the below error
# ``` CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'. ```
# Then you need to conda init first, run:
# bash `conda init <your_shell_name>`
# use `$ps -p $$` to see your shell name
conda activate codeGen_env
conda config --add channels conda-forge
conda config --add channels pytorch

conda install pytorch torchvision torchaudio cudatoolkit=11.0 six scikit-learn stringcase transformers ply slimit astunparse submitit
pip install cython
#pip3 install sacrebleu=="1.4.5" #Otherwise shows an import error
cd codegen_sources/model/tools
git clone https://github.com/glample/fastBPE.git

cd fastBPE
g++ -std=c++11 -pthread -O3 fastBPE/main.cc -IfastBPE -o fast
pip install fastBPE==v0.1.0
# python setup.py install
cd ../../../../

mkdir tree-sitter
cd tree-sitter
git clone https://github.com/tree-sitter/tree-sitter-cpp.git
git clone https://github.com/tree-sitter/tree-sitter-java.git
git clone https://github.com/tree-sitter/tree-sitter-python.git
cd ..

cd codegen_sources/test_generation/
wget https://github.com/EvoSuite/evosuite/releases/download/v1.1.0/evosuite-1.1.0.jar
cd ../..

git clone https://github.com/NVIDIA/apex
cd apex
pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
cd ..

pip install sacrebleu=="1.2.11" javalang tree_sitter psutil fastBPE
pip install hydra-core --upgrade --pre
pip install black==19.10b0

# --------------------------------
#pwd: /CodeGen
cd tree-sitter
git clone https://github.com/tree-sitter/tree-sitter-javascript
