import os, signal, sys
import ctypes

import cerver

from todo import *

from routes.items import *
from routes.service import *
from routes.users import *

todo_cerver = None

# end
def end (signum, frame):
	# cerver.cerver_stats_print (todo_cerver, False, False)
	cerver.http_cerver_all_stats_print (cerver.http_cerver_get (todo_cerver))
	cerver.cerver_teardown (todo_cerver)
	cerver.cerver_end ()

	todo_end ();

	sys.exit ("Done!")

def todo_set_todo_routes (http_cerver):
	# register top level route
	# GET /api/todo
	main_route = cerver.http_route_create (cerver.REQUEST_METHOD_GET, "api/todo".encode ('utf-8'), main_handler)
	cerver.http_cerver_route_register (http_cerver, main_route)

	# GET api/todo/version
	version_route = cerver.http_route_create (cerver.REQUEST_METHOD_GET, "version".encode ('utf-8'), version_handler)
	cerver.http_route_child_add (main_route, version_route)

	# items
	# GET api/todo/items
	items_route = cerver.http_route_create (cerver.REQUEST_METHOD_GET, "items".encode ('utf-8'), todo_items_handler)
	cerver.http_route_set_auth (items_route, cerver.HTTP_ROUTE_AUTH_TYPE_BEARER)
	cerver.http_route_set_decode_data_into_json (items_route)
	cerver.http_route_child_add (main_route, items_route)

	# POST api/todo/items
	cerver.http_route_set_handler (items_route, cerver.REQUEST_METHOD_POST, todo_item_create_handler)

	# GET api/todo/items/:id
	item_info_route = cerver.http_route_create (cerver.REQUEST_METHOD_GET, "items/:id/info".encode ('utf-8'), todo_item_get_handler)
	cerver.http_route_set_auth (item_info_route, cerver.HTTP_ROUTE_AUTH_TYPE_BEARER)
	cerver.http_route_set_decode_data_into_json (item_info_route)
	cerver.http_route_child_add (main_route, item_info_route)

	# PUT api/todo/items/:id/update
	item_update_route = cerver.http_route_create (cerver.REQUEST_METHOD_PUT, "items/:id/update".encode ('utf-8'), todo_item_update_handler)
	cerver.http_route_set_auth (item_update_route, cerver.HTTP_ROUTE_AUTH_TYPE_BEARER)
	cerver.http_route_set_decode_data_into_json (item_update_route)
	cerver.http_route_child_add (main_route, item_update_route)

	# DELETE api/todo/items/:id/remove
	item_remove_route = cerver.http_route_create (cerver.REQUEST_METHOD_DELETE, "items/:id/remove".encode ('utf-8'), todo_item_delete_handler)
	cerver.http_route_set_auth (item_remove_route, cerver.HTTP_ROUTE_AUTH_TYPE_BEARER)
	cerver.http_route_set_decode_data_into_json (item_remove_route)
	cerver.http_route_child_add (main_route, item_remove_route)

def todo_set_users_routes (http_cerver):
	# register top level route
	# GET /api/users
	users_route = cerver.http_route_create (cerver.REQUEST_METHOD_GET, "api/users".encode ('utf-8'), users_handler);
	cerver.http_cerver_route_register (http_cerver, users_route);

	# register users children routes
	# POST api/users/login
	users_login_route = cerver.http_route_create (cerver.REQUEST_METHOD_POST, "login".encode ('utf-8'), users_login_handler);
	cerver.http_route_child_add (users_route, users_login_route);

	# POST api/users/register
	users_register_route = cerver.http_route_create (cerver.REQUEST_METHOD_POST, "register".encode ('utf-8'), users_register_handler);
	cerver.http_route_child_add (users_route, users_register_route);

def start ():
	global todo_cerver
	todo_cerver = cerver.cerver_create_web (
		"web-cerver".encode ('utf-8'), PORT, CERVER_CONNECTION_QUEUE
	)

	# main configuration
	cerver.cerver_set_receive_buffer_size (todo_cerver, CERVER_RECEIVE_BUFFER_SIZE);
	cerver.cerver_set_thpool_n_threads (todo_cerver, CERVER_TH_THREADS);
	cerver.cerver_set_handler_type (todo_cerver, cerver.CERVER_HANDLER_TYPE_THREADS);

	cerver.cerver_set_reusable_address_flags (todo_cerver, True);

	# HTTP configuration
	http_cerver = cerver.http_cerver_get (todo_cerver)

	cerver.http_cerver_auth_set_jwt_algorithm (http_cerver, cerver.JWT_ALG_RS256)
	if (ENABLE_USERS_ROUTES):
		cerver.http_cerver_auth_set_jwt_priv_key_filename (http_cerver, PRIV_KEY.encode ('utf-8'))

	cerver.http_cerver_auth_set_jwt_pub_key_filename (http_cerver, PUB_KEY.encode ('utf-8'))

	todo_set_todo_routes (http_cerver)

	if (ENABLE_USERS_ROUTES):
		todo_set_users_routes (http_cerver)

	# add a catch all route
	cerver.http_cerver_set_catch_all_route (http_cerver, todo_catch_all_handler)

	# start
	cerver.cerver_start (todo_cerver)
