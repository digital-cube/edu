Some of metacharacter examples:
===============================

`.` Normally matches any character except a newline. Within square brackets the dot is literal.

```python
    $string1 = "Hello World\n";
    if ($string1 =~ m/...../) {
     print "$string1 has length >= 5.\n";
    }
```

**Output**
```
    Hello World
    has length >= 5.
```
