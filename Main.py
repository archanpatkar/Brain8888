from Brain8888 import Brain8888
from pprint import pprint

inter = Brain8888();

ast = inter.parse(inter.tokenize("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."))

pprint(ast, indent=4);

inter.interpret(ast);
