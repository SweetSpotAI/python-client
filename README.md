# SweetSpot AI python client



How to use it?
-----

```python
study = Study("test1", {'x': {'number': 'continuous'}}, token="17a3ae3404414c26a043cdafc3c47cb4")
x = study.ask()
print('got:', x)
study.tell(x, 1.0)

```
