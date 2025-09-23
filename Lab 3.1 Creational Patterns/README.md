# Lab 3.1 - Creational Patterns

Copyright (C) 2025 Jacob Farnsworth.

Created for the course Programmering, datastrukturer och algoritmer NTI Gymnasiet Karlstad HT 2025

## AI-Deklaration (Lärare)

AI användes ej i framtagandet av denna laboration.

## Introduction

Part of becoming a good programmer is learning to use the *right tools in the right situations*. When it comes to organizing data, we try to choose appropriate and effective data structures. On the other hand, for operations on data, we try to choose the fastest algorithms. Many common data and algorithm scenarios occur all the time when building software, and studying data structures and algorithms allow us to solve these problems effectively without reinventing the wheel.

However, what about other kinds of "problem scenarios"? In object-oriented languages like Python, Java or C++, we often have to design classes, and we try to structure these classes in an effective way with the principles we've learned about: encapsulation, inheritance, and polymorphism. But, as you might have realized in your studies, designing classes and making choices about inheritance and polymorphism isn't always easy.

There are plenty of common problem scenarios that involve designing classes and inheritance hierarchies. And, just like with data structures and algorithms, there are battle-tested solutions to these problems. This is exactly the field of *design patterns*: efficient solutions to problems involving classes and class hierarchies.

In this lab we will focus on the most common *creational patterns*. These are patterns that either help us efficiently create objects or manage their lifecycles.

The patterns we will focus on are *factory pattern* and *singleton pattern*. Please read the pages on these design patterns on refactoring.guru via the links below. Try to understand the scenario (what problem the pattern is trying to solve) and how the pattern works (read the class diagram!)

Factory:
* https://refactoring.guru/design-patterns/factory-method

Singleton:
* https://refactoring.guru/design-patterns/singleton

The *factory pattern* is often used in situations where we want to be able to easily create different objects of similar or related classes. Compared to manually creating objects, the factory pattern is quite useful when each object takes some amount of setup. For example:

* Generating enemies of different types in a game.
* Setting up UI elements (buttons, lists, text fields, windows) in a program with GUI.

Another benefit of the factory pattern is that it helps separate the logic of creating objects from the code that needs to create those objects. This makes it easier to add new types of objects in the future (i.e. the code has better extensibility).

Meanwhile, the *singleton pattern* is used in situations where only *one* instance of a class should exist, and we want this instance to be easily accessible for the rest of the code over the entire lifetime of the program. Example:

* A program's settings (a class can be made that stores settings, but it doesn't make sense to have several objects of this class - only one, because the program only has one set of settings).

The singleton pattern is very nice because it essentially allows us to store global data without using global variables (which some people consider to be *dangerous and bad*). A singleton class is essentially a global class; we can store global data and global behavior while keeping all the benefits of classes, i.e. we can keep our global data encapsulated.

Another benefit of the singleton pattern is that it's easier to avoid re-instantiating classes, i.e. creating several identical instances of the same class, which would otherwise be a waste of resources.

Keep in mind that design patterns don't just help you write code with good performance. In fact, design patterns aren't really about performance. Design patterns mainly help you write code that's clean, organized, and extensible.

## Assignment

* You **are allowed** to refer to the readings (w3schools, refactoring guru).
* You **are allowed** to use Google to help you understand terms you don't know.
* You **are allowed** to use AI tools to define new terms or get examples.
* You **are not allowed** to use AI tools to complete these tasks (neither writing nor programming) by copy/pasting instructions or code.
* You **are not allowed** to share your solutions with your classmates.

In addition, your solutions must abide by the following:

* You **are not allowed** to modify any of the method signatures.
* You **are not allowed** to modify or remove any of the unit tests in `tests/`. However, you are welcome to add new unit tests, if you wish to do so.
* You **are not allowed** to hardcode solutions to the test cases.

### Understanding Questions.

For each question, remember to **justify your answer**. It's not enough to answer the question, you also have to **explain how you know**.

1. Read the code in the `game/` folder. This folder contains the code for a small text-based RPG combat simulator. `main_old.py` has a version of the code *before rewriting it to use* using design patterns; `main_new.py` contains the same code but *after rewriting it to use* design patterns.

    a. Which design pattern(s) are used in the code, and where? Factory, singleton, both, or neither? How do you know?

    b. Compare `main_old.py` and `main_new.py`. What are the differences between the code before rewriting with design patterns, and after? If the code seems better, don't just write that the code "looks better". Explain *what* is better about the new version.

2. Read the code in the `os_folders/` folder. This folder contains the code for a program which determines the user's home directory.

    a. Which design pattern(s) are used in the code, and where? Factory, singleton, both, or neither? How do you know?

    b. Compare `main_old.py` and `main_new.py`. What are the differences between the code before rewriting with design patterns, and after? If the code seems better, don't just write that the code "looks better". Explain *what* is better about the new version.


### STUDENT ANSWERS (Understanding Questions)

Write your answers here.

1. 

    a. 

    b. 

2. 

    a. 

    b. 


### Programming Tasks

Follow the instructions for each task.

1. In the `game/` project, add a new enemy type called "Bandit". You will need to add a new class in an appropriate file (see the other enemy type classes for examples). Finally, add your new enemy type to the game so that it can be randomly chosen as a "medium" difficulty enemy. Do this with both the old code (`main_old.py`) and new code (`main_new.py` and `enemy_factory.py`) so that you can compare how it feels to work both with and without the design patterns. Test your code by running the game until it generates a bandit. 

    Bandits should work as follows:

    * Bandits should have 25 max health and 18 strength.
    * Bandits should have a 1/10 random chance to defend on their turn, otherwise they attack.
    * Random names should be generated as follows: A name is randomly chosen from this list:
        - "Hugo"
        - "Jerome"
        - "Nick"
        - "Selena"
        - "Aliya"
        - "Erika"
        - "Maddox"

        and a random ending is applied:
        - "the Razor"
        - "the Champion"
        - "the Hammer"
        - "the Crusher"
        - "the Smasher"

        Example: "Maddox the Hammer"

2. Write: What was different about adding your enemy type to the old code (`main_old.py`) versus the new code (`main_new.py` and `enemy_factory.py`)? How did it feel with vs. without the design pattern?

3. In the `os_folders/` project: Find out how many times the folder manager is initialized both in the old code (`main_old.py`) and the new code (`main_new.py` and `manager_holder.py`). Hint: Try running each program with breakpoints set in `WindowsFolderManager.__init__()` and count how many times the debugger breaks. Alternatively, you could add some kind of counter in `WindowsFolderManager.__init__()` that counts how many times it's called.

4. Write: Based on your previous answers and the reading in the introduction, how did design patterns improve the code in the `os_folders/` project?

### STUDENT ANSWERS (Tasks)

1. 

2. 

3. 

4. 

### (VG) Task

1. (VG) Go back to the following lab and complete the task about design patterns. You will have to rewrite some part of the program to use the appropriate design pattern. It is up to you to choose design patterns that make sense!

* Lab 2.1 Sorting

## AI-Deklaration

Användning av Al-verktyg är tillåtet i begränsad utsträckning. Du får inte klistra in uppgifter eller delar av uppgifter, men du får använda AI för att förtydliga nya ord och begrepp eller ge exempel.

Här på slutet ska du ange allmänt vilka AI-verktyg som använts, hur du använt dem, och hur användbara dessa verktyg är. Om du inte använt AI-stöd så skriv bara att "AI-verktyg har ej använts".

### STUDENTSVAR (AI-användning):

* 