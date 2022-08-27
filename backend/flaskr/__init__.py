import os
from unicodedata import category
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

# paginating questions
def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    # CORS + Allowing '*' for origins
    CORS(app, resources={'/': {'origins': '*'}})

    # after_request decorator to set Access-Control-Allow
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    # ............................................................................
    # GET REQUESTS
    # .............................................................................
    
    
    # Get Request for all categories
    # ..............................................................................
    @app.route("/categories", methods=['GET'])
    def get_categories():
        
        categories = Category.query.all()
        data = {}
        for category in categories:
            data[category.id] = category.type
            
        if (len(data) == 0):
            abort(404)
            
        return jsonify({
            "success": True,
            "categories": data
        })

    # ........................................................................................
    # Get requst for questions
    # ........................................................................................
    @app.route("/questions", methods=['GET'])
    def get_questions():
        selection = Question.query.order_by(Question.id).all()
        current_question = paginate_questions(request, selection)
        categories = Category.query.all()
        data = {}
        
        for category in categories:
            data[category.id] = category.type

        if len(current_question) == 0:
            abort(404)

        return jsonify(
            {
                'success': True,
                'questions': current_question,
                'total_questions': len(selection),
                'categories': data
            }
        )
    # Delete question 
    # ..........................................................................................
    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()

            if question is None:
                abort(404)

            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify(
                {
                    "success": True,
                    "deleted": question_id,
                    "questions": current_questions,
                    "total_questions": len(Question.query.all()),
                }
            )

        except:
            abort(422)

    # Post a question 
    # ..........................................................................................
    @app.route("/questions", methods=["POST"])
    def create_question():
        body = request.get_json()

        new_question = body.get("question", None)
        new_answer = body.get("answer", None)
        new_category = body.get("category", None)
        new_difficulty = body.get("difficulty", None)
        search = body.get("searchTerm", None)

        try:
            
            question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
            question.insert()

            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify(
                {
                    "success": True,
                    "created": question.id,
                    "question_created": question.question,
                    "questions": current_questions,
                    "total_questions": len(Question.query.all()),
                }
            )
        except:
            abort(422)
   
    # Search question
    # ..........................................................................................
    @app.route("/questions/search", methods=["POST"])
    def search_questions():
        body = request.get_json()
        search = body.get("searchTerm", None)
        
        try:
            if search:
                selection = Question.query.filter(Question.question.ilike
                                                  (f'%{search}%')).all()
                
                paginated = paginate_questions(request, selection)

            return jsonify({
                "success": True,
                "questions":  paginated,
                "total_questions": len(selection),
                "current_category": None
            })
        except:
            abort(404)
   
    # Get questions based on categories
    # .................................................................................................
    @app.route("/categories/<int:question_id>/questions")
    def questions_in_category(question_id):
        category = Category.query.filter_by(id=question_id).one_or_none()
        try:
           
            selection = Question.query.filter_by(category=category.id).all()
            paginated = paginate_questions(request, selection)

            return jsonify({
                'success': True,
                'questions': paginated,
                'total_questions': len(Question.query.all()),
                'current_category': category.type
            })
       
        except:
            abort(404)
   
    # Get Questions to play the quiz
    # ...........................................................................................
    @app.route('/quizzes', methods=['POST'])
    def get_quiz():
        try:
            body = request.get_json()
            
            previous = body.get("previous_questions", None)
            quiz_category = body.get("quiz_category", None)
           

            if quiz_category["id"] == 0:
                questions = Question.query.all()
            else:
                questions = Question.query.filter_by(
                    category = quiz_category['id']).all()
            question = None
            
            if(len(previous) < 1):
                question = questions[0].format()
            else:
                question = random.choice(questions).format()

            return jsonify({
                "success": True,
                "question": question
            })

        except Exception:
            abort(422)

    
    # Error handlers
    # .........................................................................................
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False, 
            "error": 400,
            "message": "Bad Request"
            }), 400
          
    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False, 
            "error": 405,
            "message": "Method not allowed"
            }), 405
            
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False, 
            "error": 404,
            "message": "Not found"
            }), 404
        
    @app.errorhandler(422)
    def uprecessable(error):
        return jsonify({
            "success": False, 
            "error": 422,
            "message": "Uprocessable"
            }), 422
        
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            'error': 500,
            "message": "Internal server error"
        }), 500

    return app

