# Pseudocode
- Plain language description of the steps in an algorithm or a program.
- Bridge between the program's logic and the actual code itself

## Importance
- Helps to understand and plan the program logic, so it's easier to code.
- Also helps with collaboration. Improves collaborations in team projects.
- Helps with troubleshooting (it's a high level understanding of the program)
- Identify the core areas of the programming that needs to be done.

## Characteristics:
- Plain language: Simple and understandable
- Structured: Should follow a proper logic sequence
- Abstracted: Focusses on logic more than syntax
- Detailed: Thorough walkthrough that helps explain the logic

## Basic Constructs:
- Sequential
```
    - Step 1: Do this
    - Step 2: Do that
```
- Conditional
```
    - IF condition, THEN:
        - Do something
    - ELSE:
        - Do something else
    - END IF
```
- Loops
```
    - WHILE condition meets
        - Do something
    END WHILE LOOP
```
```
    - For each item in a collection:
        - Do something
    - END FOR LOOP
```

## Practical Examples

- Example 1: Calculating the sum of a list of numbers
```
    Initialise the sum to 0
    FOR each number in the list
        ADD the number to sum
    END FOR LOOP
```

- Example 2: Finding the maximum number in a list
```
    Initialise maximum value to the first number of the list
    FOR each number in the list
        IF number is greater than max THEN
            Set max to number
        ENF IF
```