from .handler import Handler

HANDLER: Handler = Handler()

on = HANDLER.on
bind = HANDLER.bind
dispatch = HANDLER.dispatch
