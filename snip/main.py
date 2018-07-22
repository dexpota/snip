"""snip.

Usage: 
    snip <snippet>
    snip --edit <snippet>
    snip --list
    snip --version|-v

"""

from docopt import docopt
import itertools
import logging
import os


def main():
    arguments = docopt(__doc__)
    logging.basicConfig(level=logging.DEBUG)

    logging.debug("arguments: {}".format(arguments))

    snippets_home_path = os.environ.get("SNIPPETS_DIR", "~/.snippets")
    snippets_home_path = os.path.expandvars(snippets_home_path)
    snippets_home_path = os.path.expanduser(snippets_home_path)
    logging.debug("root directory: {}".format(snippets_home_path))

    if arguments["--list"]:
        # list all snippets

        if not os.path.isdir(snippets_home_path):
            logging.error("snippet directory doesn't exist: {}".format(snippets_home_path))
            exit(-1)

        for root, dirs, files in os.walk(snippets_home_path):
            dirs[:] = [d for d in dirs if not d.startswith(".")]
            files[:] = [file for file in files if not file.startswith(".")]

            for file in files:
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, snippets_home_path)
                print(relative_path)

    elif arguments["--edit"]:
        # edit the snippet
        snippet = arguments["<snippet>"]
        logging.debug("snippet: {}".format(snippet))
        raise NotImplementedError("edit functionality is not yet implemented.")
    else:
        # show the snippet
        snippet = arguments["<snippet>"]
        logging.debug("snippet: {}".format(snippet))
        raise NotImplementedError("print functionality is not yet implemented.")
    

if __name__ == "__main__":
    main()
