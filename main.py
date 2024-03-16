import cmd
from pathlib import Path

def main():
    print("""
 / \ -----------------------, 
 \ ,|                       | 
    |    VEEAM ASSESSMENT   | 
    |  ,----------------------
    \ /_____________________/ 
    """)

    parser = cmd.configure_arg_parser()
    args = parser.parse_args()

    print("Headless mode set to: ", args.headless)

    if not args.config:
        print("No config file provided, running default test with Romania and USA scope")
        cmd.run_default_test(headless = args.headless)
        exit(1)
    

    path_to_config_file = Path(args.config)
    if not path_to_config_file.exists():
        print(f"\nFile '{args.config}' not found")
        print("Please provide a valid file path and try again\n")
        exit(1)

    print(f"Running test with config file: {args.config}")



    cmd.run_test_with_config_file(path_to_config_file, args.headless)

if __name__ == '__main__':
    main()




