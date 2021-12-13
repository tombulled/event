# event
Event handling

## Usage

### Basic
```python
import event

class Event(event.Event):
    ALERT: str = 'alert'

@event.on(Event.ALERT)
def on_alert():
    print('Alert!')
```

```python
>>> event.dispatch(Event.ALERT)
Alert!
```

### Standard
```python
import event

class Event(event.Event):
    LOGIN: str = 'login'

handler = event.Handler()

@handler.on(Event.LOGIN)
def on_login(username: str):
    print('Login:', dict(username = username))
```

```python
>>> handler.dispatch(Event.LOGIN, username = 'admin')
Login: {'username': 'admin'}
```

### Advanced
```python
import event
from typing import Callable, Optional

class Event(event.Event):
    CLICK: str = 'click'

class Button:
    text: str

    _command: Optional[Callable] = None
    _handler: event.Handler
    
    def __init__(self, text: str, command: Optional[Callable] = None) -> None:
        self._handler = event.Handler()

        self.text = text
        self.command = command

    def click(self) -> None:
        self._handler.dispatch(Event.CLICK)
    
    @property
    def command(self) -> Optional[Callable]:
        return self._command

    @command.setter
    def command(self, command: Optional[Callable]) -> None:
        self._command = command

        if self._command is not None:
            self._handler.bind(Event.CLICK, self._command)

def on_click():
    print('Clicked!')

button = Button('Click Me!', command = on_click)
```

```python
>>> button.click()
Clicked!
```