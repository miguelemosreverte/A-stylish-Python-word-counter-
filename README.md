# A-stylish-Python-word-counter-
... for a job interview
![asd](https://i.imgur.com/qnLVSMc.png)



## assumptions
- #### If I were to make a program like this, I would make it because I needed to count the ocurrences of words of many files.

Being that the case:
- I would only be focused on the current number of ocurrences, not the historic one.
- So, it would be no problem if a file is processed two times for it to overwrite  the db entry for it's filepath.
- However it was assumed legibility of the data was going to be indeed important, and present values for the word ocurrences would be the only information I would want present on screen.

- ### "Besides, the script should print the last 10 searches perfomed per file"
- Is it the 10 last search _results_? Okay, scratch the last assumption. We are going to make a verbose program that informs the user about _each_ past search.
