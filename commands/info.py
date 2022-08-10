from helper.server import start_server


def info_helper(_, *args):
    if len(args) != 1:
        print("Info take 1 argument - ip:port or only port!")
        return

    arg = args[0].split(":")
    ip = ""

    if len(arg) == 2:
        ip, port = arg
    else:
        port = arg[1]

    start_server(ip, int(port))
