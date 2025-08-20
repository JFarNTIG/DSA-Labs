# Lab 2.2 - Abstract Syntax Trees

Copyright (C) 2025 Jacob Farnsworth.

Created for the course Programmering, datastrukturer och algoritmer NTI Gymnasiet Karlstad HT 2025

## AI-Deklaration (Lärare)

AI användes i framtagandet av denna laboration.

Modell som användes: OpenAI o3

AI användes i följande:

* Skrev parse_expression enligt en beskrivning (att den ska använda shunting yard-algoritmen) och definitionen av Node-klassen.

Allt annat har skrivits av lärare.

## Setup

### Linux

```
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
```

### Windows
```
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
pytest
```

## Introduction

This Python project contains code for parsing arithmetic expressions, i.e. expressions such as:

`2 + 3 * 5`

*In string form*, a computer cannot compute such an expression directly. It must first be converted into a form that a program can understand. This is usually done using an abstract syntax tree (AST).

In an AST, any expression becomes a tree where each node represents a value, an operation, or some other computable entity.

For example, the expression above would become the following:

```
  +
 / \
2   *
   / \
  3   5
```

The AST encodes everything that a program needs to know to compute the result of the expression. The example tree above can be interpreted as:

add: 2 and the result of multiply: 3 and 5

To evaluate the expression, a program can traverse the tree, evaluating the innermost nodes first (the ones which only have "leaves", no branches). In the example above, the program would first evaluate 3 * 5, reducing that node to 15:

```
  +
 / \
2   15
```

Finally, the program would evaluate 2 + 15:

```
  17
```

In this way, complex expressions can be represented efficiently.

Abstract Syntax Trees and related concepts are used in many different fields, including:

* Programming languages and compiler design. If you ever want to create your own programming language,
  you will have to learn abstract syntax trees.
* Symbolic math engines (MATLAB, WolframAlpha).
* Natural Language Processing (NLP), where sentences can be parsed as trees according to a grammar.

## Assignment

* You **are allowed** to refer to the readings (w3schools, refactoring guru).
* You **are allowed** to use Google to help you understand terms you don't know.
* You **are allowed** to use AI tools to define new terms or get examples.
* You **are not allowed** to use AI tools to complete these tasks (neither writing nor programming) by copy/pasting instructions or code.
* You **are not allowed** to share your solutions with your classmates.

In addition, your solutions must abide by the following:

* You **are not allowed** to import any new libraries. However, importing functions or classes within the project (`Node`, `BinaryOp`, etc) is allowed.
* You **are not allowed** to modify any of the existing method signatures.
* You **are not allowed** to modify or remove any of the unit tests in `tests/`. However, you may add new unit tests, if you wish to do so.
* You **are not allowed** to hardcode solutions to the test cases.

### Understanding Questions.

For each question, remember to **justify your answer**. It's not enough to answer the question, you also have to **explain how you know**.

1. Read the code for the `evaluate()` method. Note that there are three different "versions" of this function; one in `Node`, one in `Value`, and one in `BinaryOp`.

    a. Which **object-oriented principle** is demonstrated by the `evaluate()` function (encapsulation, inheritance, polymorphism)?

    b. Which **tree traversal order** does the `evaluate()` method use (breadth-first, in-order, or depth-first)?

    c. Which **type of loop** occurs in the `evaluate()` method (iterative, or recursive)?

### YOUR ANSWERS

1.  Write your answers here.

    a. 

    b. 

    c. 

### Programming Tasks

Follow the instructions for each task.

1. Implement the `to_string()` method in `Value` and `BinaryOp`. This method turns an expression tree back into string form. Your solution will involve traversing the tree; see the `evaluate()` method as an example of how you can do this.

    a. Tip: Focus on getting the function to work for the default case, i.e. `explicit_parens = True` first.
    
    b. As you work, run the unit tests periodically. For this part of the assignment, the tests in `test_printing.py` should gradually start to pass.
    
    c. Once the case for `explicit_parens = True` is working, get the method to work when `explicit_parens = False`.

2. Implement `contains_op` and `contains_value`. Like in part 1, your solutions to these will also involve traversing the tree. However, your approach may need to be adjusted slightly, because these are not class methods, but rather standalone functions.

    a. As you work, run the unit tests periodically. For this part of the assignment, the tests in `test_utils.py` should gradually start to pass.

3. Look back on your solutions to part 2. Assuming you solved these the "obvious" way, then your solutions probably contain a lot of shared logic. At this point, alarm bells should be going off in your head. **Shared logic can be abstracted.** Your task for part 3 is to rewrite `contains_op` and `contains_value` and lift the logic related to traversing the tree to a new class which can be reused by both functions.

    When you are done with this part, `contains_op` and `contains_value` should not contain **any** details of how the tree is traversed, but rather delegate this logic to some other class.

    * For this part, you **must** use one of the design patterns we have talked about in class. **It is up to you to choose the most appropriate design pattern from the ones we have discussed.** Your options are thus: **factory, singleton, iterator, visitor, observer.**

4. (VG) In this part, your task is to revise the expression system to support a new type of node, `Variable`. With the variable node type, it should be possible to parse an expression such as:

`3 + 2 * x`

Your solution should, at a minimum, support the following:

* A new class, `Variable`, which is a type of `Node`. The data of `Variable` is one letter representing a variable in an expression.
* Revised code in `parse_expression()` to support expressions with variables. You will have to modify the parsing logic so that `Variable` nodes are created when letters are encountered.
* Ability to perform a *substitution* of a variable. It should be possible to substitute a variable for **any expression**. For example:
    - Expression: `3 + 2 * x` substituting `5` for `x` returns an expression: `3 + 2 * 5`
    - Expression: `3 + 2 * x` substituting `1 + y` for `x` returns an expression: `3 + 2 * (1 + y)`
* Implementation of `evaluate()` so that expressions with variables can be evaluated. This method should determine the value of the variable using the context dict. For example:
    - Expression: `3 + 2 * x` evaluating with context `{'x': 5}` would return `13`.

    For this part, you are expected to write **new unit tests** to cover your changes.


## AI-Deklaration

Användning av Al-verktyg är tillåtet i begränsad utsträckning. Du får inte klistra in uppgifter eller delar av uppgifter, men du får använda AI för att förtydliga nya ord och begrepp eller ge exempel.

Här på slutet ska du ange allmänt vilka AI-verktyg som använts, hur du använt dem, och hur användbara dessa verktyg är. Om du inte använt AI-stöd så skriv bara att "AI-verktyg har ej använts".

### STUDENTSVAR (AI-användning):

*  