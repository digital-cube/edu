Regular expressions
===================


Regular expressions are the linguistic extension and expansion of functionality wildcards (*, ? i %). They represent an important and significant tool in natural language processing.

Their role is to:
 - provide an easy way to define the template (sample) by which will create a certain text data
 - based on the established template (samples) perform validation paragraph text into its composition meets the structure of the template
 - find the text of those parts that meet a set structure of the template (sample)

Regular Expressions characterized:
 - set of metacharacters that form regular expressions
 - a set of rules to generate templates (patterns)

Metacharacters are:
___________________

```bash
    . ^ $ * + ? { } [ ] \ | ( )
```

**Metacharacter**       **Meaning**

**[ ]** `Any character enclosed in the brackets [ ]. If metacharacters is within [ ] is treated as an ordinary character.`

**^** `Start input or row. If the character set in the [ ] starts with this symbol, it is a complementary set given.`

**$** `End of input or row.`

**\*/** `Previous character repeated 0 or more times.`

**+** `Previous character repeated 1 or more times.`

**?** `Previous character repeated 0 or 1 time`

**.** `One character except  character for the transition in the new row.`

**|** `The choice between two regular expressions given by the left and right of the mark.`

**( )** `A group of characters which define the exact order of appearance.`

**-** `A group of characters in the range between the first and second, final.`

\ `The sign annulling the role of metacharacters and he is treated as an ordinary character.  If found in front of a particular character, form a predefined sequence.`

**{ }** `The previous mark was repeated as defined within the brackets.`

Predefined special sequences
____________________________

\w `Matches any character that is a letter, number or underscore (_).`

\W  `Matches any character that is not a letter, number or underscore (_).`

\d `Finds numbers.`

\D `Matches any character that is not a number.`

\A `Finds start low.`

\z `Finds low end.`

\Z `He finds a place low. If There is no sign of the transition to the new row, finds the character before him.`

\s `Finds spaces and tabs.`

\S `Finds any character other than a space or tab.`

\b `Finds matching at the beginning or\and the end of the word - the limit word.`

\B `Finds matching except at the beginning or\and end of words.`

\0 `Finds null sign.`

\n `Finds a newline character.`

\f `Finds new row.`

\r `Finds return character.`

\t `Finds the tabulator sign.`

\v `Finds vertical tab.`

\xxx `Finds the character specified by the octal number xxx.`

\xdd `Finds the character specified by the hexadecimal number dd.`

\uxxxx `Finds Unicode character specified by the hexadecimal number xxxx.`
