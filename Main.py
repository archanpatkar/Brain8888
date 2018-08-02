from Brain8888 import Brain8888
from pprint import pprint


LANG = Brain8888();

ast = LANG.parse(LANG.tokenize("+++++++++ [ ++ -- ]"))
pprint(ast, indent=4);




# LANG.repl();

# ast = LANG.parse(LANG.tokenize("+++++ +++++ [ > +++++ ++ > +++++ +++++ > +++ > + <<<< - ] > ++ . > + . +++++ ++ . . +++ . > ++ . << +++++ +++++ . > . +++ . ----- - . ----- --- . > + . > ."))
# ast = LANG.parse(LANG.tokenize("+++++ +++++ [ > +++++ ++ > +++++ +++++ > +++ > + <<<< - [>>>> +++++ -- . +++ --]]"))
# pprint(ast, indent=4);

# inter.interpret2(ast);
# +++++ +++++
# [
#     > +++++ ++
#     > +++++ +++++
#     > +++
#     > +
# <<<< -
# ]
# > ++ .
# > + .
# +++++ ++ .
# .
# +++ .
# > ++ .
# << +++++ +++++ +++++ .
# > .
# +++ .
# ----- - .
# ----- --- .
# > + .
# > .
