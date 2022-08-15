def docker_help(_, *args):
    if len(args) != 0:
        print("Help doesn't take any arguments!")
        return

    print("""
Commands:
    init: initializing docker (Take 0 arguments)
    add: Add file to system (Take 1 argument - file_path)
    del: Delete file in system (Take 1 argument - file_path in system)
    list: Show files in system (Take 0 argument)
    info: Run server (Take 1 argument like ip:port or only port)
    """)

