# How to Set Up this Project
# Clone
clone repo
`git clone https://github.com/PyaePhyoKhant/castle-test.git`
then cd to root directory
`cd castle-test`

# Virtual Environment
create virtual environment and install requirements (this may take a few seconds)
`pipenv install`
start virtual environment
`pipenv shell`
the steps below should be inside shell or otherwise it may cause error

# Database (this step may not be needed)
apply django migrations
`python manage.py migrate`

# Server
runserver
`python manage.py runserver`
currently, two accounts were created
| Username  | Password |
|-----------|----------|
| aungkaung | 1h-jp!8* |
| blank     | 1h-jp!8* |

# Creating New User (Optional)
`python manage.py createsuperuser`
