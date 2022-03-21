

# javascript processor

[In short]

I am trying to add JavaScript support for the TransCoder (it only support python, java, cpp). To do this I need to provide a javascript processor.

To create a javascript processor I can make use of the javascript treesitter and the provided tree_sitter_processor.py,  once I git clone the javascript treesitter, the TreeSitterLangProcessor will make use of the treesitter and do what it needs to do accordingly.  https://github.com/tree-sitter/tree-sitter-javascript

So from what I understood, I just need to provide three variables to my javascript_processor.py class, similar to the java_processor.py and cpp_processor.py (their python processor is not inherited from TreeSitterLangProcessor):
 - TOKJAVASCRIPT_TOKEN2CHAR
 - JAVASCRIPT_CHAR2TOKEN
 - JAVASCRIPT_AST_NODES_TYPE_STRING

But I can't find out how I can know what to store in those three variables, could you please give me a hint?

for example:
 - why java processor has `character_literal` in its ast_nodes_type_string but cpp uses `char_literal`, how can I find the correct name to describe character literal for javascript?
 - in JAVA_TOKEN2CHAR, "STOKEN00" corresponding to "//", how can I find the mapping?


[Context]

I am trying to create a javascript processor as one step of adding a new language for the TransCoder software(steps were kindly listed by the author in one of their issue(https://github.com/facebookresearch/CodeGen/issues/42) ).

From what I understood, to create a javascript_processor.py, the easiest way is to utilize the TreeSitter and the tree_sitter_processor.py provided by the paper author in the directory `codegen_sources/preprocessing/lang_processors/`, github link to this folder is https://github.com/ziwenyd/CodeGen/blob/main/codegen_sources/preprocessing/lang_processors/tree_sitter_processor.py


The language processor must have these three functions:
- tokenize_code
- detokenize_code
- extract_functions

extract_functions is not needed if we train the model on file level, however the TransCoder paper actually train and evaluate their model on function level, so I think I better implement this function and train & evaluate on function level as well (Tree2Tree is also on function level, better for comparison as well).


  - their Python processor was built on the tokenizer of the standard library for Python (https://docs.python.org/3/library/tokenize.html), didn't make use of the tree_sitter_processor
  - their Java and Cpp processor are both inherited from the tree_sitter_processor. So I am trying to do the same for my JavaScript processor.


[My Question]

I created a javascript_processor in the same directory, initally just copied the java_processor.py.  https://github.com/ziwenyd/CodeGen/blob/main/codegen_sources/preprocessing/lang_processors/javascript_processor.py

I looked into the java_processor and cpp_processor to try to understand how they make use of the tree_sitter_processor.

For extract_functions() func: looks like I just need to modify it based on javascript syntax to allow the function detect class-functions and standalone-functions.

For tokenize_code() and detokenize_code() functions:

Looks like I need to supply the class with the below init params of TreeSitterLangProcessor class, 
 - TOKJAVASCRIPT_TOKEN2CHAR
 - JAVASCRIPT_CHAR2TOKEN
 - JAVASCRIPT_AST_NODES_TYPE_STRING

But I checked the repository and the paper again, didn't find anything indicates what those three represent and how I can obtain the same info for another language(javascript). Could you please give me a hint on this?




