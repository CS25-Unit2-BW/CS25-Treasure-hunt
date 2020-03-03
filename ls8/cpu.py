import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
     # inside def __init__(self): of the CPU class
        # add ram property with empty list that holds 256 bites 
        self.ram = [0] * 256
        # add reg property with a list of 8 zeros (reg = [0] * 8)
        self.reg = [0] * 8
        # add properties for internal registers
        # pc - program counter, address of the current executing instruction
        self.pc = 0
        # add a branch table set to an empty dictionary
        self.branchtable = {}
        # add properties that call each instruction and it's helper function (HLT, LDI, PRN) for...
        # MUL we will call the alu still
        self.halted = True
        self.sp = 7
        self.reg[self.sp] = 0xF4
        self.fl = 0b00000000

    def load(self):
        """Load a program into memory."""

        address = 0

    # Inside the load() method
        # if there is no sys.argv[1]
        if len(sys.argv) == 1:
            # print an error message
            print("Proper Usage: python/python3 <filename>")
        # else Open a file dynamically from examples directory (using sys.argv[1])
        else:
            with open(sys.argv[1]) as f:
                # for every line in this file
                for line in f:
                    # slice out everything that is after a '#' and strip the white space 
                    new_line = line.split('#')[0].strip()
                    # print(new_line)
                    # if it is a blank line
                    if new_line == '':
                        # ignore it (continue)
                        continue
                    # convert the binary number to an interger
                    instruction = int(new_line, 2)
                    # save it to the ram at the current address
                    self.ram[address] = instruction
                    # increment address
                    # print(address, self.ram[address])
                    address += 1


    # add ram_read() method - takes in address to read from mar
    def ram_read(self, mar):
        # create a variable called value and assign it to the value located in the RAM at specific address passed in
        value = self.ram[mar]
        # return value from RAM
        return value

    # add ram_write() method - takes in value to write from mdr, and address to write too from mar
    def ram_write(self, mdr, mar):
        # writes the value to the ram at the specific address passed in
        self.ram[mar] = mdr

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # else if op == "MUL"
        elif op == "MUL":
            # get value from reg A and get value from reg B, mulitply and assign to reg A
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == "CMP":
            if self.reg[reg_a] == self.reg[reg_b]:
                self.fl = 0b00000001
            # elif reg_a < reg_b:
            #     self.fl = 0b00000100
            # elif reg_a > reg_b:
            #     self.fl = 0b00000010
            # else:
            #     self.fl = 0b00000000
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()
    
    # inside the cpu class
    # add a helper function for HLT
    def handle_hlt(self, operand_a, operand_b):
        # include the logic from the is statement in run()
        self.halted = True
        self.pc += 1
      
    # add a helper function for LDI
    def handle_ldi(self, operand_a, operand_b):
        # include the logic from the is statement in run()
        self.reg[operand_a] = operand_b
        self.pc += 3
     
    # add a helper function for PRN
    def handle_prn(self, operand_a, operand_b):
        # include the logic from the is statement in run()
        reg_num = operand_a
        print(self.reg[reg_num])
        self.pc += 2
    
    def handle_mul(self, operand_a, operand_b):
        self.alu("MUL", operand_a, operand_b)
        self.pc += 3

    def handle_push(self, operand_a, operand_b):
        # decrement stack pointer
        self.reg[self.sp] -= 1
        # copy the value into the register at the sp
        reg_num = operand_a
        reg_val = self.reg[reg_num]
        self.ram[self.reg[self.sp]] = reg_val
        # increment pc
        self.pc += 2

    def handle_pop(self, operand_a, operand_b):
        # grab value at the top of the stack
        val = self.ram[self.reg[self.sp]]
        # copy the value from the stack into the given register
        reg_num = operand_a
        self.reg[reg_num] = val
        # increment sp
        self.reg[self.sp] += 1
        # increment pc
        self.pc += 2

    def handle_call(self, operand_a, operand_b):
        # push return address onto stack
        ret_add = self.pc + 2 # next instruction in the stack
        # decrement sp
        self.reg[self.sp] -= 1
        self.ram[self.reg[self.sp]] = ret_add
        # set the pc to the value in the register
        reg_num = operand_a
        self.pc = self.reg[reg_num]

    def handle_ret(self, operand_a, operand_b):
        # pop the return address off the stack
        # store it in the pc
        self.pc = self.ram[self.reg[self.sp]]
        self.reg[self.sp] += 1

    def handle_add(self, operand_a, operand_b):
        self.alu("ADD", operand_a, operand_b)
        self.pc += 3
    
    '''
    SPRINT handlers
    '''
    def handle_cmp(self, operand_a, operand_b):
        # print ("comparing")
        self.alu("CMP", operand_a, operand_b)
        self.pc += 3

    def handle_jmp(self, operand_a, operand_b):
        # set the pc to the address stored at the given register
        reg_num = operand_a
        self.pc = self.reg[reg_num]

    def handle_jeq(self, operand_a, operand_b):
        # if the equal flag is true (00000001)
        # print(f" inside jeq but outside if statement {operand_a}")
        # print(f"in jeq {self.fl}")
        if self.fl == 0b00000001:
            # jump to the address stored in the given register
            reg_num = operand_a
            # print(reg_num)
            self.pc = self.reg[reg_num]
        else:
            self.pc += 2

    def handle_jne(self, operand_a, operand_b):
        # If E flag is clear (00000010 OR 00000100)
        if self.fl != 0b00000001 :
        # jump to the address stored in the given register.
            # print(f"in JNE")
            reg_num = operand_a
            self.pc = self.reg[reg_num]
        else: 
            self.pc += 2

    '''
    STRETCH handlers
    '''
    # def handle_addi(self, operand_a, operand_b):
    #     pass


    def run(self):
        """Run the CPU."""
    # inside the run() method
        # add HLT definition
        HLT = 0b00000001
        # add LDI definition
        LDI = 0b10000010
        # add PRN definition
        PRN = 0b01000111
        # add MUL to the instructions list with machine code 0b10100010
        MUL = 0b10100010
        # add push and pop definitions
        PUSH = 0b01000101
        POP = 0b01000110
        # add call and ret definitions
        CALL = 0b01010000
        RET = 0b00010001
        ADD = 0b10100000
        # SPRINT
        CMP = 0b10100111
        JMP = 0b01010100
        JEQ = 0b01010101
        JNE = 0b01010110

        # add each instruction and it's helper function (HLT, LDI, PRN) to the branch table
        # MUL we will call the alu still
        self.branchtable[HLT] = self.handle_hlt
        self.branchtable[LDI] = self.handle_ldi
        self.branchtable[PRN] = self.handle_prn
        self.branchtable[MUL] = self.handle_mul
        self.branchtable[PUSH] = self.handle_push
        self.branchtable[POP] = self.handle_pop
        self.branchtable[CALL] = self.handle_call
        self.branchtable[RET] = self.handle_ret
        self.branchtable[ADD] = self.handle_add
        # SPRINT 
        self.branchtable[CMP] = self.handle_cmp
        self.branchtable[JMP] = self.handle_jmp
        self.branchtable[JEQ] = self.handle_jeq
        self.branchtable[JNE] = self.handle_jne
        # STRETCH
        # self.branchtable[ADDI] = self.handle_addi

        
        # set halted to False
        self.halted = False

        # while not halted
        while not self.halted:
            # read memory address stored in pc & store result in variable ir
            ir = self.ram_read(self.pc)
            # print(f"in loop {ir}")
            # use ram_read() method and pass in pc+1 and store in variable operand_a
            operand_a = self.ram_read(self.pc+1)
            # print(operand_a)
            # use ram_read() method and pass in pc+2 and store in variable operand_b
            operand_b = self.ram_read(self.pc+2)
            # print(operand_b)
            # instead of the casscading if statments call the branchtable with the specific op (set to ir)
            self.branchtable[ir](operand_a, operand_b)

            # how to implement without a branchtable
            # if ir == HLT 
            # if ir == HLT:
            #     # to exit the loop by changing halted to True
            #     halted = True
            #     # increment pc by 1 bite
            #     self.pc += 1
            # # else if ir == LDI
            # elif ir == LDI:
            #     # store the 8 value in a given register
            #     self.reg[operand_a] = operand_b
            #     # increment pc by 3 bites
            #     self.pc += 3
            # # else if ir == PRN
            # elif ir == PRN:
            #     # print the value in a register
            #     reg_num = operand_a
            #     print(self.reg[reg_num])
            #     # increment pc by 2 bites
            #     self.pc += 2
            # # if the ir is equal to the MUL
            # elif ir == MUL:
            #     # invoke alu(op,reg_a, reg_b)
            #     self.alu("MUL", operand_a, operand_b)
            #     # increment pc by 3
            #     self.pc += 3
            # otherwise
            # else:
            #     # print error message
            #     print(f"No instructrion found at index {self.pc}")
            #     halted = True