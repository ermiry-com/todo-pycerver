import signal

import cerver

import service
from todo import todo_config
import version

if __name__ == "__main__":
	signal.signal (signal.SIGINT, service.end)
	signal.signal (signal.SIGTERM, service.end)
	signal.signal (signal.SIGPIPE, signal.SIG_IGN)

	cerver.cerver_init ()

	cerver.cerver_version_print_full ()

	cerver.pycerver_version_print_full ()

	version.todo_version_print_full ()

	todo_config ()

	service.start ()
