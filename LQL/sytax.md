# LogScale and Splunk SPL Syntax Differences

## Parentheses `()`

### LogScale
- Used to encapsulate arguments in function calls.

### Splunk SPL
- Used to group operations and define the order of operations, similar to their use in mathematics.
- Also used to encapsulate arguments in function calls.

## Square Brackets `[]`

### LogScale
- Used to define arrays or lists.

### Splunk SPL
- Used to define subsearches, which are searches that run within another search.

## Curly Braces `{}`

### LogScale
- Used in `case` and `match` statements to define conditions and their corresponding actions.
- Also used to encapsulate subqueries in `join` statements.

### Splunk SPL
- Not commonly used. When they are used, it's typically in the context of advanced statistical commands or macros.

## General Syntax

### LogScale
- More similar to traditional programming languages, with a focus on expressions and functions.

### Splunk SPL
- Based on a pipeline model where each command or function operates on the results of the previous command or function. This is represented by the pipe character `|`.
