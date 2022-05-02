import itertools
from typing import Iterable
from event import Handler


def test_on() -> None:
    handler: Handler = Handler()

    @handler.on("foo")
    def foo():
        pass

    assert handler.hooks == {"foo": [foo]}


def test_bind() -> None:
    handler: Handler = Handler()

    def foo():
        pass

    handler.bind("foo", foo)

    assert handler.hooks == {"foo": [foo]}


def test_dispatch() -> None:
    count: itertools.count[int] = itertools.count()

    handler: Handler = Handler()

    def foo():
        next(count)

    handler.hooks["foo"] = [foo]

    handler.dispatch("foo")

    assert next(count) == 1
