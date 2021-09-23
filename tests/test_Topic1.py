import sys
sys.path.append(".")

# Import the student solutions
import Topic1_helper

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
answers = joblib.load(str(DIR)+"/answers_Topic1.joblib")

def test_exercise_1():
    assert Topic1_helper.count("ACAACTATGCATACTATCGGGAACTATCCT","ACTAT") == answers['answer_exercise_1a']
    
def test_exercise_2():
    assert Topic1_helper.frequent_words("ACAACTATGCATACTATCGGGAACTATCCT",4) == answers['answer_exercise_2a']

def test_question_1():
    assert Topic1_helper.answer_question_1() == answers['answer_question_1']

def test_exercise_3():
    assert Topic1_helper.reverse_complement("cagt") == answers['answer_exercise_3']
    
def test_exercise_4():
    assert Topic1_helper.frequency_table(Lab1.text,3) == answers["answer_exercise_4"]

def test_exercise_5():
    assert Topic1_helper.better_frequent_words(Lab1.text,9) == answers["answer_exercise_5"]
    
def test_exercise_6():
    assert Topic1_helper.skew(Lab1.genome) == answers["answer_exercise_6"]
