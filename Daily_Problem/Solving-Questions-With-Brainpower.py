class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        i = 0
        already_computed = {}
        return self.findMaxPoints(questions,i,already_computed)
        
    def findMaxPoints(self,questions: List[List[int]], i:int, already_computed:dict) -> int:
        if i in already_computed:
            return already_computed[i]
        
        # Solve the current question
        points_1 = questions[i][0]
        if i+1<len(questions):
            # Skip the current question
            points_2 = self.findMaxPoints(questions,i+1,already_computed)
        else:
            # There are no more questions
            already_computed[i] = points_1
            return points_1
        if i+1+questions[i][1] < len(questions):
            points_1 += self.findMaxPoints(questions,i+1+questions[i][1],already_computed)
        max_points =  max(points_1,points_2)
        already_computed[i] = max_points
        # print(already_computed)
        return max_points