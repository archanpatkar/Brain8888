    # def parse(self,tokens):
    #     ast = { "type":"Root" , "children":[] };
    #     i = 0;
    #     while i < len(tokens):
    #         token = tokens[i];
    #         # if(token.type == "Loop-Start"):
    #         #     node = {"type":"Loop" , "children":[]}
    #         #     while token.type !=  "Loop-End":
    #         #         if(token.type == "Loop-Start"):
    #         #             node = self.parse(tokens[i+1:]);
    #         #         else:
    #         #             node.get("children").append({ "operation":token.type , "symbol": token.symbol });
    #         #             i += 1;
    #         #             token = tokens[i];
    #             # node["children"] = node.get("children")[1:-1];
    #             # ast.get("children").append(node);
    #         # else:
    #         ast.get("children").append({ "operation":token.type , "symbol": token.symbol });
    #         i += 1;
    #     return ast;

    # def interpret(self,code):
    #     self.program_counter = 0;
    #     instructions = code.get("children");
    #     while self.program_counter < len(instructions):
    #         token = instructions[self.program_counter];
    #         print(token);
    #         if token["operation"] == "Forward" :
    #             self.current += 1;
    #             self.tape.append(0);
    #         elif token["operation"] == "Backward" :
    #             self.current -= 1;
    #         elif token["operation"] == "Increment" :
    #             self.tape[self.current] += 1;
    #         elif token["operation"] == "Decrement" :
    #             if self.current > 0 :
    #                 self.tape[self.current] -= 1;
    #             else :
    #                 raise BaseException("Tape Already At The Start!");
    #         elif token["operation"] == "Print" :
    #             num = self.tape[self.current];
    #             if num >= 0:
    #                 print(chr(num), end='');
    #         elif token["operation"] == "Read" :
    #             self.tape[self.current] = ord(input()[0]);
    #         elif token["operation"] == "Loop-Start" :
    #             while self.tape[self.current] != 0 :
    #                 loop = token.get("children");
    #                 counter = 0;
    #                 while top.type != "Loop-End" :
    #                     counter += 1;
    #                     top = loop[counter];
    #                     self.interpret({ "operation":"Step" , "children": [top]});
    #         elif token["operation"] == "Loop-End" :
    #             raise BaseException("Unexpected ']'");
    #         self.program_counter += 1;


    # def interpret(self,code):
    #     self.program_counter = 0;
    #     while self.program_counter < len(code):
    #         char = code[self.program_counter]
    #         if(char == '['):
    #             self.program_counter += 1;
    #             while self.tape[self.current] != 0:
    #                 self.iteration(code,self.program_counter)
    #         else:
    #             self.each(char);
    #         self.program_counter += 1;
    #
    # def each(self,char):
    #     if(char == '>'):
    #         self.current += 1;
    #         self.tape.append(0);
    #     elif(char == '<'):
    #         if(self.current > 0):
    #             self.current -= 1;
    #     elif(char == '+'):
    #         self.tape[self.current] += 1;
    #     elif(char == '-'):
    #         self.tape[self.current] -= 1;
    #     elif(char == '.'):
    #         num = self.tape[self.current];
    #         if num >= 0:
    #             print(chr(self.tape[self.current]), end='');
    #     elif(char == ','):
    #         self.tape[self.current] = ord(input()[0]);
    #
    #
    # def iteration(self,code,start):
    #     char = code[self.program_counter];
    #     while(char != ']'):
    #         self.interpret(char);
    #         self.program_counter += 1;
    #         char = code[self.program_counter];
    #     self.program_counter = start;

    # def loop(self,code,start):
    #     char = '';
    #     end = 0;
    #     while self.program_counter < len(code):
    #         char = code[self.program_counter];
    #         if(self.tape[self.current] == 0):
    #             self.program_counter = end;
    #             return;
    #         if(char == '[' and self.tape[self.current] != 0):
    #             self.program_counter += 1;
    #             self.loop(code,self.program_counter);
    #         if(char == ']' and self.tape[self.current] != 0):
    #             end = self.program_counter;
    #             self.program_counter = start;
    #             char = code[self.program_counter];
    #             self.each(char);
    #         else:
    #             self.each(char);
    #         self.program_counter += 1;



# loop = [];
                # tok = tokens[ip]
                # ip += 1
                # while tok.type != "Loop-End" and ip < len(tokens):
                #     loop.append(tok);
                #     tok = tokens[ip];
                #     ip += 1;
                # main.append(self.parse(loop));


 # ip = 0;
        # main = [];
        # while ip < len(tokens):
        #     tok = tokens[ip];
        #     ip += 1
        #     if(tok.type == "Loop-Start"):
        #         parent = main
        #         stack = []
        #         stack.append(tok)
        #         while ip < len(tokens):
        #             tok = tokens[ip]
        #             ip += 1
        #             if tok.type == "Loop-End":
        #                 loop = []
        #                 v = stack.pop()
        #                 while v.type != "Loop-Start":
        #                     loop.append(v)
        #                     v = stack.pop()
        #                 parent.append(loop)
        #                 parent = loop
        #             else:    
        #                 stack.append(tok)
        #     else:
        #         main.append(tok);
        # return main;