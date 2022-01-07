# event
Event handling

## Usage

### Basic
```python
import event

@event.on('alert')
def on_alert():
    print('Alert!')
```

```python
>>> event.dispatch('alert')
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
    print(f'User {username!r} logged in')
```

```python
>>> handler.dispatch(Event.LOGIN, username = 'admin')
User 'admin' logged in
```