# Employee Scheduling App (windows)
A basic medical job scheduling GUI tools. (python)
In this app, we provided:

&nbsp;&nbsp;**custom setting for departments (like department A cannot/only schedule work on 09.01)**

&nbsp;&nbsp;**auto-scheduling, here we use ortools lib provided by Google (supporting C++/Python/Java/Js)**

&nbsp;&nbsp;**automatically generating the .doc file with tables of schedule**

To use the app, we need to pip-download the following python libs:

```
python -m pip install python-docx
```
```
python -m pip install --upgrade --user ortools
```
```
python -m pip install pygame
```
then cd the folder, and run
```
python .\content_view.py
```
Here are the basic steps:

&nbsp;&nbsp;**1. select the year and month**

&nbsp;&nbsp;**2. choose the target departments and set their constraints (add mode / delete mode)**

&nbsp;&nbsp;**3. click the generate button, wait a while then you could see the finishing .docx file in the app folder (if not succeed, the app will exit)**

Here are some figures of the app:






