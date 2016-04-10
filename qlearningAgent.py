  
  class QLearningAgent:
    
    def __init__(self):
      
  
    def update_Qvalue(self, pstate, action, state, reward):
        max_qvalue = max([AgentG.get_Qvalue(self, state, a) for a in self.actions)])
        value = reward + self.gamma * max_qvalue
        old_qvalue = Agent.Qvalues.get(str(pstate), str(action), None)
        
        if old_qvalue = None:
            self.Qvalues[(str(pstate), str(action))] = reward
        else:
            self.Qvalues[(str(pstate), str(action))] = reward + self.gamma * (max_qvalue - old_value)
    
    def choose_actions(self):
        if random.random() <= self.epsilon:
            return self.actions[np.random.choice(len(self.actions))]
        else:
            q = [Agent.get_Qvalue(self, state, a) for a in self.actions]
            maxQ = max(q)                
            count = q.count(maxQ)
        
        if count > 1:
            best = [i for i in range(len(self.actions)) if q[i] == maxQ]
            i = best[np.random.choice(len(best))]
        else:
            i = q.index(maxQ)

        action = self.actions[i]
        return action
        
    def get_actions(self):
