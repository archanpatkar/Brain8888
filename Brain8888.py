from collections import namedtuple
from Panim import *

Token = namedtuple('Token', 'type symbol')

class Brain8888:
    def __init__(self):
        self.tape = [0];
        self.current = 0;
        self.program_counter = 0;

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
        ip = 0;
        main = [];
        while ip < len(tokens):
            tok = tokens[ip];
            if(tok.type == "Loop-Start"):
                loop = [];
                while tok.type != "Loop-End" and ip < len(tokens):
                    tok = tokens[ip];
                    loop.append(tok);
                    ip = ip + 1;
                loop = loop[1:-1];
                main.append(self.parse(loop));
            else:
                main.append(tok);
            ip = ip + 1;
        return main;

    def eval(self,code):
        for token in code:
            # token = code[counter];
            if isinstance(token,list) :
                # print(token)
                # print(self.tape[self.current]);
                while self.tape[self.current] != 0:
                    # print(self.tape[self.current]);
                    self.eval(token);
            elif token.type == "Forward" :
                self.current += 1;
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
                if num >= 0:
                    print(chr(num), end='');
            elif token.type == "Read" :
                self.tape[self.current] = ord(input()[0]);
            self.program_counter += 1;

    def repl(self):
        foreground(RED);
        print("Brain8888 0.0.1");
        print("Welcome Human 👋");
        print("");
        foreground(GREEN);
        read = input("> ");
        while read != "q" and read != "quit" and read != "exit" and read != "bye":
            if(read == "current"):
                print("Position of Tape Head = ",self.current)
                print("Value of Current Cell = ",self.tape[self.current])
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
