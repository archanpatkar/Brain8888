import sys
from collections import namedtuple
from Panim import *
from pprint import pprint

Token = namedtuple('Token', 'type symbol')

class Brain8888:
    def __init__(self):
        self.tape = [0];
        self.current = 0;

    def reset(self):
        self.__init__()

    def tokenize(self,code):
        tokens = [];
        for char in code:
            if(char == ">"):
                tokens.append(Token("Forward",char));
            elif(char == "<"):
                tokens.append(Token("Backward",char));
            elif(char == "+"):
                tokens.append(Token("Increment",char));
            elif(char == "-"):
                tokens.append(Token("Decrement",char));
            elif(char == "."):
                tokens.append(Token("Print",char));
            elif(char == ","):
                tokens.append(Token("Read",char));
            elif(char == "["):
                tokens.append(Token("Loop-Start",char));
            elif(char == "]"):
                tokens.append(Token("Loop-End",char));
        return tokens;

    def parse(self,tokens):
        ip = 0
        stack = []
        while ip < len(tokens):
            tok = tokens[ip]
            ip += 1
            if(tok.type == "Loop-Start"):
                stack.append(tok)
            elif(tok.type == "Loop-End"): 
                loop = []
                v = stack.pop()
                while isinstance(v,list) or v.type != "Loop-Start":
                    loop.append(v)
                    v = stack.pop()
                stack.append(loop[::-1])
            else:
                stack.append(tok)
        return stack

    def get(self): return self.tape[self.current];

    def eval(self,code):
        program_counter = 0
        while program_counter < len(code):
            token = code[program_counter]
            if isinstance(token,list):
                while self.get() != 0:
                    self.eval(token);
            elif token.type == "Forward" :
                self.current += 1;
                if(self.current >= len(self.tape)):
                    self.tape.append(0);
            elif token.type == "Backward" :
                if self.current > 0 :
                    self.current -= 1;
                else :
                    raise BaseException("Tape Already At The Start!");
            elif token.type == "Increment" :
                self.tape[self.current] += 1;
            elif token.type == "Decrement" :
                self.tape[self.current] -= 1;
            elif token.type == "Print" :
                num = self.tape[self.current];
                if num >= 0 and num <= 256:
                    print(chr(num), end='');
            elif token.type == "Read" :
                self.tape[self.current] = ord(input());
            program_counter += 1;

    def execute(self,code):
        self.eval(self.parse(self.tokenize(code)))

    def repl(self):
        foreground(RED);
        print("Brain8888 0.0.1");
        print("Welcome Human 👋");
        print("");
        foreground(GREEN);
        read = input("> ");
        while read != "q" and read != "quit" and read != "exit" and read != "bye":
            if(read == "current position"):
                print("Position of Tape Head = ",self.current);
                print("Value of Current Cell = ",self.tape[self.current]);
            elif(read == "tape"):
                print(self.tape)
            elif(read == "reset"):
                self.reset();
            else:
                tokens = self.tokenize(read);
                ast = self.parse(tokens);
                self.eval(ast);
            read = input("> ");
        foreground(BLUE);
        print("");
        print("May We Meet Again 🖖");
        print("May the Force be with you ✋");
        foreground(WHITE);
        background(BLACK);

if __name__ == "__main__":
    interpreter = Brain8888()
    if len(sys.argv) > 1:
        code = open(sys.argv[1],"r").read()
        interpreter.execute(code)
    else:
        interpreter.repl()
