#!/usr/bin/env python3
""" This file will be the reason for the Cli commands ! """

import argparse
from ElysiumCli.commands.elysium_info import (
    version , status ,
    last_development_changes , version_name ,
    is_stable , elysium_info , check_version  ,
    update
)

def build_parser(): 
    parser = argparse.ArgumentParser(prog="E.L.Y.S.I.U.M")
    subparser = parser.add_subparsers(dest="command")

    version_parser = subparser.add_parser("version")
    version_parser.set_defaults(func=version)
   
    status_parser = subparser.add_parser("status")
    status_parser.set_defaults(func=status)

    dev_parser =  subparser.add_parser("dev")
    dev_parser.set_defaults(func=last_development_changes)
    
    version_name_parser = subparser.add_parser("version_name")
    version_name_parser.set_defaults(func=version_name)

    stable_parser = subparser.add_parser("is_stable")
    stable_parser.set_defaults(func=is_stable)

    el_parser = subparser.add_parser("info")
    el_parser.set_defaults(func=elysium_info)

    version_checker_parser = subparser.add_parser("check_version")
    version_checker_parser.set_defaults(func=check_version)

    update_parser = subparser.add_parser("update")
    update_parser.set_defaults(func=update)
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)

if __name__ == "__main__":
    main()
