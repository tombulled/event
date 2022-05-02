# event
Event handling

## Usage

### Basic
```python
import event

@event.on("alert")
def on_alert():
    print("Alert!")
```

```python
>>> event.dispatch("alert")
Alert!
```

### Standard
```python
import event

handler = event.Handler()

@handler.on("login")
def on_login(username: str):
    print(f"Logged in as {username}")
```

```python
>>> handler.dispatch("login", username="admin")
Logged in as admin
```