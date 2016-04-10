class     
    
    def update_Qvalue(self, pstate, action, state, reward):
        max_qvalue = max([GameManager.get_Qvalue(self, state, a) for a in self.actions)])
        value = reward + self.gamma * max_qvalue
        old_qvalue = GameChanger.Qvalues.get(str(pstate), str(action), None)
        
        if old_qvalue = None:
            self.Qvalues[(str(pstate), str(action))] = reward
        else:
            self.Qvalues[(str(pstate), str(action))] = reward + self.gamma * (max_qvalue - old_value)
    
    def choose_actions(self):
        if random.random() <= self.epsilon:
            return self.actions[np.random.choice(len(self.actions))]
        else:
            q = [GameManager.get_Qvalue(self, state, a) for a in self.actions]
            maxQ = max(q)                
            count = q.count(maxQ)
        
        if count > 1:
            best = [i for i in range(len(self.actions)) if q[i] == maxQ]
            i = best[np.random.choice(len(best))]
        else:
            i = q.index(maxQ)

        action = self.actions[i]
        return action
            
    def get_Qvalue(self, state, action):
        return self.Qvalues.get(str(state), str(action), 0.0)
