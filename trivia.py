import requests
import json
import random
from html.parser import HTMLParser
from string import ascii_uppercase

class Trivia:

  def __init__(self):
    self.url = 'https://opentdb.com/api.php?amount=1'
  
  def get_question(self):
    r = requests.get(self.url).text
    result = json.loads(r)['results'][0] 
    question = result['question']
    self.correct_answer = result['correct_answer']
    answers = result['incorrect_answers']
    answers.append(self.correct_answer)
    question = self.format_question(question, answers)
    return question

  def format_question(self, question, answers):
    random.shuffle(answers)
    for index, answer in enumerate(answers):
      letter = ascii_uppercase[index]
      if answer == self.correct_answer:
        self.correct_letter = letter
      question += ' ' + letter + '. ' + answer
    question = HTMLParser().unescape(question)
    return question

  def check_answer(answer, correct_letter, correct_answer):
    if correct_letter.lower() == answer.lower():
      return 'Correct!'
    else:
      return 'Incorrect. The correct answer is ' \
        + correct_letter + '. ' + correct_answer