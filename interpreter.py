import sys

# Memory
MEMORY_SIZE = 65536
memory = []
ptr_instruction = 0
ptr_mem = 0

for i in range(MEMORY_SIZE):
    memory.append(0)

loops = []
saved_pointers = []
# A saved pointer is a tuple of (type: str, ptr value: int, name: str)

# Read program
program = list(open(sys.argv[1]).read())

# Run program
while ptr_instruction != len(program):
    instruction = program[ptr_instruction]
    if instruction == "#":
        while True:
            ptr_instruction += 1
            if (program[ptr_instruction] == "\n" or ptr_instruction == len(program) - 1):
                break
    elif instruction == "%":
        # Data pointer saving
        varname = ""
        while True:
            ptr_instruction += 1
            if program[ptr_instruction].isalpha():
                varname += program[ptr_instruction]
            else:
                break
        saved_pointers.append(("data", ptr_mem, varname))
    elif instruction == "&":
        if loops != []:
            print("INTERPRETER ERROR: Loop not closed, cannot save instruction pointer ({})".format(ptr_instruction))
            sys.exit(1)
        varname = ""
        while True:
            ptr_instruction += 1
            if program[ptr_instruction].isalpha():
                varname += program[ptr_instruction - 1]
            else:
                break
        # Instruction pointer saving
        saved_pointers.append(("instruction", ptr_instruction, varname))
    elif instruction == "!":
        varname = ""
        while True:
            ptr_instruction += 1
            if program[ptr_instruction].isalpha():
                varname += program[ptr_instruction]
            else:
                break
        for pointer in saved_pointers:
            if pointer[2] == varname:
                if pointer[0] == "data":
                    ptr_mem = pointer[1]
                    break
                elif pointer[0] == "instruction":
                    ptr_instruction = pointer[1]
                    loops = []
                    break
    elif instruction == "^":
        charstoprint = ""
        while True:
            ptr_instruction += 1
            if program[ptr_instruction] == "^":
                break
            else:
                charstoprint += program[ptr_instruction]
        charstoprint = charstoprint.replace("\\n", "\n")
        print(charstoprint, end="")
    elif instruction == "~":
        print(int(memory[ptr_mem]), end="")
    elif instruction == "=":
        # Hard set memory value
        while True:
            ptr_instruction += 1
            memory[ptr_mem] = int(program[ptr_instruction])
            if not program[ptr_instruction + 1].isnumeric():
                break
    elif instruction == "+":
        memory[ptr_mem] += 1
    elif instruction == "-":
        memory[ptr_mem] -= 1
    elif instruction == "<":
        ptr_mem -= 1
    elif instruction == ">":
        ptr_mem += 1
    elif instruction == ".":
        print(chr(memory[ptr_mem]), end="")
    elif instruction == ",":
        memory[ptr_mem] = int(ord(input("")[0]))
    elif instruction == "[":
        loops.append(ptr_instruction)
    elif instruction == "]":
        if memory[ptr_mem] == 0:
            loops.pop()
        else:
            ptr_instruction = loops[-1]
    ptr_instruction += 1