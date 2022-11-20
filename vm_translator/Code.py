#!/usr/bin/env python3

from bits import VMCode


class testCode(VMCode):

    def writeArithmetic(self, command):
        commands = []
        if command == "delete":
            commands.append("leaw $0, %A")
            commands.append("movw (%A), %D")
            commands.append("subw %D, $1, %D")
            commands.append("leaw $0, %A")
            commands.append("movw %D, (%A)")

        elif command == "add3":
            commands.append("leaw $0, %A")
            commands.append("movw (%A), %A") # Read SP
            commands.append("subw %A, $1, %A") # Decrease 1 SP
            commands.append("movw (%A), %D") # Save SP-1 on D
            commands.append("subw %A, $1, %A") # Decrease 1 SP
            commands.append("addw %D, (%A), %D") # D = D + RAM[SP-2]
            commands.append("subw %A, $1, %A") # Decrease 1 SP
            commands.append("addw %D, (%A), %D") # D = D + RAM[SP-3]
            commands.append("movw %D, (%A)") # Move D to SP-3
            commands.append("incw %A") # Change SP to SP-2
            commands.append("movw %A, %D")
            commands.append("leaw $0, %A")
            commands.append("movw %D, (%A)") # Save new Stack Pointer

        elif command == "swap":
            commands.append("leaw $0, %A")
            commands.append("movw (%A), %A") # Save SP in A
            commands.append("subw %A, $1, %A") # Decrease 1 SP
            commands.append("movw (%A), %D") # Move SP-1 to D
            commands.append("incw %A") # A = SP - 1 + 1
            commands.append("movw %D, (%A)") # Save D to Last Value on Stack
            commands.append("subw %A, $1, %A")
            commands.append("subw %A, $1, %A") # Decrease 2 SP
            commands.append("movw (%A), %D") #Move SP-2 to D
            commands.append("incw %A") # Increase 1 SP
            commands.append("movw %D, (%A)") # Move SP-2 to SP-1
            commands.append("incw %A") # Increase 1 SP
            commands.append("movw (%A), %D") # Move SP to D
            commands.append("subw %A, $1, %A")
            commands.append("subw %A, $1, %A") # Decrease 2 SP
            commands.append("movw %D, (%A)") # Move SP-1 to SP-2

    # não mexer
        self.commandsToFile(commands)
