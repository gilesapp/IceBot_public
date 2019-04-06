# IceBot_public
This IceBot is developed based on the A2. // SNA:Meng Tian (SID:31120983)
--------------------------------------------------------------------------
DESCRIPTION:
---------------
//This a simple chatbot project that is built upon and implemented in python that allows users to have a stimulus conversation by geting prompt from the chatbot and ask questions to it through a premade data base.(an updated version of A2)  

HOW TO COMPILE & RUN:
----------------
//1.Download the IceBot_public.py and open it on an IDE (visual studio 2019 is what I used).
//  2.Download the Stanford toolkit OpenNLP and run (pip install stanfordcorenlp) as this chatbot uses it.
//  3.Run IceBot_public.py (GUI is still on development, it is recommened to use the console)


CLASS:
--------------------
//'GUI': Create and initialize basic user interface with title, conversation window, input entry, and a chat history viewer
        'chatBot': Store dataset, prompt questions and give responses, users’ inputs validity check, help.     

HELP:
-------------------
// typing “help” if you need help


Features added 
--------------------------------------
//A GUI: this interface helps the overall conversation looks better and more user-friendly
//An extra topic: two new keys(games, math) are added into the database which makes the topic more diverse e.g "What's your favorite game?" "LOL" 
//A backup answer base: now the chatbot can give 5 different reasonable responses when the user enters something outside the topics e.g"Sorry, I can not understand the question.../Uh...please say something else..."
//A Porter Stemmer spelling handler: By implementing the stemmer(on a 32-bit python) with 'pre-' '-end' two sets, the misspelling now can be corrected as a right spelling e.g"what's your majorer" => "what's your major"
//POS-tagging(Stanford toolkit, OpenNLP)
//Named entity recognition(Stanford toolkit, OpenNLP)
//Tokenize(Stanford toolkit, OpenNLP) These three Stanfor toolkit allows a faster analysis of the user's input, e.g pos-tagging:"What's your major" could be analyised "what's,IN, your,IN, major,NNP", the only thing we need is NNP, thus, we can match the NNP directly with the database 
