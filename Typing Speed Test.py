# Importing tkinter and timeit libraries
from tkinter import *
import random
from tkinter import messagebox
from timeit import default_timer as timer 

# Creating  first Window
window = Tk()

# Initialising needed variables
count = 0
score = 0
miss = 0
l= []
l1 =[]
count = 0
correct_count =0
timeleft = 60
sliderWords = ''

# creating Label for the title in first window
lbl = Label(window,text = 'TYPING SPEED TEST',font=('arial',25,'italic bold'),bg = 'black',fg='white')
lbl.place(x=200,y=10)
        
# Creating Beginner Function
def beginner():
    root = Tk()             # creating second window for beginner level
    t0 = timer()            # Timer will be started 
    root.geometry('800x600+400+100')     # setting the geometry of the window, height=800,width=600,x-axis=400,y axis= 100
    root.configure(bg = 'black')          # configuring background of the window
    
    root.title('Typing Speed Test Game')    # Giving the title 

    root.iconbitmap("image.ico")            # Changing icon
 

    
    def labelSlider():            # Creating function for sliding the title
        global count,sliderWords
        text = 'Welcome to Typing Speed Game'       # initialising text variable with project name 
        if(count>=len(text)):                # checking condition 
            
            count = 0
            sliderWords = ''
        sliderWords += text[count]          # if the condition is false,then add text[count] in sliderwords
        count += 1                          # incrementing count
        fontLabel.configure(text = sliderWords)       # configuring fontLabel with sliderwords
        fontLabel.after(100,labelSlider)         # after every 100 ms, it will call the labelSlider function.


   
   
    def get_sentence():                  # creating function to get words using file handling
        f = open("beginner.txt","r")
        lines = f.read().split("\n")     # contains words in list wherever finds next line
        line = random.choice(lines)       # randomly picking word from list
        return line
    

   
    
    def startGame(event):             # Creating function using event handling
        global score,miss,timeleft,l,count
        if (timeleft==60):
             time()              # when timeleft is 60,it will call the time function
        gamePlayDetailLabel.configure(text = '')        # once the game has started the hint that "enter and hit" will vanish
        if (wordEntry.get()==wordLabel['text']):      # condition to check whether user has given the correct inout or not
            
            score += 1            # incrementing score
            l.append(wordEntry.get())         # append the input in list l
            l1.append(wordEntry.get())        # append the input in list l1
            scoreLabelCount.configure(text = score)     # configuring the label with score
           

        else:             # when condition is false
            
            
            miss += 1           # incrementing the variable miss
            l.append(wordEntry.get())         # appending the input in list l
        wordLabel.configure(text=get_sentence())       # configuring the Wordlabel with function get_sentence()
        wordEntry.delete(0,END)            # clear the entry box after hitting Enter

    def time():           # creating time function
         
         
         global timeleft,score,miss,count,correct_count
         if timeleft>=11:
             
             pass
         else:
             
             timeLabelCount.configure(fg = 'red')    # when timeleft<11 , fg of timelabelcount will be changed to red
         if(timeleft>0):
             
             timeleft -= 1       # decrementing timeleft 
             timeLabelCount.configure(text = timeleft)   # to configure the count with left time
             timeLabelCount.after(1000,time)    # after every 1000 mili sec..it will call time
         else:
             t1 = timer()        # timer will be stopped when timeleft becomes 0
             for i in l:         # traversing the list l
                 count += len(i)   # adding the length of each word in list
             print(l)               # list l contains all input
             print(count)
             print(l1)            # list l1 contains only correct input
             for i in l1:          # traversing the list l1
                 correct_count += len(i)         
             print(correct_count)        # printing the total length of correct input  by user 
             t = str(round(t1-t0))        # total time taken by user
                
                # configuring the label with Total Score , WPM and Accuracy
             gamePlayDetailLabel.configure(text = 'Total Score = {} | WPM={} | Accuracy={}'.format(score-miss,int((count*60)/int(5*(t1-t0))),int((correct_count*100)/count)))
             rr = messagebox.askretrycancel('Notification','Hit Retry to Play Again')    # asking for Retry or Cancel
             if rr == True:          # if user has selected Retry ,then set all the variables as earlier
                 
                 score = 0
                 timeleft = 60
                 miss = 0
                 timeLabelCount.configure(text = timeleft)
                 wordLabel.configure(text = get_sentence())
                 scoreLabelCount.configure(text = score)

  
# Creating Different Labels
         
    fontLabel = Label(root,text = 'Welcome to Typing Speed Game',font=('arial',25,'italic bold'),bg ='black',fg = 'grey',width = 40)
    fontLabel.place(x = 10,y = 10)
    labelSlider()         # calling labelSlider function
    

    
    wordLabel = Label(root, text = get_sentence(),font=('arial',20,'italic bold'),bg = 'black',width =50,fg='dark green')
    wordLabel.place(x = 10,y = 250)

    scoreLabel = Label(root,text = 'Your Score : ',font=('arial',25,'italic bold'),bg = 'black',fg='blue')
    scoreLabel.place(x =10,y = 100)

    scoreLabelCount = Label(root,text = score,font=('arial',25,'italic bold'),bg ='black',fg = 'grey')
    scoreLabelCount.place(x = 80,y =180)

    timerLabel = Label(root,text = 'Time Left :',font=('arial',25,'italic bold'),bg ='black',fg ='blue')
    timerLabel.place(x = 600, y = 100)

    timeLabelCount = Label(root,text = timeleft,font=('arial',25,'italic bold'),bg ='black',fg = 'grey')
    timeLabelCount.place(x = 680,y= 180)

    gamePlayDetailLabel = Label(root, text = 'Type Word and Hit Enter',font = ('arial',20,'italic'),bg = 'black', fg = 'dark grey')
    gamePlayDetailLabel.place(x = 220,y = 400)
     
        # Creating Entry Box

    wordEntry = Entry(root,font=('arial',20,'italic bold'),bd = 10,width = 15,justify='center') # justify enable the text to be input in center
    wordEntry.place(x = 300,y = 300)
    wordEntry.focus_set()  # by this no need to enter into the entry box and then write...enable the input wothout clicking into the entry box


    root.bind('<Return>',startGame) # binding enter with the function StartGame .. we will be able to get the words typed after hitting enter.part of event handling
    root.mainloop()

######### FOR INTERMEDIATE LEVEL ###########

def intermediate():
    root = Tk()
    t0 = timer()
    root.geometry('800x600+400+100')
    root.configure(bg = 'black')
    
    root.title('Typing Speed Test Game')

    root.iconbitmap("image.ico")
 

    
    def labelSlider():
        global count,sliderWords
        text = 'Welcome to Typing Speed Game'
        if(count>=len(text)):
            
            count = 0
            sliderWords = ''
        sliderWords += text[count]
        count += 1
        fontLabel.configure(text = sliderWords)
        fontLabel.after(100,labelSlider)


   
   
    def get_sentence():
        f = open("intermediate.txt","r")
        lines = f.read().split("\n")
        line = random.choice(lines)
        return line
    

   
    
    def startGame(event):
        global score,miss,timeleft,l,count
        if (timeleft==60):
             time()
        gamePlayDetailLabel.configure(text = '')
        if (wordEntry.get()==wordLabel['text']):
            
            score += 1
            l.append(wordEntry.get())
            l1.append(wordEntry.get())
            scoreLabelCount.configure(text = score)
           

        else:
            
            
            miss += 1
            l.append(wordEntry.get())
        wordLabel.configure(text=get_sentence())
        wordEntry.delete(0,END)

    def time():
         
         
         global timeleft,score,miss,count,correct_count
         if timeleft>=11:
             
             pass
         else:
             
             timeLabelCount.configure(fg = 'red')
         if(timeleft>0):
             
             timeleft -= 1
             timeLabelCount.configure(text = timeleft)   # to configure the count woth left time
             timeLabelCount.after(1000,time)    # after every 1000 micro sec..it will call time
         else:
             t1 = timer()
             for i in l:
                 count += len(i)
             print(l)
             print(count)
             print(l1)
             for i in l1:
                 correct_count += len(i)
             print(correct_count)    
             t = str(round(t1-t0))   
             gamePlayDetailLabel.configure(text = 'Total Score = {} | WPM={} | Accuracy={}'.format(score-miss,int((count*60)/int(5*(t1-t0))),int((correct_count*100)/count)))
             rr = messagebox.askretrycancel('Notification','Hit Retry to Play Again')
             if rr == True:
                 
                 score = 0
                 timeleft = 60
                 miss = 0
                 timeLabelCount.configure(text = timeleft)
                 wordLabel.configure(text = get_sentence())
                 scoreLabelCount.configure(text = score)

  

         
    fontLabel = Label(root,text = 'Welcome to Typing Speed Game',font=('arial',25,'italic bold'),bg ='black',fg = 'grey',width = 40)
    fontLabel.place(x = 10,y = 10)
    labelSlider()
    

    
    wordLabel = Label(root, text = get_sentence(),font=('arial',20,'italic bold'),bg = 'black',width =50,fg='dark green')
    wordLabel.place(x = 10,y = 250)

    scoreLabel = Label(root,text = 'Your Score : ',font=('arial',25,'italic bold'),bg = 'black',fg='blue')
    scoreLabel.place(x =10,y = 100)

    scoreLabelCount = Label(root,text = score,font=('arial',25,'italic bold'),bg ='black',fg = 'grey')
    scoreLabelCount.place(x = 80,y =180)

    timerLabel = Label(root,text = 'Time Left :',font=('arial',25,'italic bold'),bg ='black',fg ='blue')
    timerLabel.place(x = 600, y = 100)

    timeLabelCount = Label(root,text = timeleft,font=('arial',25,'italic bold'),bg ='black',fg = 'grey')
    timeLabelCount.place(x = 680,y= 180)

    gamePlayDetailLabel = Label(root, text = 'Type Word and Hit Enter',font = ('arial',20,'italic'),bg = 'black', fg = 'dark grey')
    gamePlayDetailLabel.place(x = 220,y = 400)

    wordEntry = Entry(root,font=('arial',20,'italic bold'),bd = 10,width = 15,justify='center') # justify enable the text to be input in center
    wordEntry.place(x = 300,y = 300)
    wordEntry.focus_set()  # by this no need to enter into the entry box and then write...enable the input wothout clicking


    root.bind('<Return>',startGame) # binding enter with the function call .. we will be able to get the words typed after hitting enter.part of event handling
    root.mainloop() 


################# FOR ADVANCED LEVEL###########


def advanced():
    root = Tk()
    t0 = timer()
    root.geometry('800x600+400+100')
    root.configure(bg = 'black')
    
    root.title('Typing Speed Test Game')

    root.iconbitmap("image.ico")
 

    
    def labelSlider():
        global count,sliderWords
        text = 'Welcome to Typing Speed Game'
        if(count>=len(text)):
            
            count = 0
            sliderWords = ''
        sliderWords += text[count]
        count += 1
        fontLabel.configure(text = sliderWords)
        fontLabel.after(100,labelSlider)


   
   
    def get_sentence():
        f = open("advanced.txt","r")
        lines = f.read().split("\n")
        line = random.choice(lines)
        return line
    

   
    
    def startGame(event):
        global score,miss,timeleft,l,count
        if (timeleft==60):
             time()
        gamePlayDetailLabel.configure(text = '')
        if (wordEntry.get()==wordLabel['text']):
            
            score += 1
            l.append(wordEntry.get())
            l1.append(wordEntry.get())
            scoreLabelCount.configure(text = score)
           

        else:
            
            
            miss += 1
            l.append(wordEntry.get())
        wordLabel.configure(text=get_sentence())
        wordEntry.delete(0,END)

    def time():
         
         
         global timeleft,score,miss,count,correct_count
         if timeleft>=11:
             
             pass
         else:
             
             timeLabelCount.configure(fg = 'red')
         if(timeleft>0):
             
             timeleft -= 1
             timeLabelCount.configure(text = timeleft)   # to configure the count woth left time
             timeLabelCount.after(1000,time)    # after every 1000 micro sec..it will call time
         else:
             t1 = timer()
             for i in l:
                 count += len(i)
             print(l)
             print(count)
             print(l1)
             for i in l1:
                 correct_count += len(i)
             print(correct_count)    
             t = str(round(t1-t0))   
             gamePlayDetailLabel.configure(text = 'Total Score = {} | WPM={} | Accuracy={}'.format(score-miss,int((count*60)/int(5*(t1-t0))),int((correct_count*100)/count)))
             rr = messagebox.askretrycancel('Notification','Hit Retry to Play Again')
             if rr == True:
                 
                 score = 0
                 timeleft = 60
                 miss = 0
                 timeLabelCount.configure(text = timeleft)
                 wordLabel.configure(text = get_sentence())
                 scoreLabelCount.configure(text = score)

  

         
    fontLabel = Label(root,text = 'Welcome to Typing Speed Game',font=('arial',25,'italic bold'),bg ='black',fg = 'grey',width = 40)
    fontLabel.place(x = 10,y = 10)
    labelSlider()
    

    
    wordLabel = Label(root, text = get_sentence(),font=('arial',20,'italic bold'),bg = 'black',width =50,fg='dark green')
    wordLabel.place(x = 10,y = 250)

    scoreLabel = Label(root,text = 'Your Score : ',font=('arial',25,'italic bold'),bg = 'black',fg='blue')
    scoreLabel.place(x =10,y = 100)

    scoreLabelCount = Label(root,text = score,font=('arial',25,'italic bold'),bg ='black',fg = 'grey')
    scoreLabelCount.place(x = 80,y =180)

    timerLabel = Label(root,text = 'Time Left :',font=('arial',25,'italic bold'),bg ='black',fg ='blue')
    timerLabel.place(x = 600, y = 100)

    timeLabelCount = Label(root,text = timeleft,font=('arial',25,'italic bold'),bg ='black',fg = 'grey')
    timeLabelCount.place(x = 680,y= 180)

    gamePlayDetailLabel = Label(root, text = 'Type Word and Hit Enter',font = ('arial',20,'italic'),bg = 'black', fg = 'dark grey')
    gamePlayDetailLabel.place(x = 220,y = 400)

    wordEntry = Entry(root,font=('arial',20,'italic bold'),bd = 10,width = 15,justify='center') # justify enable the text to be input in center
    wordEntry.place(x = 300,y = 300)
    wordEntry.focus_set()  # by this no need to enter into the entry box and then write...enable the input wothout clicking


    root.bind('<Return>',startGame) # binding enter with the function call .. we will be able to get the words typed after hitting enter.part of event handling
    root.mainloop() 
                 
    

# Creating label     
             
lbl=Label(window,text="Select Your Level",font=('arial',25,'italic bold'),bg ='black',fg = 'brown')
lbl.place(x=250,y=100)

# Creating 3 different buttons for 3 level
btn=Button(window,text="Beginner",command=beginner,bg='orange red',width=10,height=2,font=('arial',10,'italic bold'))
btn.place(x=350,y=150)
btn=Button(window,text="Intermediate",command = intermediate, bg='orange red',width=10,height=2,font=('arial',10,'italic bold'))
btn.place(x=350,y=200)
btn=Button(window,text="Advanced",bg='orange red',command = advanced,width=10,height=2,font=('arial',10,'italic bold'))
btn.place(x=350,y=250)

# setting iMage into Label for first Window
filename = PhotoImage(file = "image2.png")
imglabel = Label(window,image=filename,width=770)
imglabel.place(x=10,y= 300)



window.geometry('800x600+400+100')     # setting geometry
window.configure(bg ='black')           # changing bg
window.title('Typing Speed Test Game')  # setting title
window.iconbitmap('image.ico')      # changing icon

window.mainloop()         

        

     
        
        
    
        



    
    
