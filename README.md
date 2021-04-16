# polls-api-polls

git clone
pip install -r requirements.txt

cd app
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver


Admin
/account/login
/account/logout/

- Polls CRUD 
GET /polls/
POST /poll-create/
GET /poll-detail/<int:pk>/
PUT /poll-update/<int:pk>/
DELETE /poll-delete/<int:pk>/

- Questions CRUD
GET /questions/<int:pk>/
POST /question-create/
GET /question-detail/<int:pk>/
PUT /question-update/<int:pk>/
DELETE /question-delete/<int:pk>/

User
GET /polls-active/  show active polls
POST /answer-create/
GET /answers/<int:pk>/  show user's answers
