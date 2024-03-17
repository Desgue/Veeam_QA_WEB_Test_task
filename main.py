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

    # Parse command line arguments
    parser = cmd.configure_arg_parser()
    args = parser.parse_args()

    processes = args.processes
    is_headless = args.headless


    print(
        f"""
        Running test with {processes} processes
        Headless mode set to: {is_headless}
        """
    )

    # If no config file is provided, run default test with Romania and USA scope
    if not args.config:
        print(
            """
            No config file provided, running default test with Romania and USA scope
            """
            )
        cmd.run_default_test(
            headless = is_headless, 
            processes = processes
            )
        exit(1)
    
    path_to_config_file = Path(args.config)
    # If config file is not valid or does not exist, exit with a message
    if not path_to_config_file.exists():
        print(
            f""" 
            File '{args.config}' not found
            Please provide a valid file path and try again
            Exiting Program...
            """
            )

        exit(1)

    # Run test with config file
    print(
        f"""
        Running test with config file: {args.config}
        """
        )

    cmd.run_test_with_config_file(
        path_to_config_file = path_to_config_file, 
        headless= is_headless, 
        processes= processes
        )


if __name__ == '__main__':
    main()





