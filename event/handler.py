import dataclasses
from typing import Any, Callable, Dict, List


@dataclasses.dataclass
class Handler:
    hooks: Dict[Any, List[Callable]] = dataclasses.field(default_factory=dict)

    def on(self, event: Any) -> Callable:
        def wrapper(func: Callable):
            self.bind(event, func)

            return func

        return wrapper

    def bind(self, event: Any, func: Callable) -> None:
        self.hooks.setdefault(event, []).append(func)

    def dispatch(self, event: Any, *args: Any, **kwargs: Any) -> None:
        hook: Callable
        for hook in self.hooks.get(event, ()):
            hook(*args, **kwargs)
