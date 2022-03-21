from codegen_sources.preprocessing.lang_processors.tree_sitter_processor import (
    TreeSitterLangProcessor,
    NEW_LINE,
)
from codegen_sources.preprocessing.obfuscation.utils_deobfuscation import dico_to_string
# from codegen_sources.preprocessing.obfuscation import javalang_obfuscator

from codegen_sources.preprocessing.lang_processors.tokenization_utils import (
    ind_iter,
    NEWLINE_TOKEN,
)
import re

# don't know what to put in for javascript token2char, below is an example taken from the java processor
# JAVA_TOKEN2CHAR = {
#     "STOKEN00": "//",
#     "STOKEN01": "/*",
#     "STOKEN02": "*/",
#     "STOKEN03": "/**",
#     "STOKEN04": "**/",
#     "STOKEN05": '"""',
#     "STOKEN06": "\\n",
#     "STOKEN07": "\\r",
#     "STOKEN08": ";",
#     "STOKEN09": "{",
#     "STOKEN10": "}",
#     "STOKEN11": r"\'",
#     "STOKEN12": r"\"",
#     "STOKEN13": r"\\",
# }
JAVASCRIPT_TOKEN2CHAR = {}
JAVASCRIPT_CHAR2TOKEN = {value: " " + key + " " for key, value in JAVASCRIPT_TOKEN2CHAR.items()}

# don't know what to put here for javascript, below is an example taken from the java processor
# ast_nodes_type_string=["comment", "string_literal", "character_literal"]
JAVASCRIPT_AST_NODES_TYPE_STRING = [] 


class JavaScriptProcessor(TreeSitterLangProcessor):
    # compulsory functions to successfully run the process.py pipeline
    #   tokenize_code
    #   detokenize_code
    #   extract_functions 
    # fun `extract_functions` is not needed if only translate at file level instead of function level.
    #                         However, as stated in the TransCoder paper, 
    #                                  Facebook train an evaluate the translation model on functions only. 
    #                         So I should have this function as well in order to match the original paper.
    #                         - functions are differentiated by two types: class functions and standalone functions.
    #                                    

    def __init__(self, root_folder):
        super().__init__(
            language="javascript",
            ast_nodes_type_string=JAVASCRIPT_AST_NODES_TYPE_STRING,
            stokens_to_chars=JAVASCRIPT_TOKEN2CHAR,
            chars_to_stokens=JAVASCRIPT_CHAR2TOKEN,
            root_folder=root_folder,
        )

    # def obfuscate_code(self, code):
    #     res, dico = javalang_obfuscator.obfuscate(code)
    #     return res, dico_to_string(dico)

    def extract_functions(self, tokenized_code):
        # [NOTE] below is copied from java processor, need to be updated for javascript.
        """Extract functions from tokenized Java code"""
        if isinstance(tokenized_code, str):
            tokens = tokenized_code.split()
        else:
            assert isinstance(tokenized_code, list)
            tokens = tokenized_code
        i = ind_iter(len(tokens))
        functions_standalone = []
        functions_class = []
        try:
            token = tokens[i.i]
        except KeyboardInterrupt:
            raise
        except:
            return [], []

        while True:
            try:
                # detect function
                tokens_no_newline = []
                index = i.i
                while index < len(tokens) and len(tokens_no_newline) < 3:
                    index += 1
                    if tokens[index].startswith(NEWLINE_TOKEN):
                        continue
                    tokens_no_newline.append(tokens[index])

                if token == ")" and (
                    tokens_no_newline[0] == "{"
                    or (
                        tokens_no_newline[0] == "throws" and tokens_no_newline[2] == "{"
                    )
                ):
                    # go previous until the start of function
                    while token not in [";", "}", "{", "*/", "ENDCOM", NEW_LINE, "\n"]:
                        i.prev()
                        token = tokens[i.i]

                    if token == "*/":
                        while token != "/*":
                            i.prev()
                            token = tokens[i.i]
                        function = [token]
                        while token != "*/":
                            i.next()
                            token = tokens[i.i]
                            function.append(token)
                    elif token == "ENDCOM":
                        while token != "//":
                            i.prev()
                            token = tokens[i.i]
                        function = [token]
                        while token != "ENDCOM":
                            i.next()
                            token = tokens[i.i]
                            function.append(token)
                    else:
                        i.next()
                        token = tokens[i.i]
                        function = [token]

                    while token != "{":
                        i.next()
                        token = tokens[i.i]
                        function.append(token)
                    if token == "{":
                        number_indent = 1
                        while not (token == "}" and number_indent == 0):
                            try:
                                i.next()
                                token = tokens[i.i]
                                if token == "{":
                                    number_indent += 1
                                elif token == "}":
                                    number_indent -= 1
                                function.append(token)
                            except StopIteration:
                                break
                        if "static" in function[0 : function.index("{")]:
                            functions_standalone.append(
                                self.remove_annotation(" ".join(function))
                            )
                        else:
                            functions_class.append(
                                self.remove_annotation(" ".join(function))
                            )
                i.next()
                token = tokens[i.i]
            except KeyboardInterrupt:
                raise
            except:
                break
        return functions_standalone, functions_class

    # def remove_annotation(self, function):
    #     return re.sub(
    #         r"^@ (Override|Deprecated|SuppressWarnings) (\( .*? \) )", "", function
    #     )

    def get_function_name(self, function):
        return self.get_first_token_before_first_parenthesis(function)

    def extract_arguments(self, function):
        return self.extract_arguments_using_parentheses(function)
