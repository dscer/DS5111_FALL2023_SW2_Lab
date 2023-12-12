# DS5111_FALL2023_SW2_Lab

1) What did you have to do to get `make` to work? 

The first step is to `sudo apt update`, then `sudo apt install make`.

2) Similarly for `python3 -m venv env`, what did you have to do? (How likely are you to have guessed that without their clear error message?)

To get this command to work I had to run the following command `apt install python3.10-venv`. The error message made it very clear that needed to be done. Without it I would have looked up venv requirements are likely would have found something after searching a while but not as fast or effectively as the verbose error message.

3) Both the pip install on the requirements.txt, and the call to run bin/clockdeco_param.py should be activating the virtual environment first. In other words, there are two bash commands separated by a `;`, the first of which activates. Why can't we just do that on a separate line? In other words, why do we have to do that in one line and separate the commands with a `;`

In the makefile each line is isolated meaning we can put the commands on different lines if we want them to interact. The semicolon (`;`) is used to separate multiple commands that are associated with a single target. Therefore, we need to leverage this feature to activate the environment that has the requirements to run the python script. Otherwise we just ran a command to activate the environment then another to run python in a the system's python environment (/usr/bin/python3). 

4) As it is, both the `env` and `tests` jobs run differently in that only one runs if the directory exists. This is as intended and all is well. What do you think about the job `run`? What would happen if you accidentaly had a file called `run` in your directory? What can we do to fix this?

If we had a file called "run" running `make run` would return "run" is up to date. The following shows that scenario:

```
ubuntu@ip-172-31-45-242:~/DS5111_FALL2023_SW2_Lab$ touch run
ubuntu@ip-172-31-45-242:~/DS5111_FALL2023_SW2_Lab$ make run
make: 'run' is up to date.
ubuntu@ip-172-31-45-242:~/DS5111_FALL2023_SW2_Lab$ rm -rf run
ubuntu@ip-172-31-45-242:~/DS5111_FALL2023_SW2_Lab$ make run
[0.12322140s] snooze(0.123) -> None
[0.12322378s] snooze(0.123) -> None
[0.12318110s] snooze(0.123) -> None
```

5) The code provided to you for the test file starts with two lines, seemingly to append something to `sys.path`. What is the purpose of these lines?

sys.path is a built-in variable within the sys module. This variable contains a list of directories that the python interpreter will search in for the required module(s). Using the .append() method allows us to add a specific path for interpreter to search in. The sys.path.append(".") statement in our case is used to add the current working directory - the directory Python script is running in. With that path appended we can then import a module located in the same directory or in our case from the bin folder which contains our main script. I've also seen/used the approach where you add an empty __init__.py file to the various folders in the project for python to know which are python modules you can import from.

# Extra Credit

1) Execute sudo apt install tree, and use that application to print out the file and directory structure, just as it is shown in this document at the top. You will have to look up in the reading, or google it in stackoverflow, what flag you need to exclude the 'env' directory. No need to cut and paste the structure, just include the full line you used to get it working.

Using the `-I` flag we can add patterns we want to exclude. For our case its the `env` directory so the command `tree -I 'env'` will achieve the intended results.

2) Your .gitignore has 'env/', and also a callout to ignore the compiled python files, the ones in `__pycache__` folders. What is the meaning of the `**/*`?

A leading `**` followed by a slash means match in all directories. An asterisk `*` matches anything except a slash. Therefore, `**/*` pattern is used to wildcard match all files and directories recursively meaning we can ignore the complied python files in the `__pycache__` folder wherever it is found in the repo rather specifying specific paths to each individual `__pycache__` foldern that was generated.  

3) Do a `pip list` or `pip freeze` and call out versions of the pytest and pylint packages in your requirements.txt. Include them in your requirements.txt, and for the extra credit, just add a note reminding me you included them.

`pip freeze > requirements.txt` was used to update the file with specific package versions used in the `env` venv.

4) In the sample code from the book, why does the line `if __name__=="__main__":` allow the script to run if called directly, but not otherwise? What's going on there?

That line allows the program to determine if the script is being run directly as the main program or if it is being imported as a module into another script. `__main__` is the name of the environment where top-level code is run. When a Python module or package is imported, `__name__` is set to the module’s name. Therefore, we can compare the two to determine if the script is being imported as a module or run if is in fact "__main__" - a.k.a the driver script.

5) If you add two print statements, (or any statements for that matter), one above and one below the `if __name__...` line, what would happen when I do an `import` of the file? What happens when I call the file directly with `python <filename>`. Most importantly, `why?`.

If you add any print statments above or below, but not inside `if __name__ ...` those will be print to the console when you import the file because the script is executed sequentially when its imported. Any print statments that are within the `if __name__ ...` will only print to the console if the file is run directly. This is because anything in the `if __name__ ...` statment will be run if the file is run directly (see response to question 4). 

