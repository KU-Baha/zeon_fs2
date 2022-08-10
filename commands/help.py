def docker_help(*args):
    if len(args) != 0:
        print("Help doesn't take any arguments!")
        return

    print("""
    Commands:
        init: initializing docker (Take 0 arguments)
        add: Add file to system (Take 1 argument - file_path)
        del: Delete file in system (Take 
    """)