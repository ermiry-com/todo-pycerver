import cerver.utils

TODO_VERSION = "0.2"
TODO_VERSION_NAME = "Version 0.2"
TODO_VERSION_DATE = "31/05/2021"
TODO_VERSION_TIME = "10:02 CST"
TODO_VERSION_AUTHOR = "Erick Salas"

def todo_version_print_full ():
	cerver.utils.cerver_log_both (
		cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
		"\nTodo PyCerver Version: %s".encode ('utf-8'), TODO_VERSION_NAME.encode ('utf-8')
	)

	cerver.utils.cerver_log_both (
		cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
		"Release Date & time: %s - %s".encode ('utf-8'),
		TODO_VERSION_DATE.encode ('utf-8'), TODO_VERSION_TIME.encode ('utf-8')
	)

	cerver.utils.cerver_log_both (
		cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
		"Author: %s\n".encode ('utf-8'),
		TODO_VERSION_AUTHOR.encode ('utf-8')
	)

def todo_version_print_version_id ():
	cerver.utils.cerver_log_both (
		cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
		"\nTodo PyCerver Version ID: %s\n".encode ('utf-8'),
		TODO_VERSION.encode ('utf-8')
	)

def todo_version_print_version_name ():
	cerver.utils.cerver_log_both (
		cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
		"\nTodo PyCerver Version: %s\n".encode ('utf-8'),
		TODO_VERSION_NAME.encode ('utf-8')
	)
