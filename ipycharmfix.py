# ipycharmfix.py

def fixipycharm(curframe, subdirname ="code"):
    """
    Forces PyCharm to include subdirname in IPython moduel include path and
    changes the current working directory to subdirname.

    Args:
        curframe: callers stack frame from which module folder will be extracted
        subdirname: desired subdir name

    Returns:
        current working directory path text

    Notes:
        Usage:
            import inspect, ipycharmfix
            ipycharmfix.fixipycharm(inspect.currentframe())
        This function:
            - does not effect include path if subdirname already in it
            - does not change current working directory if it is already subdirname
            - may be a workaround for a bug in PyCharm IPython operation
        Implementation based on:
            http://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
            http://stackoverflow.com/questions/1250103/attributeerror-module-object-has-no-attribute
    """
    import os, sys, inspect
    cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( curframe ))[0]))
    if cmd_folder not in sys.path:
        sys.path.insert(0, cmd_folder)
    if(not cmd_folder.endswith(subdirname)):
        cmd_folder = os.path.realpath(os.path.abspath(os.path.join(cmd_folder, subdirname)))
        if cmd_folder not in sys.path:
            sys.path.insert(0, cmd_folder)
    cwd = os.getcwd()
    if(not cwd.endswith(subdirname)):
        os.chdir(cmd_folder)
    # print(os.getcwd())
    # print("\n".join(sys.path))
    return os.getcwd()