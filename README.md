Django URL Reporter
====================

Customised Django URL Reporter. Generates a summary of the content of the URL.

Getting Started
---------------

I'm assuming you have Python installed. It is preferable to have a virtual environment for the project libraries.
Also assuming you've git setup on your system.

Setting Up the Virtual Environment (skip this if you want to mess-up your python libraries :P)
-------------------------------------------------------------------------------------------

If you're using pip to install packages (and I can't see why you wouldn't), you can get both virtualenv and virtualenvwrapper by simply installing the latter.

            pip install virtualenvwrapper

After it's installed, add the following lines to your shell's start-up file (.zshrc, .bashrc, .profile, etc).

            export WORKON_HOME=$HOME/.virtualenvs
            export PROJECT_HOME=$HOME/directory-you-do-development-in
            source /usr/local/bin/virtualenvwrapper.sh

Reload your start up file (e.g. source .bashrc) and you're ready to go.

Creating a virtual environment is simple. Just type

            mkvirtualenv url-report

or If already created the Virtual Environment, just start the environment by typing

            workon url-report


Getting the App Running
-----------------------

Installing Python Packages and getting the app running is just like eating chocolate.

            cd /path/where/you/want/your/project
            git clone git@bitbucket.org:verdanmahmood/django-url-reporter.git
            cd django-url-reporter/
            
Packages can be installed using pip command.
This command installs the packages in the requirement file.
            
            pip install -r requirements.txt
            
Start the Server
            
            python manage.py runserver
                      
            