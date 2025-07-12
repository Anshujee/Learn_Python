markdown
# 📘 Mutable vs Immutable in Python

Understanding how Python handles memory and object references is essential for writing efficient and bug-free code.

## 🔸 Definitions

### Immutable – Unchangeable  
Once created, the object **cannot** be modified in place.

**Examples**:
- `int`
- `float`
- `str`
- `tuple`
- `bool`

### Mutable – Changeable  
You **can** change the content of the object without creating a new one.

**Examples**:
- `list`
- `dict`
- `set`
- `bytearray`

---

## 🧠 How Python Handles Memory

Every time you create a variable:

- Python creates an object in memory.
- Assigns it a unique ID (`id()`).
- Your variable acts as a label pointing to that memory address.

---

## 📦 Immutable Objects: Stored Once, Reused Often

```python
a = 10
b = 10

print(id(a))  # e.g., 140734627083888
print(id(b))  # Same as above
Since integers are immutable, Python reuses the same object in memory (a technique called interning).

Changing a:

python
a = 11
print(id(a))  # New memory address
✅ New object created ✅ b still points to the original 10

📦 Mutable Objects: Change Content Inside
python
x = [1, 2, 3]
y = x
x.append(4)

print(y)  # Output: [1, 2, 3, 4]
✅ Both x and y point to the same list object ✅ Changes to x affect y