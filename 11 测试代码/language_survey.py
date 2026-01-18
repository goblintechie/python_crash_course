"""
为了证明AnonymousSurvey能正确工作，编写一个使用它的程序
"""
from survey import AnonymousSurvey

# 定义一个问题，创建一个调查
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_questions()
print("Enter 'q' at anytime to quit.\n")
while True:
    response = input("Language:")
    if response == 'q':
        break
    my_survey.store_responses(response)

# 显示调查结果
print("\nThank you to everyone who participated in the survey.")
my_survey.show_results()
