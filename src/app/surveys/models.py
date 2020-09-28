import datetime
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ARRAY
from app import sqlAlchemy as db

class Surverys(db.Model):

    __tablename__ = 'surverys'

    id = db.Column(
        db.Integer,
        nullable = True,
        unique = True,
        primary_key = True
    )
    name_survery = db.Column(
        db.String(30),
        nullable = True
    )
    questions = db.Column(
        db.ARRAY(String),
        nullable = True
    )
    answers_correct = db.Column(
        db.ARRAY(Integer),
        nullable = True
    )
    deadline = db.Column(
        db.DateTime,
        nullable = True
    )
    created_date = db.Column(
        db.DateTime,
        nullable = True,
        default = datetime.datetime.now
    )
    labels = db.Column(
        db.ARRAY(String),
        nullable = True
    )
    # Foreign Key
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )
    answers = db.relationship('Answers')

    def __init__(self,
        name_survery: str, 
        questions: list, 
        answers_correct: list, 
        deadline: datetime, 
        labels: list, 
        user_id: int
    ):
        self.name_survery = name_survery
        self.questions = questions
        self.answers_correct = answers_correct
        self.deadline = deadline
        self.labels = labels
        self.user_id = user_id

    def save(self) -> str:
        if not self.id:
            db.session.add(self)
        db.session.commit()
        return 'Se guardo la encuesta correctamente!'

    @staticmethod
    def get_survery_by_id(id: int):
        return Surverys.query.filter_by(id = id).first()

    @staticmethod
    def get_survery_all():
        return Surverys.query.all()

class Answers(db.Model):
    __tablename__ = 'answers'

    id = db.Column(
        db.Integer,
        nullable = True,
        unique = True,
        primary_key = True
    )
    user = db.Column(
        db.String,
        nullable = True
    )
    answer = db.Column(
        db.Integer,
        nullable = True
    )
    answer_date = db.Column(
        db.DateTime,
        nullable = True,
        default = datetime.datetime.now
    )
    # Foreign Key
    survery_id = db.Column(
        db.Integer,
        db.ForeignKey('surverys.id')
    )

    def __init__(self, 
        user: str,
        answer_date: datetime,
        answer: int,
        survery_id: int
    ):
        self.user = user
        self.survery_id = survery_id
        self.answer_date = answer_date
        self.answer = answer

    def save(self) -> dict:
        # Obtener Encuesta
        survery = Surverys.get_survery_by_id(self.survery_id)
        
        # Obtener fechas limites y fecha actual
        deadline = survery.deadline
        date_now = datetime.datetime.combine(
            datetime.date.today(), datetime.time(0, 0)
        )
        
        # Comprobar si la fecha caduco
        if deadline >= date_now:
            if not self.id:
                db.session.add(self)
            db.session.commit()

            response = {
                'error': False,
                'msg': 'Respuestas Guardadas!'
            }
            return response
        else:
            response = {
                'error': True,
                'msg': 'La encueta ya caduco!'
            }
            return response

    @staticmethod
    def get_answers_of_survery(survery_id: int):
        return Answers.query.join(Surverys).filter(Surverys.id == survery_id).all()
