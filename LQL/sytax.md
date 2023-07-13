# LogScale and Splunk SPL Syntax Differences

## Parentheses `()`

### LogScale
- Used to encapsulate arguments in function calls.

### Splunk SPL
- Used to group operations and define the order of operations, similar to their use in mathematics.
- Also used to encapsulate arguments in function calls.

## Square Brackets `[]`

### LogScale
- Used to define arrays or lists (e.g. calling multiple fields field=() vice field=([]).

### Splunk SPL
- Used to define subsearches, which are searches that run within another search.

## Curly Braces `{}`

### LogScale
- Used in `case` and `match` statements to define conditions and their corresponding actions.
- Also used to encapsulate subqueries in `join` statements.

### Splunk SPL
- Not commonly used. When they are used, it's typically in the context of advanced statistical commands or macros.
