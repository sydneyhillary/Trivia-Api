# Full Stack Trivia API Project

This is the Udacity project where you get to test your knowledge with some nice trivia questions. The project has functionalities such as:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.


## Getting Started
Developers should have Python3, pip3, node, and npm installed.

### Frontend Dependencies
This project depends on Nodejs and Node Package Manager (NPM). You must download and install Node. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```


### Backend

Setup the virtual env

```
python -m virtualenv env
source env/bin/activate
```
windows:
```
source env/Scripts/activate
```

Once you have your virtual environment setup and running, install dependencies by naviging to the 
`/backend` directory and running:

```
pip install -r requirements.txt
```

## Running Your Frontend in Dev Mode
The frontend app was built using create-react-app. In order to run the app in development mode use npm start. You can change the script in the package.json file.

Open http://localhost:3000 to view it in the browser. The page will reload if you make edits.

```
npm start
```

### DATABASE SETUP
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```
psql trivia < trivia.psql
```
### RUNNING THE SERVER
From within the backend directory first ensure you are working using your created virtual environment.

To run the server, execute:

```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
### Testing 

To run the tests, run

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## Endpoints

### GET /categories
* Returns a list of categories
* Example: `curl http://localhost:5000/categories`

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```
### GET /questions
* Get a list of questions paginated in groups of 10 with categories and answers
* Example: `curl http://127.0.0.1:5000/questions`

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 20
}
```

### GET /categories/int:id/questions
* Returns questions based on Category id
* Example `curl http://localhost:5000/categories/5/questions`

```
{
  "current_category": "Entertainment",
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Katherine",
      "category": 5,
      "difficulty": 2,
      "id": 24,
      "question": "Who was Elena's double in Vampire Diaries?"
    }
  ],
  "success": true,
  "total_questions": 20
}
```

### POST /questions
* Create a new question with :
    * Answer
    * Difficulty
    * Category
* Example: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"What is the real name of the main protagonist in the netflix show LUPIN", "answer": "Omar Sy","category" :"5", "difficulty":"3"}'`

```
{
      "answer": "Omar Sy",
      "category": 5,
      "difficulty": 3,
      "id": 25,
      "question": "What is the real name of the main protagonist in the netflix show LUPIN"
    }
],
  "success": true,
  "total_questions": 21
```

### POST /questions/search
* Search questions with searchTerm
* Example: ` curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm": "tom"}'`

```
{
  "current_category": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }
  ],
  "success": true,
  "total_questions": 1
}
```

### DELETE /questions/int:question_id
* Deletes a question by id

* Example: `curl http://127.0.0.1:5000/questions/6 -X DELETE`

```
{
  "deleted": 6,
  "questions": [
    {
     ...........
    }
  ],
  "success": true,
  "total_questions": 20
}
```

### POST /quizzes
* Play the quiz game
* Retrieve the question and its category
* Example: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"quiz_category":{"type":"Entertainment","id":"5"}, "previous_questions":[7]}'`

```
{
  "question": {
    "answer": "Omar Sy",
    "category": 5,
    "difficulty": 3,
    "id": 25,
    "question": "What is the real name of the main protagonist in the netflix show LUPIN"
  },
  "success": true
}
```

## Error Handling
* Errors are returned as JSON in the following format:
```
{
  "error": 405,
  "message": "Method not allowed",
  "success": false
}
```
* Types of Errors:
    * 400 - Bad request
    * 404 - Resource not found
    * 422 - Unprocessable
    * 405 - Method not allowed
    * 500 - Internal server error
