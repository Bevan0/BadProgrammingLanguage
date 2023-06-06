# BadProgrammingLanguage
Brainfuck but just slightly less brainrotting

All Brainfuck code will work, but this has a couple more features. I made this in May 2022 and have not touched it since. `example.bad` is a number guessing game and `improvements.bad` is a micro-tutorial of a few of the new features.

## New features
`#` makes the rest of the line a comment.
`%name` saves the current memory pointer with the name `name`.
`&name` is the same as `%` but for the instruction pointer.
`!name` will jump to the pointer, whichever type it is.
`^Text^` will print `Text`.
`~` is the same as `.` but prints the integer value.
`=value` will set the value of the current memory address to `value`.