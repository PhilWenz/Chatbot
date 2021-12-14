@echo off

If exist venv\ goto start
goto setup

:setup
call create.bat
goto start

:start
echo Server wird gestartet.
call venv\Scripts\activate.bat
python chatbot\manage.py runserver 80

pause