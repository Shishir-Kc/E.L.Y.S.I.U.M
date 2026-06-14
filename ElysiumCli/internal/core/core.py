from commands.help.help import help
from commands.system_info.sys_info import system_info

def logic(user_input:str):
    if user_input == "help":
        print(help())
    elif user_input == "stats":
        print(system_info())

def main():

    while True:
        user_input = input("E.L > ")
        logic(user_input)
