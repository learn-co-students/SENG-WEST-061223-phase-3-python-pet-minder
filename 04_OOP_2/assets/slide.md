---
theme : "night"
transition: "slide"
highlightTheme: "monokai"
slideNumber: false
title: "P3L4 - OOP 2: Class Methods, Class Variables & Object Relationships"
verticalSeparator: 'xxx'
presentation:
    width: 1500
    height: 1000

---

<h2>OOP 2: Class Methods, Class Variables & Object Relationships</h2>
<img alt="python logo" src="./python-logo-only.png"/>

---

<h3><strong> ✅ Objectives </strong></h3>


- Learn about decorators
  - what are they? {.fragment}
  - how are they useful in Python classes? {.fragment}
  - Python's "pie" syntax {.fragment}
- Understand class variables {.fragment}
  - how to define and update their value {.fragment}
- Write class methods {.fragment}
  - use the `@classmethod` decorator {.fragment}
  - `cls` keyword {.fragment}

xxx

- Object inheritance {.fragment}
  - how is it useful? {.fragment}
  - inherited or overwritten? {.fragment}
  - calling `super()` {.fragment}

xxx

- Build one-to-many relationships between objects {.fragment}
    - Discuss their importance and use {.fragment}
    - Emphasize single-source-of-truth {.fragment}
    - Demonstrate building one-way and two-way relationships {.fragment}
- Build many-to-many relationships between objects {.fragment}
    - Discuss their importance and use {.fragment}
    - Demonstrate building the relationship with and without intermediary class {.fragment}
- Aggregate Methods {.fragment}
    - Write aggregate methods to collect data about objects using their related objects {.fragment}



---

#### What are decorators? 🪴 🛋️

<img src="./Decorators3.png" />

---

<div style="display: flex;">
  <div style="width: 40%; height: 100%">
    <p>Decorators give us an easy way to extend a method's functionality without altering the method.</p>
  </div>

  <div style="width: 60%; height: 100%">
    <img src="./Where-Decorators-Used.png" />
  </div>
</div>


---

#### Decorators are higher-order functions

<img src="./Python-Decorators-Explained.png" />

<p>They take in a function as an argument, and return a function.</p>

<p class="fragment" >The "pie", <code>@decorator</code>, syntax makes decorators easier to implement in our code.</p>

#### Let's try it! 🏈 {.fragment}

---

### Class Variables

<div style="display: flex">
  <div style="width: 50%">
    <img src="./create_declare_instance_variable.webp" />
  </div>
  <div style="width: 50%; text-align: left">
    We have used instance variables (attributes) to assign unique values to instances of a class. How could we assign a univeral value which would be the same for all instances?
  </div>

</div>

---

<img src="./create_and_access_class_variable.webp" >

<p>Every object instantiated from the class has read and write access to its class variables.</p>
