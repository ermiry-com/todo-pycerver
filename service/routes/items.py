import ctypes

import cerver

# GET /api/todo/items
# get all the authenticated user's items
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_items_handler (http_receive, request):
	pass

# POST /api/todo/items
# a user has requested to create a new item
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_item_create_handler (http_receive, request):
	pass

# GET /api/todo/items/:id/info
# returns information about an existing item that belongs to a user
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_item_get_handler (http_receive, request):
	pass

# PUT /api/todo/items/:id/update
# a user wants to update an existing item
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_item_update_handler (http_receive, request):
	pass

# DELETE /api/todo/items/:id/remove
# deletes an existing user's item
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_item_delete_handler (http_receive, request):
	pass
