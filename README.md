**Git global setup**

1.  git config --global user.name "Firstname Lastname"
2.  git config --global user.email "example@example.com"

**Create a new repository**

1. git clone http://10.3.101.105/FLname/ofac_cc_proj 
2. cd ofac_cc_proj
3. touch README.md
4. git add README.md
5. git commit -m "add README"
6. git push -u origin master

**Existing folder**

1.  cd existing_folder
2.  git init
3.  git remote add origin http://10.3.101.105/FLname/ofac_cc_proj
4.  git add .
5.  git commit -m "Initial commit"
6.  git push -u origin master

**Existing Git repository**

1.  cd existing_repo
2.  git remote rename origin old-origin
3.  git remote add origin http://10.3.101.105/FLname/ofac_cc_proj
4.  git push -u origin --all
5.  git push -u origin --tags

**--------------------------------------------------------------------**

**Install things**
You will need python3
You will need MPI (mpi4py): mpi installation steps can be found in the **'Installing MPI Single Node'** file. -  this is under the static directory.

1. Create a virtual environment using python3
2. source venv/bin/activate
3. export FLASK_APP=main.py
4. flask run