import dataclasses
import enumb


class Event(enumb.StrEnum):
    pass


@dataclasses.dataclass
class Handler:
    hooks: dict = dataclasses.field(default_factory=dict)

    def on(self, event):
        def wrapper(func):
            self.bind(event, func)

            return func

        return wrapper

    def bind(self, event, func):
        self.hooks.setdefault(event, []).append(func)

    def dispatch(self, event, *args, **kwargs):
        for hook in self.hooks.get(event, ()):
            hook(*args, **kwargs)


GLOBAL_HANDLER = Handler()

on = GLOBAL_HANDLER.on
dispatch = GLOBAL_HANDLER.dispatch
