class HighScores:
    def __init__(self, scores):
        self.scores = scores


    def latest(self):
        return self.scores[-1]
    
    
    def personal_best(self):
        return self.personal_top_three()[0]
    
    
    def personal_top_three(self):
        buffer = self.scores.copy()
        buffer.sort(reverse = True)
        if len(buffer) < 3:
            return buffer[0:len(buffer)]
        return buffer[0:3]
