class Process :
    def __init__(self,pid,clock = None):
        self.pid = pid
        self.clock = 0
        self.timestamps = {}

    def event(self,label):
        self.clock +=1
        print(f'{label} Process {self.pid} performed an event at time {self.clock}')
        self.timestamps[label]= self.clock
        return self.clock
        

    def sendmsg(self,label):
        print(f'{label} Process {self.pid} sent msg at time {self.clock}')
        return self.clock

    def receivemsg(self,label,msg_time):
        self.clock = max(self.clock,msg_time) +1
        print(f'{label}: Process {self.pid} received a message. Clock updated to {self.clock}')
        self.timestamps[label]= self.clock
        return self.clock

p1 = Process('p1')
p2 = Process('p2')
p3 = Process('p3')

p1.event('a')
p1.event('b')
p2.event('i')
timeb = p1.sendmsg('b')
timei = p2.sendmsg('i')
p1.receivemsg('c',timei)
p2.receivemsg('j',timeb)
p1.event('d')
p3.event('l')
p3.event('m')
timem = p3.sendmsg('m')
p1.receivemsg('f',timem)
p1.event('g')
timeg = p1.sendmsg('g')
p2.receivemsg('k',timeg)
p1.event('h')
print(p1.clock)
print(p2.clock)
print(p3.clock)
print(p1.timestamps)
print(p2.timestamps)
print(p3.timestamps)


# a Process p1 performed an event at time 1
# b Process p1 performed an event at time 2
# i Process p2 performed an event at time 1
# b Process p1 sent msg at time 2
# i Process p2 sent msg at time 1
# c: Process p1 received a message. Clock updated to 3
# j: Process p2 received a message. Clock updated to 3
# d Process p1 performed an event at time 4
# l Process p3 performed an event at time 1
# m Process p3 performed an event at time 2
# m Process p3 sent msg at time 2
# f: Process p1 received a message. Clock updated to 5
# g Process p1 performed an event at time 6
# g Process p1 sent msg at time 6
# k: Process p2 received a message. Clock updated to 7
# h Process p1 performed an event at time 7
# 7
# 7
# 2
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 5, 'g': 6, 'h': 7}
# {'i': 1, 'j': 3, 'k': 7}
# {'l': 1, 'm': 2}


class Process :

    def __init__(self,pid):
        self.pid = pid
        self.clock = 0
        self.timestamps={}

    def event(self,label):
        self.clock +=1
        print(f'{label} process {self.pid} executes at time {self.clock}')
        self.timestamps[label] = self.clock
        return self.clock
    
    def sendmsg(self,label):
        print(f'{label} process {self.pid} sends at time {self.clock}')
        return self.clock
    
    def receivemsg(self,label,time):
        self.clock = max(time,self.clock) +1
        print(f'{label} process {self.pid} receives at time {self.clock}')
        self.timestamps[label] = self.clock
        return self.clock
    
p1 = Process('p1')
p2 = Process('p2')
p3 = Process('p3')

p1.event('a')
p1.event('b')
p2.event('i')
timeb = p1.sendmsg('b')
timei = p2.sendmsg('i')
p1.receivemsg('c',timei)
p2.receivemsg('j',timeb)
p1.event('d')
p3.event('l')
p3.event('m')
timem = p3.sendmsg('m')
p1.receivemsg('f',timem)
p1.event('g')
timeg = p1.sendmsg('g')
p2.receivemsg('k',timeg)
p1.event('h')
print(p1.clock)
print(p2.clock)
print(p3.clock)
print(p1.timestamps)
print(p2.timestamps)
print(p3.timestamps)