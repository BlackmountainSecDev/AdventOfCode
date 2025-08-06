def readTheFile(filename):
    with open(filename, 'r') as file:
        data = file.read()
    #with open('Resources/day17ResourceTraining.txt', 'r') as lines:
        return data


def part1():
    isTraining = False

    print('Part 1')

    if isTraining:
        data = readTheFile('Resources/day17ResourceTraining.txt')

    else:
        data = readTheFile('Resources/day17Resource.txt')


    splittedData = data.split('\n')

    waste, value = splittedData[0].split(':')
    registerA = int(value.strip())

    waste, value = splittedData[1].split(':')
    registerB = int(value.strip())

    waste, value = splittedData[2].split(':')
    registerC = int(value.strip())

    print(f'Register A: {registerA}')
    print(f'Register B: {registerB}')
    print(f'Register C: {registerC}')

    waste, instructions = splittedData[4].split(':')

    instructions = instructions.strip()

    print(f'Program: {instructions}')

    output = ''
    instructionPointer = 0
    while instructionPointer < len(instructions):
        currentCalc = instructions[instructionPointer:instructionPointer+3]
        instructionPointer += 4


        opcode, operand = currentCalc.split(',')
        opcode = int(opcode)
        operand = int(operand)


        if operand == 4:
            operand = registerA
        elif operand == 5:
            operand = registerB
        elif operand == 6:
            operand = registerC


        if opcode == 0:
            #print('adv')
            if operand != 0:
                registerA = registerA // pow(2, operand)
            else:
                registerA = 0

        elif opcode == 1:
            #print('bxl')
            registerB ^= operand

        elif opcode == 2:
            #print('bst')
            result = operand % 8
            registerB = result & 7

        elif opcode == 3:
            #print('jnz')
            if registerA != 0:
                instructionPointer = operand

        elif opcode == 4:
            #print('bxc')
            registerB ^=  registerC

        elif opcode == 5:
            #print('out')
            result = operand % 8
            if len(output) > 0:
                output = output +',' + str(result)
            else:
                output = str(result)

        elif opcode == 6:
            #print('bdv')
            if opcode != 0:
                registerB = registerA // pow(2, operand)
            else:
                registerB = 0

        elif opcode == 7:
            #print('cdv')

            if opcode != 0:
                registerC = registerA // pow(2, operand)
            else:
                registerC = 0



    print(f'registerA: {registerA}')
    print(f'registerB: {registerB}')
    print(f'registerC: {registerC}')
    print(f'Program: {output}')



def part2():
    isTraining = False

    print('Part 2')

    registerA = 0
    registerB = 0
    registerC = 0
    instructions = '2,4,1,2,7,5,4,5,0,3,1,7,5,5,3,0'

    print(f'Register A: {registerA}')
    print(f'Register B: {registerB}')
    print(f'Register C: {registerC}')
    print(f'Program: {instructions}')

    output = ''
    counter = 220807395

    while output != instructions:

        output = ''
        counter += 1

        registerA = counter
        registerB = 0
        registerC = 0

        print(f'Start Register A: {registerA}')

        instructionPointer = 0
        while instructionPointer < len(instructions):
            currentCalc = instructions[instructionPointer:instructionPointer+3]
            instructionPointer += 4


            opcode, operand = currentCalc.split(',')
            opcode = int(opcode)
            operand = int(operand)

            if operand == 4:
                operand = registerA
            elif operand == 5:
                operand = registerB
            elif operand == 6:
                operand = registerC


            if opcode == 0:
                #print('adv')
                if operand != 0:
                    registerA = registerA // pow(2, operand)
                else:
                    registerA = 0

            elif opcode == 1:
                #print('bxl')
                registerB ^= operand

            elif opcode == 2:
                #print('bst')
                result = operand % 8
                registerB = result & 7

            elif opcode == 3:
                #print('jnz')
                if registerA != 0:
                    instructionPointer = operand

            elif opcode == 4:
                #print('bxc')
                registerB ^=  registerC

            elif opcode == 5:
                #print('out')
                result = operand % 8
                if len(output) > 0:
                    output = output +',' + str(result)
                else:
                    output = str(result)

                if instructions.startswith(output) == False:
                    break


            elif opcode == 6:
                #print('bdv')
                if opcode != 0:
                    registerB = registerA // pow(2, operand)
                else:
                    registerB = 0

            elif opcode == 7:
                #print('cdv')

                if opcode != 0:
                    registerC = registerA // pow(2, operand)
                else:
                    registerC = 0



    print(f'registerA: {registerA}')
    print(f'registerB: {registerB}')
    print(f'registerC: {registerC}')
    print(f'Program: {output}')



if __name__ == '__main__':
    #part1()
    part2()