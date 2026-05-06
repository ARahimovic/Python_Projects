import argparse

"""
ARGPARSE GUIDE:
==============
argparse is a Python module for parsing command-line arguments and options.

1. CREATE A PARSER:
   parser = argparse.ArgumentParser(prog="name", description="...", epilog="...")

2. POSITIONAL ARGUMENTS (required):
   parser.add_argument('name', help="description")
   Usage: python script.py value

3. OPTIONAL ARGUMENTS (flags):
   parser.add_argument('-f', '--flag', help="description")
   parser.add_argument('-v', '--verbose', action='store_true', help="boolean flag")
   parser.add_argument('-m', '--message', required=True, help="required option")
   Usage: python script.py -f value or --flag value

4. SUBCOMMANDS (like git add, git commit):
   subparsers = parser.add_subparsers(dest="command", help="available commands")
   sub1 = subparsers.add_parser('add', help="...")
   sub1.add_argument('path', help="...")
   Usage: python script.py add filepath

5. PARSE ARGUMENTS:
   args = parser.parse_args()
   Access via: args.name, args.flag, args.command
"""

# parser = argparse.ArgumentParser(prog="Tuto Parser", description="Learning how to use argParse", epilog="And that is how we do it")
# parser.add_argument('userName', help="enter user name")
# parser.add_argument('-v', '--verbose', action='store_true', help="Make it longer and prettier")

# args = parser.parse_args()

# if args.verbose :
#     print(f"usre name : {args.userName} is using this program")
# else :
#     print(args.userName)



# mini git
parser = argparse.ArgumentParser(prog="mini git", description="mimicking git commands")
subparsers = parser.add_subparsers(dest="command", help="available commands")

add_parser = subparsers.add_parser('add', help="add Files to staging")
add_parser.add_argument("path", help="Path to the file you want to add")


commit_parser = subparsers.add_parser("commit", help="commit staged files")
commit_parser.add_argument('-m', "--message", required = True, help="Commit message")


args = parser.parse_args()

if args.command == 'add' :
    print(f"adding file : {args.path}")
elif args.command == 'commit':
    print(f"commiting with message {args.message}")
else :
    parser.print_help()


