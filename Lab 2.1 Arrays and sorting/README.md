# Lab 1 - Sorting Algorithms

Copyright (C) 2025 Jacob Farnsworth.

Created for the course Programmering, datastrukturer och algoritmer NTI Gymnasiet Karlstad HT 2025

## AI-Deklaration (Lärare)

AI användes ej i framtagandet av denna laboration.

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

In programming, there are often many different ways to solve a given problem. However, not all solutions are created equal: some solutions are more efficient than others, or consume more memory. Naturally, if you're going to solve a problem, you probably want to choose the most efficient solution.

Some problems boil down to figuring out the best way to organize some data; this is roughly the field of **data structures**. Other problems involve figuring out the most efficient way to operate on data; this is roughly the study of **algorithms**.

For a long time, programmers have been studying the **most efficient ways** to solve different kinds of problems, so that these most efficient solutions can be reused. Naturally, there has been a focus on the **most common problems** in programming, since they appear just about everywhere.

For example, **searching** and **sorting** are extremely common tasks; almost every program searches or sorts some kind of collection at some point in its execution. Pathfinding is another example of a common problem; any game AI probably involves some kind of pathfinding algorithm to get from one location to the next.

Studying data structures and algorithms also provides us with tools to analyze and quantify how effective these solutions are, so that different solutions can be compared in a meaningful way.

In this lab, you will implement some common **sorting algorithms on arrays**. In addition, you will **compare the effectiveness** of these sorting algorithms, both in theory (big-O notation) and in practice (by running and timing them).

The algorithms you will implement are:
* Bubble sort. (provided as an example)
* Insertion sort.
* Quick sort.
* Merge sort.
* Mystery sort.

Mystery sort is a sorting algorithm that my buddy Paul discovered. He was doing some digging in his backyard before a barbecue when he accidentally dug up an ancient Babylonian clay tablet with an algorithm inscribed on it.

The inscription read as follows:

```
PROCEDURE SORT LIST items DO
    IF LENGTH OF items LESS OR EQUAL 1 DO RETURN

    IF LENGTH OF items EQUAL 2 DO
        IF items[0] GREATER items[1] DO
            SWAP items[0], items[1]
        END IF

        RETURN
    END IF

    LET min = MINIMUM OF items
    LET max = MAXIMUM OF items
    LET betwixt = EMPTY

    FOR item IN items DO
        IF item GREATER min AND item LESS max DO
            SET betwixt = item
            BREAK
        END IF
    END FOR

    IF betwixt NOT EMPTY DO
        LET less = EMPTY LIST
        LET middle = EMPTY LIST
        LET greater = EMPTY LIST

        FOR item IN items DO
            IF item EQUAL betwixt DO
                APPEND item TO middle
            ELSE IF item GREATER betwixst DO
                APPEND item TO greater
            ELSE DO
                ??????????????????
            END IF
        END FOR

        IF less NOT EMPTY DO
            sort less
        END IF

        IF greater NOT EMPTY DO
            sort greater
        END IF

        CLEAR items
        EXTEND items BY less
        EXTEND items BY middle
        ??????????????????????
    END IF
END PROCEDURE
```

Unfortunately, Paul smudged some barbecue sauce on the clay tablet, making some parts of the code unreadable. You'll have to think about what the code is trying to do in order to recreate the original algorithm.

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

1. **In theory**, as the number of elements grows very large, which **standard** sorting algorithm (bubble, insertion, quick, merge) is most efficient with regard to **time complexity**? **Your answer must involve a comparison of algorithms using big-O notation**. If there is a tie between more than one algorithm, state this in your answer.

2. **In theory**, as the number of elements grows very large, which **standard** sorting algorithm (bubble, insertion, quick, merge) is **most efficient** with regard to **space (memory) complexity**? **Your answer must involve a comparison of algorithms using big-O notation**. If there is a tie between more than one algorithm, state this in your answer.

3. Time complexity can be further broken down into best, average, and worst case. Focusing on **insertion sort**: What is the best case, vs average case, vs worst case time complexity? In which situation does insertion sort achieve **best case** complexity? Why?


### STUDENT ANSWERS (Understanding Questions)

Write your answers here.

1. 

2. 

3. 


### Programming Tasks

Follow the instructions for each task.

1. Finish the implementations of insertion sort, quick sort, and merge sort. You can refer to the pages on w3schools about these algorithms and adapt the examples. **Keep in mind** that you cannot simply copy the examples verbatim; you **must** adapt them. Each sorting algorithm must also accept an optional comparison function, which it will use to compare elements in the list.

    * Remember to run unit tests periodically as you work. Once all unit tests are passing for each sorting algorithm, you will know your implementations are more or less correct.

2. Finish the implementation of mystery sort. Refer to the pseudocode in the assignment description. Keep in mind: Just like the standard sorting algorithms, you must adapt mystery sort to accept an optional comparison function.

    * Remember to run unit tests periodically as you work.

3. Measure the **actual** effectiveness of each of the sorting algorithms. You will write a program that does the following (refer to `examples/sort.py` for a starting point):

    * Start by generating a list of (10000, 15000, or 20000) integer numbers. The numbers in each list should be randomized between 0 and 10000.
    * Record the start time (use the `timeit` library)
    * Sort the list.
    * Record the end time.
    * Compute the difference `end-start`. This is the time taken to sort.
    * Run the program, and record the sort time. **Organize your results in the provided table**.

    By default, Python has a recursion limit of 1000, which may result in errors when using functions with deep recursion. If you run into errors, you can change the recursion limit to a higher value:

    ```
    import sys

    sys.setrecursionlimit(10**6)
    ```

    **Standard Array (Python list)**

    |           |  **Bubble**  | **Insertion** |   **Quick**   |   **Merge**   |   **Mystery**   |
    |-----------|--------------|---------------|---------------|---------------|-----------------|
    |  N=100    |      -       |       -       |       -       |       -       |        -        |
    |  N=10000  |      -       |       -       |       -       |       -       |        -        |
    |  N=15000  |      -       |       -       |       -       |       -       |        -        |
    |  N=20000  |      -       |       -       |       -       |       -       |        -        |


    a. What conclusions can you draw from your results? Which algorithms were most effective in practice? Does anything else in the results stick out to you?

    ### STUDENT ANSWERS (Analysis of Results)

    Write your answers here.

    a. 

4. Read `src/sortlib/favorite.py` and `examples/favorite.py`. There is a function `favorite_sort()` which sorts a list according to the user's "favorite" sorting algorithm, which is specified in a settings file.

    There is a bit of a problem with the favorite system. Every time `favorite_sort()` is executed, the settings file is read from disk. This means if a program executes `favorite_sort()` multiple times (i.e. to sort more than one list) then the file will be read multiple times, even though the setting hasn't changed.

    Your task in this part is to rewrite the favorite system (focus **especially** on `get_favorite_sort()`) to have better performance.

    * For this part, you **must** use one of the design patterns we have talked about in class. **It is up to you to choose the most appropriate design pattern from the ones we have discussed**. Your options are thus: **factory, singleton, iterator, visitor, observer**.

5. **(VG)** In this part, your task is to study how sorting a linked list differs from sorting an ordinary array. Recall that a **doubly-linked list** stores each item in a node, where each node has pointers to the next node and the previous node in the list.

    In a linked list, some operations (inserting an element in the beginning, or between two nodes) are generally faster than with an array. However, some operations (looking up an item by index, searching from beginning to end) are generally slower.

    Iterating a linked list is *theoretically* as fast as iterating a standard array, however, in practice it is usually somewhat slower. This is because following pointers is more "expensive" for the processor than iterating a continuous region of memory.

    See `linkedlist.py` and the `LinkedList` class, which implements a doubly-linked list.

    In this part, you are to implement a version of bubble sort that works on linked lists (`ll_bubble.py`). **Remember:** Looking up an item in a linked list by index is quite slow. As a general rule, in your algorithm, do not ever access an element by index (`items[i]`). Instead, operate on nodes and use `next` and `prev` to navigate around the list.

    Next, compare your linked list bubble sort to standard bubble sort and quick sort. (For the latter two, simply use the same sort function from before, but pass in a linked list instead of an array. See `test_ll_bubble.py` for examples on how to create a linked list.)

    **(VG) Linked List**

    |           |   **Bubble**    |  **LL Bubble**  |   **Quick**   |
    |-----------|-----------------|-----------------|---------------|
    |  N=100    |        -        |        -        |       -       |
    |  N=5000   |        -        |        -        |       -       |

    a. What conclusions can you draw from your results? Which algorithm was most effective for linked lists? Were the results surprising or unsurprising?

    ### STUDENT ANSWERS (Analysis of Results)

    Write your answers here.

    a. 

## AI-Deklaration

Användning av Al-verktyg är tillåtet i begränsad utsträckning. Du får inte klistra in uppgifter eller delar av uppgifter, men du får använda AI för att förtydliga nya ord och begrepp eller ge exempel.

Här på slutet ska du ange allmänt vilka AI-verktyg som använts, hur du använt dem, och hur användbara dessa verktyg är. Om du inte använt AI-stöd så skriv bara att "AI-verktyg har ej använts".

### STUDENTSVAR (AI-användning):

* 