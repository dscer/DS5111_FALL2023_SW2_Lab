# DS5111_FALL2023_SW2_Lab

1) What did you have to do to get make to work?

2) Similarly for python3 -m venv env, what did you have to do? (How likely are you to have guessed that without their clear error message?)

3) Both the pip install on the requirements.txt, and the call to run bin/clockdeco_param.py should be activating the virtual environment first. In other words, there are two bash commands separated by a ;, the first of which activates. Why can't we just do that on a separate line? In other words, why do we have to do that in one line and separate the commands with a ;

4) As it is, both the env and tests jobs run differently in that only one runs if the directory exists. This is as intended and all is well. What do you think about the job run? What would happen if you accidentaly had a file called run in your directory? What can we do to fix this?

5) The code provided to you for the test file starts with two lines, seemingly to append something to sys.path. What is the purpose of these lines?
