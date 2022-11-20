#!/usr/bin/env python3

from bits import VMCode


class testCode(VMCode):

    def writeArithmetic(self, command):
        commands = []
        if command == "delete":
            commands.append("")

        elif command == "add3":
            commands.append("")

        elif command == "swap":
            commands.append("")

        # não mexer
        self.commandsToFile(commands)
