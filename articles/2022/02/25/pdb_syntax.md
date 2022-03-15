

`b(reak) [ ([filename:]lineno | function) [, condition] ]`

p
pp
ll
l


n (next)
s (step)
using breakpoints with b (break)
c (continue).

unt (until) -- Without lineno, continue execution until the line with a number greater than the current one is reached. With lineno, continue execution until a line with a number greater or equal to that is reached. In both cases, also stop when the current frame returns.

display 	display [expression] 	Display the value of expression if it changed, each time execution stops in the current frame. Without expression, list all display expressions for the current frame.

ndisplay 	undisplay [expression] 	Do not display expression any more in the current frame. Without expression, clear all display expressions for the current frame.

w(where) - to print stacktrace
ou can use the two commands
u (up) [count]
d (down) [count]
to change the current frame



p 	Print the value of an expression.
pp 	Pretty-print the value of an expression.
n 	Continue execution until the next line in the current function is reached or it returns.
s 	Execute the current line and stop at the first possible occasion (either in a function that is called or in the current function).
c 	Continue execution and only stop when a breakpoint is encountered.
unt 	Continue execution until the line with a number greater than the current one is reached. With a line number argument, continue execution until a line with a number greater or equal to that is reached.
l 	List source code for the current file. Without arguments, list 11 lines around the current line or continue the previous listing.
ll 	List the whole source code for the current function or frame.
b 	With no arguments, list all breaks. With a line number argument, set a breakpoint at this line in the current file.
w 	Print a stack trace, with the most recent frame at the bottom. An arrow indicates the current frame, which determines the context of most commands.
u 	Move the current frame count (default one) levels up in the stack trace (to an older frame).
d 	Move the current frame count (default one) levels down in the stack trace (to a newer frame).
h 	See a list of available commands.
h <topic> 	Show help for a command or topic.
h pdb 	Show the full pdb documentation.
q 	Quit the debugger and exit.