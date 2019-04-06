#IceBot 
from  tkinter import *
#GUI initialization
class GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, bg='white')
        self.pack(expand=YES,fill=BOTH)
        self.window_init()
        self.createWidgets()   
        

    def signal(self, input):
        self.bind('<Return>', self.user_input.select_clear())           
        if input !="HI" or input !="hi":
                self.dia_text.insert(INSERT, "I can not answer your question, please try again!\n")              
     
    def get_input(self):
        e = self.createWidgets()
        return e
    
    def addToFrame (self):
        temp = []
        return temp 
    #GUI window size
    def window_init(self):
            self.master.title('IceBot')
            self.master.geometry("{}x{}".format(1024, 768))
          
    #Widgets
    def createWidgets(self):
        #initial chatbot
            isActive = 1
        #title & prompt
            prompt_data = ['major',
'birthday',
'food',
'drink',
'sport',
'color',
'weather',
'breakfast',
'homework',
'sleep',
'gym',
'coffee',
'class',
]
            #database
            data={
'major':['math','art','physics','computer science'],
'birthday':['october 10th 2000','today,june 17th 1997'],
'food':['pudding','cake','spaghetti','Kung pao chicken'],
'drink':['blood','7 up','Pepsi','orange juice'],
'sport':['soccer','badminton','basketball','archery'],
'color':['red','black','green','yellow'],
'weather':['sunny','snowy','rainy'],
'breakfast':['burger','cereal','corn','bread'],
'homework':['I haven''t finished it yet','Yesterday','uhhh, let''s change a topic'],
'sleep':['at 12:00 pm','at 3:00 am','I have sleep disorder yesterday...'],
'gym':['last month','yesterday','a week ago, I guess....'],
'coffee':['yesterday'],
'class':['no, I am a good student','uhh, maybe.''I refuse to answer this question.'],
'semester':['five courses','4 courses'],
'homework':['about 10 hours','about 2 hours'],
'games':['a whole day','5 hours'] ,
'job':['no, I have no time to work.''yes, I have.'],
'father':['his name is ChatbotA'],
'mother':['Her name is Sara'],
'cousin':['Her name is Sam'],
'sister':['Her name is Amy'],
'math':'steve',
'art':'Ronny',
'drama':'Abie',
'CS':'Aron',
'Social':'Aaron',
'History':'summer',
'friend':['I do not have friend except you','her name is annie, another chatbot'],
'hometomn':['kelowna','Mars'],
'summer':['vancouver','ontario'],
'game':'LOL',
'Car':'Audi'
}
            dataKey=list(data.keys())
            #interface 
            self.mainFrame = Frame(self, bg='white')
            self.Frame_title = Label(self.mainFrame, text = "IceBot", font=(42), bg='white', fg='#4169E1')
            self.Frame_title.pack(side=TOP)
            #title & initialization
            self.dia_text = Text(self.mainFrame, bg='white', width='100', height='30')
            self.dia_text.insert(INSERT,"Hello, I'm IceBot, These are some of the keywords (but not all) in my dataset, please have a look:\n")
            self.dia_text.insert(INSERT, prompt_data)
            
            self.dia_text.pack(side=LEFT)
            self.mainFrame.pack(side=TOP)
             
            #user input entry
            self.inputFrame = Frame(self, bg='white')
            
            self.warning = Label(self.inputFrame, text = "The GUI is still in development, please use the console instead", font=(42),bg='white').pack()
            self.prompt_user = Label(self.inputFrame, text = "Give me a word! (If you do not know what to ask, type \'help\')", bg='white').pack()
           
            self.user_input = Entry(self.inputFrame, font=(24), width='24')
            self.inputFrame.pack()
            
            #self.user_input.select_clear()
            self.user_input.pack()            
                    
            #scrollbar for history
            self.sb = Scrollbar(self.mainFrame)
            self.sb.pack(side=RIGHT, fill=Y)
            self.lb = Listbox(self.mainFrame, yscrollcommand=self.sb.set)            
            self.lb.pack(side=LEFT, fill=BOTH)
            self.sb.config(command=self.lb.yview)
            
            
if __name__=='__main__':
    app = GUI()
    
    app.mainloop()







# Porter Stemmer with nltk for 32-bit python 
'''from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps = PorterStemmer()
pre_error = ['s', 'b', 'c', 'as', ' ']
end_error = ['er', 'ing', 'ly', 'ed', 'ily']'''

#database
data={
'major':['math','art','physics','computer science'],
'birthday':['october 10th 2000','today,june 17th 1997'],
'food':['pudding','cake','spaghetti','Kung pao chicken'],
'drink':['blood','7 up','Pepsi','orange juice'],
'sport':['soccer','badminton','basketball','archery'],
'color':['red','black','green','yellow'],
'weather':['sunny','snowy','rainy'],
'breakfast':['burger','cereal','corn','bread'],
'homework':['I haven''t finished it yet','Yesterday','uhhh, let''s change a topic'],
'sleep':['at 12:00 pm','at 3:00 am','I have sleep disorder yesterday...'],
'gym':['last month','yesterday','a week ago, I guess....'],
'coffee':['yesterday'],
'class':['no, I am a good student','uhh, maybe.''I refuse to answer this question.'],
'semester':['five courses','4 courses'],
'homework':['about 10 hours','about 2 hours'],
'games':['a whole day','5 hours'] ,
'job':['no, I have no time to work.''yes, I have.'],
'father':['his name is ChatbotA'],
'mother':['Her name is Sara'],
'cousin':['Her name is Sam'],
'sister':['Her name is Amy'],
'math':['steve'],
'art':['Ronny'],
'drama':['Abie'],
'CS':['Aron'],
'Social':['Aaron'],
'History':['summer'],
'friend':['I do not have friend except you','her name is annie, another chatbot'],
'hometomn':['kelowna','Mars'],
'summer':['vancouver','ontario'],
'game':['LOL'],
'Car':['Audi']
}
#database initialization 
dataKey=list(data.keys())
#go to the CoreNlp folder by using: cd directory and type java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
'''nlp = StanfordCoreNLP('http://localhost', port=9000)'''


import random

for x in data:
    print(x)
print("These are the keywords in my dataset,please have a look\n")

answer=input("Hi, I am chatBot\n")
while answer!="HI" and answer!="hi":
    print("Sorry, I can not answer your question, please say \'HI\' or \'hi\' first")
    answer=input("Hi, I am chatBot\n")

isActive =  1

#ask user input       
name=input("What is your name\n")
print("Nice to meet you "+name+"!\n")
print("Ask me some questions "+name)
#print("if you do not know what to ask, type help")
while isActive != 0:
    answer = input(" (if you do not know what to ask, type \'help\'\nor if you don\'t want to talk no more, type \'bye\'\n)")

    #stem inputs
#commented for nltk only running on 32-bit python 
    '''ps.stem(answer) '''

#backup response for invalid inputs
    backup_answers = ['Sorry, I can not understand the question',
                                      'Oh please, say something that I can understand (the words that in my database)',
                                      'Uh...please say something else, I can\'t understand it',
                                      'Maybe you should type \'help\' for help or ask me something else',
                                      'Don\'t want to say this, but I really don\'t understand it']
    #POS tagging
    'pos = nlp.pos_tag(answer)'
    #Named Entities'''
    'nameE = nlp.ner(answer)'
    #Tokenize'''
    'nlp.word_tokenize(answer)'

    '''for key in pos:
        if key != 'NNP':
            pos.remove(key)
    for key in nameE:
        if key != 'Organization':
            pos.remove(key)'''
    
    if answer=="help":
        print(data.keys())
        print('Here is a sample question: what\'s your major?\n')
    elif answer=="bye":
        isActive = 0
        print("chatBot terminated")
        break
    
    if answer in dataKey :
        index_num = random.randint(0,len(data[answer])-1)
        print(data[answer][index_num])
    else: 
        print(backup_answers[random.randint(0,len(backup_answers)-1)])
    
    print("Now, what you want to ask?(remember to type \'help\' for help, and \'bye\' to quit)\n")

#play=True

#while play==True:
   
#play=input("Do you still want to play ?")   
# question=input("What you want to ask")

