# Chit-Chat
A chit chat app in which the user will be able to send messages back and forth with a bot. 

# Follow these directions
0. `cd ~/environment && git clone https://github.com/PRamos/project2-m1-par25`  
1. Install your stuff!  
  a) `npm install`  
  b) `pip install flask-socketio`  
  c) `pip install eventlet`  
  d) `npm install -g webpack`  
  e) `npm install --save-dev webpack`  
  f) `npm install socket.io-client --save`  
If you see any error messages, make sure you use `sudo pip` or `sudo npm`. If it says "pip cannot be found", run `which pip` and use `sudo [path to pip from which pip] install`
2. Run your code!  
  a) `npm run watch`. If prompted to install webpack-cli, type "yes"  
  b) In a new terminal, `python app.py`  
  c) Preview Running Application (might have to clear your cache by doing a hard refresh)  
3. Play with the app by clicking the button and seeing what happens!  
4. Answer the following questions:  
  a) Is the random number generated by the client or the server?  
  b) Is the random number rendered by the client or server?  
  c) What are the steps that happen after the random number is generated?  

# Follow these aswell
# Set up React  
1. Install your stuff!    
  a) `npm install -g webpack && npm install --save-dev webpack && npm install socket.io-client --save`    
  b) `pip install flask-socketio`    
  c) `pip install eventlet`    
:warning: :warning: :warning: If you see any error messages, make sure you use `sudo pip` or `sudo npm`. If it says "pip cannot be found", run `which pip` and use `sudo [path to pip from which pip] install`  :warning: :warning: :warning:  
</div>
  
# Getting PSQL to work with Python  
1. Update yum: `sudo yum update`, and enter yes to all prompts    
2. Upgrade pip: `sudo pip install --upgrade pip`  
3. Get psycopg2: `sudo pip install psycopg2-binary`    
4. Get SQLAlchemy: `sudo pip install Flask-SQLAlchemy==2.1`    
  
# Setting up PSQL  
1. Install PostGreSQL: `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`    
    Enter yes to all prompts.    
2. Initialize PSQL database: `sudo service postgresql initdb`    
3. Start PSQL: `sudo service postgresql start`    
4. Make a new superuser: `sudo -u postgres createuser --superuser $USER`    
    :warning: :warning: If you get an error saying "could not change directory", that's okay! It worked!  
5. Make a new database: `sudo -u postgres createdb $USER`    
        :warning: :warning: If you get an error saying "could not change directory", that's okay! It worked!  
6. Make sure your user shows up:    
    a) `psql`    
    b) `\du` look for ec2-user as a user    
    c) `\l` look for ec2-user as a database    
7. Make a new user:    
    a) `psql` (if you already quit out of psql)    
    ## REPLACE THE [VALUES] IN THIS COMMAND! Type this with a new (short) unique password.    
    b) I recommend 4-5 characters - it doesn't have to be very secure. Remember this password!   
        `create user [some_username_here] superuser password '[some_unique_new_password_here]';`   
        :warning: this should look like `create user sresht superuser password 'mypass';` :warning:   
    c) `\q` to quit out of sql    
8. make a new file called `sql.env` and add `SQL_USER=` and `SQL_PASSWORD=` in it  
9. Fill in those values with the values you put in 7. b)  

# Setting up Joke API and getting Funtranslate working
Go to https://sv443.net/jokeapi/v2/
Click on request form and select the jokes you want, copy the link and insert link into the app.py under the joke api.
Joke api will automatically work with no key involved
then Go to funtranslate and subscribe to a translate, once obtained the API key, send the key inside your sql.env file under Key

# Setting up the OAuth Google:
Go to https://console.developers.google.com/ and sign up using your PERSONAL google account.
⚠️ ⚠️ Do NOT use your NJIT account! You must use your personal account ⚠️ ⚠️
Click "CREATE PROJECT" or in the dropdown menu called "Select a Project" in the top, click "NEW PROJECT".
Make a new project named cs490-lect12. "No organization" is fine.
Click "Credentials" in the left hand bar, then click "+ CREATE CREDENTIALS" and then click "OAuth client ID".
4.5. If you see a warning that says "To create an OAuth client ID, you must first set a product name on the consent screen", do the following steps:
1. Click the "CONFIGURE CONSENT SCREEN" button.
2. Choose "External"
3. For "Application name," specify "CS490 Lect12" or something similar.
4. Press save.
Go back to Credentials -> Create Credentials -> OAuth client ID. Click "web application".
5. Set up the ID inside GoogleButton.jsx and input the id given inside clientId
6. type `npm install react-google-login` in the terminal and youre good to go

# Setting up the imports
type `pip install rfc3987` inside the terminal, it should be working immediately after that

# Enabling read/write from SQLAlchemy  
There's a special file that you need to enable your db admin password to work for:  
1. Open the file in vim: `sudo vim /var/lib/pgsql9/data/pg_hba.conf`  
:warning: :warning: :warning: If that doesn't work: `sudo vim $(psql -c "show hba_file;" | grep pg_hba.conf)`  :warning: :warning: :warning:  
2. Replace all values of `ident` with `md5` in Vim: `:%s/ident/md5/g`  
3. After changing those lines, run `sudo service postgresql restart`  
4. Ensure that `sql.env` has the username/password of the superuser you created!  
5. Run your code!    
  a) `npm run watch`. If prompted to install webpack-cli, type "yes"    
  b) In a new terminal, `python app.py`    
  c) Preview Running Application (might have to clear your cache by doing a hard refresh)    
6. You should just see the same random number as lect10's socket demo.

#  Finally
1. For your sql.env file create a functions call `Key` and add the api_key for funtranslate
2. and you are good to go

## Technical Issues

1. For this milestone a technical issue I found was the authentication for google wasnt working as intended to fix this was just simply deleting cache and cookies within the last hour on the web browser you are currently using it should be under settings
2. Another technical issue is depending on the web browser the messages might be a bit disarrayed and ouot of column, the fix to this was keeping them in a fixed position within the css. for other web browsers aside from microsoft edge brav and google chroome i havent checked if those same issues lie within those browsers

## Ways to improve this project if I had more time
1. When making milestone 2 the count function on the top left of the screen would not work correctly, It couldve been a simple fix but simply no time to deal with it since it poses and causes so many errors if i tried
2. if I had more time I would like to fix the orientation of the google button as it lies on the top left of its panel in the middle of the screen, this isnt a huge issue but for aesthetic reasons i hope to fix it in the near future.
