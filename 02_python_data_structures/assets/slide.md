---
theme : "night"
transition: "slide"
highlightTheme: "monokai"
slideNumber: false
title: "P3L1 - Python Fundamentals"
verticalSeparator: 'xxx'
presentation:
    width: 1500
    height: 1000

---

<h2>Python Data Structures 🏗️</h2>
<img alt="python logo" src="./python-logo-only.png"/>

---

<h3><strong> ✅ Objectives </strong></h3>

- Review the Sequence types: `list`, `tuple`, `range` (and `str`)
  - Lists: understand CRUD operations with list values
  - Tuples: 
      - Discuss: `mutable` vs `immutable`
      - Create and access values in tuples
 
xxx

  - Ranges: and how they're useful in loops
  - Learn about Set types (time permitting)
- Dictionaries:
  - a mapping data structure
  - know all CRUD operations
- Loops: create `for` and `while` loops with sequences
- Use list comprehensions to emulate JS `map`, `filter` and `find` functions

---

<h3>List... array's Pythonic twin?</h3>

- ordered collection of elements
- aka sequence
- mutable

<pre>
  <code class="language-python">
  my_list = ["hello", "world", 42, ["another", "list"]]
  </code>
</pre>

---

<div style="display: flex; flex-direction: column;">
  <div>
    <img src="./Built-in-List-Functions-in-Python-01.jpg">
  </div>

  <div style="font-size: 1.5rem; margin: 0.85rem 1rem;">
    Let's dive into the code! 🌊
  </div>
</div>

---

<h3>Tuples–when values are forever 💎</h3>

- ordered collection of values
- aka sequence
- **_immutable_**

<pre>
  <code class="language-python">
    my_tuple = (4, 2, "Miyuki", True)
  </code>
</pre>


---

<img src="./Python-range-function-explained.webp" />
<pre>
  <code class="language-python">
    for num in range(8):
      print(f"The count is {num}")
  </code>
</pre>

---

<h3>Dictionaries 📖 Python's JSON</h3>

<h5>Creating dictionaries:</h5>
<pre>
  <code class="language-python">
    cat_1 = {
      'name': 'Simon',
      'color': 'ginger',
      'age': 10
    }
  </code>
  <code class="language-python">
    cat_2 = dict(name='Miyuki', color='grey', age=10)
  </code>
</pre>

---

<h5>Reading and adding values 👓</h5>

<pre><code class="language-python" data-line-numbers="1-5|6-7|8-9|10-11|12-13">cat_1 = {
      'name': 'Simon',
      'color': 'ginger',
      'age': 10
}
cat_1['color']
# => ginger
cat_1.get('age')
# => 10
cat_1.get('mood')
# => None
cat_1['mood'] = 'hungry'
cat_1.setdefault('breed', 'Munchkin')
</code></pre>

<h6 class="fragment">Let's try it! 🚀</h6>

---

<h5>Updating and Deleting values 📝 ❌</h5>

<pre><code class="language-python" data-line-numbers="1-6|7-10|11-14">cat_1 = {
      'name': 'Simon',
      'color': 'ginger',
      'age': 10,
      'mood': 'hungry'
}
cat_1['mood'] = 'sleepy'
cat_1.update(age=11, mood='feisty')
print(cat_1)
# {'name': 'Simon', 'color': 'ginger', 'age': 11, 'mood': 'feisty'}
del cat_1('age')
cat_1.pop('mood')
print(cat_1)
# {'name': 'Simon', 'color': 'ginger'}
</code></pre>

<h6 class="fragment">Let's do it! 🛠️</h6>

---

<h5><code>For</code> loops: let me reiterate 🐈🐈🐈</h5>

<img src="./for-loop-in-python.webp" />


---

#### `break` keyword 🔑

<div style="font-size: 1.5rem">
In a loop, the <code>break</code> keyword escapes the loop, regardless of the iteration number. Once <code>break</code> executes, the program will continue to execute after the loop.
</div>


```python
numbers = [0, 254, 2, -1, 3]

for num in numbers:
  if (num < 0):
    print("Negative number detected!")
    break
  print(num)
  
# 0
# 254
# 2
# Negative number detected!

```

---

<div style="display: flex;">
  <div style="width: 40%">
    <h5>What do PyPi and Pip stand for?</h5>
  </div>
  <div style="font-size: 1.5rem; margin-top: 0.85rem; width: 60%">
    <textarea style="font-size: 1.5rem; border: 2px solid black; padding: 1rem; width: 90%; background: #333; color: #eee" rows="5" cols="35"></textarea>    
  </div>
</div>

<p>Let's install a popular package for sending HTTP requests</p>

```python
pip install requests
```
[PyPi](https://pypi.org/)

---

To install a specific version:
```python
pip install requests==2.22.0
```
To uninstall a package:
```python
pip uninstall requests
```

When deploying, you will use pip to create a requirements file:
```python
pip install -r requirements.txt
```

---

### The Python Shell

<img src="./py_shell.png" />

- Python comes with a built in REPL.
- Start a REPL by typing `python` at the command line.
- Exit with `exit()` or `ctrl + d`

##### Let's try it!

---

### Python's Common Data Types

<div style="font-size: 1.5rem" >

| Example                       | Data Type | Name       |
| ----------------------------- | --------- | ---------- |
| `"Hello Python"`              | str       | string     |
| `20`                          | int       | integer    |
| `20.5`                        | float     | float      |
| `[1, 2, 3]`                   | list      | list       |
| `(1, 2, 3)`                   | tuple     | tuple      |
| `{"name": "Mimi", "age": 10}` | dict      | dictionary |
| `{2, 4, 6}`                   | set       | set        |
| `True`                        | bool      | boolean    |
| `None`                        | NoneType  | NoneType   |

</div>

---

<div style="display: in-line block">
    <iframe src="https://www.classtools.net/dragdrop/202307_DS3M2K" style="position:relative;top:0;left:0;width:900px;height:650px;overflow:none;border:none"></iframe>
</div>

---

### The Virtual Environment 🌲

#### Pyenv

Pyenv is the tool we'll use to install and manage different versions of Python.

- `pyenv versions` will show you what Python versions are currently installed on your machine
- `pyenv install -l` will show a list of versions available to install
- `pyenv install 3.9.2` will install that version on your machine
- `pyenv global 3.9.2` will set that as the global version on your machine

---

#### Pipenv

<p style="font-size: 1.7rem">Pipenv is a tool built upon <code>pip</code> which can create virtual environments and install packages in them.</p>

<div style="font-size: 1.5rem">

- `Pipfile`: look for this first, it is analogous to npm's package.json file and lists the dependencies and Python version for the current project
- `Pipfile.lock`: similar to package-lock.json, this file describes both the Pipfile dependencies AND their dependencies with exact versions

If the project directory doesn't have these, you need to create a virtual environment

<pre style="font-size: 1.7rem"><code>pipenv --python 3.8.13</code></pre>

Now you can start adding dependencies similarly to how you would install packages with `pip`:

<pre style="font-size: 1.7rem"><code>pipenv install requests</code></pre>

</div>

xxx

<div style="font-size: 1.5rem">

| Command          | Description                                               |
| ---------------- | --------------------------------------------------------- |
| `pipenv install` | creates the virtual environment and installs dependencies |
| `pipenv shell`   | activates the virtual environment                         |
| `ctrl + d`       | deactivates the virtual environment                       |
| `pipenv -rm`     | removes the virtual environment                           |

</div>

---

## Let's dive into the code! 🤿

---
