"""
11.2.2 一个要测试的类
类的测试与函数的测试相似
大部分工作是测试类中的方法的行为
下面编写一个要测试的类：
"""

class AnonymousSurvey:
    """收集匿名调查问卷的答案"""
    def __init__(self,question):
        """存储一个问题，为存储答案做准备"""
        self.question = question
        self.responses = []
    
    def show_questions(self):
        """显示调查问卷"""
        print(self.question)

    def store_responses(self,new_response):
        """存储单份调查问卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答案"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
