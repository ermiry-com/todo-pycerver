import cerver.utils

TODO_VERSION 			= "0.1"encode ('utf-8')
TODO_VERSION_NAME 		= "Version 0.1"encode ('utf-8')
TODO_VERSION_DATE 		= "05/04/2021"encode ('utf-8')
TODO_VERSION_TIME 		= "10:14 CST"encode ('utf-8')
TODO_VERSION_AUTHOR 	= "Erick Salas"encode ('utf-8')

def todo_version_print_full ():
	cerver.utils.cerver_log_both (
		cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
		"\nTodo PyCerver Version: %s".encode ('utf-8'), TODO_VERSION_NAME
	)

	cerver.utils.cerver_log_both (
		cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
		"Release Date & time: %s - %s".encode ('utf-8'),
		TODO_VERSION_DATE, TODO_VERSION_TIME
	)

	cerver.utils.cerver_log_both (
		cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
		"Author: %s\n".encode ('utf-8'),
		TODO_VERSION_AUTHOR
	)

def todo_version_print_version_id ():
	cerver.utils.cerver_log_both (
		cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
		"\nTodo PyCerver Version ID: %s\n".encode ('utf-8'),
		TODO_VERSION
	)

def todo_version_print_version_name ():
	cerver.utils.cerver_log_both (
		cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
		"\nTodo PyCerver Version: %s\n".encode ('utf-8'),
		TODO_VERSION_NAME
	)