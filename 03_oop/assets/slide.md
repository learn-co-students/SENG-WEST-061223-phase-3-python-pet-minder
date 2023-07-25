---
theme : "night"
transition: "slide"
highlightTheme: "monokai"
slideNumber: false
title: "P3L3 - Object-Oriented Programming in Python"
verticalSeparator: 'xxx'
presentation:
    width: 1500
    height: 1000

---

<h2>Object-Oriented Programming in Python</h2>
<img alt="python logo" src="./python-logo-only.png"/>

---

<h3><strong> ✅ Objectives </strong></h3>

* Define Object-Oriented Programming
* Understand the benefits of OOP
* Build Classes
* Create instances of those classes
* Use `__init__` to instantiate objects with attribute values

xxx

* Add instance methods to our classes
* Understand the use of the `self`` keyword in instances
* Know the principles of OO Design
* Stretch: object properties, mass assignment

---

<h3>What is OOP? 🤔</h3>

<div style="font-size: 1.8rem" >

* a programming paradigm  
* seeks to encapsulate information and it's related behaviors together as objects
* models concepts and objects in the real world. 
* easier to reason about and solve problems involving those data, 
* facilitates structuring our programs in ways that can share and reuse these objects.
* contrast to Procedural Programming, 
  * written in sequential order and 
  * procedures are called when behaviour needs to be shared between pages in an application.
</div>


---

<img src="./OOPConcept.jpg" style="width: 900px">

---


<section data-background-color="mistyrose" >
  <h3>Classes and Instances</h3>
  <img src="./classes_instances.png" />
</section>


---

### A Python Class is...

* a blueprint or template for creating individual objects
* a data structure which assigns values and methods to objects

<div style="display: flex;">
  <div style="width: 35%; height: 100%">
    <img src="./604px-CPT-OOP-objects_and_classes_-_attmeth.svg.png" />
  </div>

  <div style="width: 65%; height: 100%">
    <img src="./OOP-là-gì-3.jpg" />
  </div>
</div>

---

### An object is...

<div style="display: flex;">
  <div style="font-size: 1.75rem; width: 50%">
    <ul>
      <li> an individual collection of variables (attributes), functions (methods), and data structures</li>
      <li> constructed from a class</li>
      <li> also called an 'instance'</li>
      <li> a representation of a real world object or event</li>
    </ul>
  </div>

  <div style="width: 50%">
    <img src="./CookieCutter.png" />
    
  </div>
</div>


---

#### You actually already have some experience with classes and instances!

<pre>
  <code class="language-python" data-trim >
    type("hello") # => < class 'str'>
    42.__class__ # => < class 'int'>
  </code>
</pre>

<p>What happens when you enter <code>dir("world")</code> in a Python shell?</p>

#### Let's build a class and some instances! 👷

---

#### Some strengths of OOP

* having total control of what objects look like just by updating their class

#### Some weaknesses of OOP

* becuase my objects have to conform to a class, I lose flexibility in changing their attributes without changing the class

---

#### Example Application Domains

* healthcare {.fragment}
* FinTech/banking {.fragment}
* insurance {.fragment}
* sales {.fragment}
* eCommerce {.fragment}
* accounting {.fragment}
* booking software for hospitality and travel {.fragment}

---

#### OOP Design Principles

---

#### How will objects help us going forward? 🚗 

---


___

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

#### `continue` keyword 🔑

<div style="font-size: 1.5rem">
In Python, a <code>while</code> loop will repeatedly execute a code block as long as a condition evaluates to <code>True</code>.
</div>


```python
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# Print only positive numbers:
for i in big_number_list:
  if i < 0:
    continue
  print(i)

```

---

#### `while` loops 🔍

<div style="font-size: 1.5rem">
In Python, the <code>continue</code> keyword is used inside a loop to skip the remaining code inside the loop code block and begin the next loop iteration.
</div>

```python
hunger = 5
while hunger > 0:
  print('munch!')
  hunger -= 1 # be sure to progress your condition towards the base case!
# this will print 'munch!' 5 times

```

---

#### List Comprehension 💡

<div style="font-size: 1.5rem">
List comprehension is a simpler method to create a list from an existing list. It is generally a list of iterables generated with an option to include only the items which satisfy a condition.
</div>

<img src="./list-comp-diagram.png" />

---

