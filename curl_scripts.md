- Test Add
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":2, "argument2":1 }' http://localhost:5000/add
{
  "answer": 3
}
```

- Test Subtract
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":4, "argument2":3 }' http://localhost:5000/subtract
{
  "answer": 1
}
```

- Test Multiply
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":2, "argument2":3 }' http://localhost:5000/multiply
{
  "answer": 6
}
```

- Test Divide
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":12, "argument2":4 }' http://localhost:5000/divide
{
  "answer": 3
}
```

- Test Square Root
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":9 }' http://localhost:5000/sqrt
{
  "answer": 3
}
```

- Test Cube Root
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":64 }' http://localhost:5000/cbrt
{
  "answer": 4
}
```

- Test Power
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":2, "argument2":3 }' http://localhost:5000/exp
{
  "answer": 8
}
```

- Test Factorial
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"argument1":5 }' http://localhost:5000/factorial
{
  "answer": 120
}
```
