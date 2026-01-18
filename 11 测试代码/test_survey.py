"""
11.2.3. 测试AnonymousSurvey类
下面编写一个测试，对AnonymousSurvey的行为的一个方面进行验证
如果用户只提供一个答案，答案能妥善保存，我们要核实这个答案确实存在于答案列表中
"""

import unittest
from survey import AnonymousSurvey

class TsetAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        """创建一个对象和一组答案，供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Chinese', 'English', 'Français']
    
    def test_store_single_response(self):
        """测试单个答案"""
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    
    def test_store_three_responses(self):
        """测试三个答案"""
        for response in self.responses:
            self.my_survey.store_responses(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

    # def test_store_single_response(self):
    #     """测试单个答案会被保存在答案列表中"""
    #     question = "What language did you first learn to speak?"
    #     my_survey = AnonymousSurvey(question)
    #     my_survey.store_responses('English')
    #     self.assertIn('English', my_survey.responses)
    
    # def test_store_three_responses(self):
    #     """测试三个答案会被保存"""
    #     question = "What language did you first learn to speak?"
    #     my_survey = AnonymousSurvey(question)
    #     responses = ['Chinese', 'English', 'Français']
    #     for response in responses:
    #         my_survey.store_responses(response)
    #     for response in responses:
    #         self.assertIn(response,my_survey.responses)
        
if __name__ == '__main__':
    unittest.main()
