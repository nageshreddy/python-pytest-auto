| Feature                | List               | Set                | Tuple               |
|------------------------|--------------------|--------------------|---------------------|
| Ordered?               | ✅ Yes             | ❌ No              | ✅ Yes              |
| Mutable?               | ✅ Yes             | ✅ Yes             | ❌ No               |
| Allows duplicates?     | ✅ Yes             | ❌ No              | ✅ Yes              |
| Indexing?              | ✅ Yes             | ❌ No              | ✅ Yes              |
| Use cases              | Collections of items that change | Unique items, fast membership testing | Fixed data, keys in dicts |

✅ Run locally:
docker-compose up -d
pytest -v 

docker-compose up --build --abort-on-container-exit


🔑 Benefits of this Setup:
✅ Separation of concerns (data/db/logs).

✅ Dockerized DB for consistent local & CI testing.

✅ GitHub CI/CD with pytest running on each push/PR.

✅ Logging & config are modular.

✅ Easy to extend (add new modules or tests).
 What are Python’s built-in data types?

 What is Python?
Python is a high-level, interpreted, general-purpose programming language known for its readability and dynamic typing.

2️⃣ What are Python’s key features?

Easy to learn & use

Dynamically typed

Interpreted

Extensive standard libraries

Supports multiple paradigms (OOP, functional, etc.)

3️⃣ What is PEP 8?
PEP 8 is Python’s official style guide for writing clean and readable code.

What are Python’s built-in data types? 
What’s the difference between a list and a tuple?

List: Mutable, defined with [].

Tuple: Immutable, defined with ().  

How does Python handle memory?

Python uses reference counting and a garbage collector to manage memory automatically.

Numbers: int, float, complex

Sequence: list, tuple, range

Text: str

Set: set, frozenset

Mapping: dict

Boolean: bool

Binary: bytes, bytearray

What are Python’s built-in data types?

Numbers: int, float, complex

Sequence: list, tuple, range

Text: str

Set: set, frozenset

Mapping: dict

Boolean: bool

Binary: bytes, bytearray 


What is a lambda function?
An anonymous function defined with the lambda keyword. Example: