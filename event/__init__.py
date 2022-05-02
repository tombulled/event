from .handler import Handler

HANDLER: Handler = Handler()

on = HANDLER.on
dispatch = HANDLER.dispatch
