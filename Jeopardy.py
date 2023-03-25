from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import Menu

global play_again
play_again = True

while play_again == True:
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0

    def quitapp():
        global play_again
        play_again = False
        start.destroy()
        
    def playgame():
        num_of_teams = teamselect.get()
        start.destroy()
        
        def incorrect():
            messagebox.showinfo('', 'Answer is Wrong!')    

        def team1score():
            global counter1
            counter1 += 100
            t.configure(text = counter1)

        def team2score():
            global counter2
            counter2 += 100
            tt.configure(text = counter2)
            
        def team3score():
            global counter3
            counter3 += 100
            ttt.configure(text = counter3)
            
        def team4score():
            global counter4
            counter4 += 100
            tttt.configure(text = counter4)
            
        def team5score():
            global counter5
            counter5 += 100
            ttttt.configure(text = counter5)
            
        def history100():
            def close():
                question.destroy()
            def correcthist100():
                ans = Ans100.get()
                if ans == "Franz Ferdinand":
                    messagebox.showinfo('','Answer is Correct! Add 100 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('History 100')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans100 = Entry(question, width = 10)
            Ans100.grid(column = 0, row = 1, pady = 10)
            EnterHist100 = Button(question, text = 'Enter', command = correcthist100)
            EnterHist100.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 3, pady = 15)
            hist100 = Button(window, text = '100', style = "red.TButton")
            hist100.grid(column = 0, row = 3, pady = 7)
            
        def history200():
            def close():
                question.destroy()
            def correcthist200():
                ans = Ans200.get()
                if ans == "Neil Armstrong":
                    messagebox.showinfo('','Answer is Correct! Add 200 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('History 200')
            Q = Label(question, text='Who was the first man to walk on the moon?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans200 = Entry(question, width = 10)
            Ans200.grid(column = 0, row = 1, pady = 10)
            EnterHist200 = Button(question, text = 'Enter', command = correcthist200)
            EnterHist200.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 3, pady = 15)
            hist200 = Button(window, text = '200', style = "red.TButton")
            hist200.grid(column = 0, row = 4, pady = 7)
            
        def history300():
            def close():
                question.destroy()
            def correcthist300():
                ans = Ans500.get()
                if ans == "1963":
                    messagebox.showinfo('','Answer is Correct! Add 300 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('History 300')
            Q = Label(question, text='In which year was John F. Kennedy assassinated?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans300 = Entry(question, width = 10)
            Ans300.grid(column = 0, row = 1, pady = 10)
            EnterHist300 = Button(question, text = 'Enter', command = correcthist300)
            EnterHist300.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 3, pady = 15)
            hist300 = Button(window, text = '300', style = "red.TButton")
            hist300.grid(column = 0, row = 5, pady = 7)

        def history400():
            def close():
                question.destroy()
            def correcthist400():
                ans = Ans400.get()
                if ans == "South Sudan":
                    messagebox.showinfo('','Answer is Correct! Add 400 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('History 400')
            Q = Label(question, text='Which country is the newest country to exist?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans400 = Entry(question, width = 10)
            Ans400.grid(column = 0, row = 1, pady = 10)
            EnterHist400 = Button(question, text = 'Enter', command = correcthist400)
            EnterHist400.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 3, pady = 15)
            hist400 = Button(window, text = '400', style = "red.TButton")
            hist400.grid(column = 0, row = 6, pady = 7)
            
        def history500():
            def close():
                question.destroy()
            def correcthist500():
                ans = Ans500.get()
                if ans == "Appomattox":
                    messagebox.showinfo('','Answer is Correct! Add 500 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('History 500')
            Q = Label(question, text='In 1865, Confederate General Robert E. Lee surrendered ' +
            'to Union General Ulysses S. Grant, effectively ending the American Civil War. Where did this take place??')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans500 = Entry(question, width = 10)
            Ans500.grid(column = 0, row = 1, pady = 10)
            EnterHist500 = Button(question, text = 'Enter', command = correcthist500)
            EnterHist500.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 3, pady = 15)
            hist500 = Button(window, text = '500', style = "red.TButton")
            hist500.grid(column = 0, row = 7, pady = 7)

        def sports100():
            def close():
                question.destroy()
            def correctsport100():
                ans = Ans100.get()
                if ans == "Steph Curry":
                    messagebox.showinfo('','Answer is Correct! Add 100 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Sports 100')
            Q = Label(question, text='Which basketball player recently surprassed the record for most 3PM?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans100 = Entry(question, width = 10)
            Ans100.grid(column = 0, row = 1, pady = 10)
            EnterSport100 = Button(question, text = 'Enter', command = correctsport100)
            EnterSport100.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            sport100 = Button(window, text = '100', style = "red.TButton")
            sport100.grid(column = 1, row = 3, pady = 7)
            
        def sports200():
            def close():
                question.destroy()
            def correctsport200():
                ans = Ans200.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 200 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Sports 200')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans200 = Entry(question, width = 10)
            Ans200.grid(column = 0, row = 1, pady = 10)
            EnterSport200 = Button(question, text = 'Enter', command = correctsport200)
            EnterSport200.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            sport200 = Button(window, text = '200', style = "red.TButton")
            sport200.grid(column = 1, row = 4, pady = 7)
            
        def sports300():
            def close():
                question.destroy()
            def correctsport300():
                ans = Ans300.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 300 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Sports 300')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans300 = Entry(question, width = 10)
            Ans300.grid(column = 0, row = 1, pady = 10)
            EnterSport300 = Button(question, text = 'Enter', command = correctsport300)
            EnterSport300.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            sport300 = Button(window, text = '300', style = "red.TButton")
            sport300.grid(column = 1, row = 5, pady = 7)

        def sports400():
            def close():
                question.destroy()
            def correctsport400():
                ans = Ans400.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 400 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Sports 400')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans400 = Entry(question, width = 10)
            Ans400.grid(column = 0, row = 1, pady = 10)
            EnterSport400 = Button(question, text = 'Enter', command = correctsport400)
            EnterSport400.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            sport400 = Button(window, text = '400', style = "red.TButton")
            sport400.grid(column = 1, row = 6, pady = 7)
            
        def sports500():
            def close():
                question.destroy()
            def correctsport500():
                ans = Ans500.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 500 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Sports 500')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans500 = Entry(question, width = 10)
            Ans500.grid(column = 0, row = 1, pady = 10)
            EnterSport500 = Button(question, text = 'Enter', command = correctsport500)
            EnterSport500.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            sport500 = Button(window, text = '500', style = "red.TButton")
            sport500.grid(column = 1, row = 7, pady = 7)
        
        def geography100():
            def close():
                question.destroy()
            def correctgeo100():
                ans = Ans100.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 100 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Geography 100')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans100 = Entry(question, width = 10)
            Ans100.grid(column = 0, row = 1, pady = 10)
            EnterGeo100 = Button(question, text = 'Enter', command = correctgeo100)
            EnterGeo100.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            geo100 = Button(window, text = '100', style = "red.TButton")
            geo100.grid(column = 2, row = 3, pady = 7)
            
        def geography200():
            def close():
                question.destroy()
            def correctgeo200():
                ans = Ans200.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 200 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Geography 200')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans200 = Entry(question, width = 10)
            Ans200.grid(column = 0, row = 1, pady = 10)
            EnterGeo200 = Button(question, text = 'Enter', command = correctgeo200)
            EnterGeo200.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            geo200 = Button(window, text = '200', style = "red.TButton")
            geo200.grid(column = 2, row = 4, pady = 7)
            
        def geography300():
            def close():
                question.destroy()
            def correctgeo300():
                ans = Ans300.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 300 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Geography 300')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans300 = Entry(question, width = 10)
            Ans300.grid(column = 0, row = 1, pady = 10)
            EnterGeo300 = Button(question, text = 'Enter', command = correctgeo300)
            EnterGeo300.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            geo300 = Button(window, text = '300', style = "red.TButton")
            geo300.grid(column = 2, row = 5, pady = 7)

        def geography400():
            def close():
                question.destroy()
            def correctgeo400():
                ans = Ans400.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 400 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Geography 400')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans400 = Entry(question, width = 10)
            Ans400.grid(column = 0, row = 1, pady = 10)
            EnterGeo400 = Button(question, text = 'Enter', command = correctgeo400)
            EnterGeo400.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            geo400 = Button(window, text = '400', style = "red.TButton")
            geo400.grid(column = 2, row = 6, pady = 7)
        
        def geography500():
            def close():
                question.destroy()
            def correctgeo500():
                ans = Ans500.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 500 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Sports 500')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans500 = Entry(question, width = 10)
            Ans500.grid(column = 0, row = 1, pady = 10)
            EnterGeo500 = Button(question, text = 'Enter', command = correctgeo500)
            EnterGeo500.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            geo500 = Button(window, text = '500', style = "red.TButton")
            geo500.grid(column = 2, row = 7, pady = 7)
        
        def movie100():
            def close():
                question.destroy()
            def correctmovie100():
                ans = Ans100.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 100 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Movie 100')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans100 = Entry(question, width = 10)
            Ans100.grid(column = 0, row = 1, pady = 10)
            EnterMovie100 = Button(question, text = 'Enter', command = correctmovie100)
            EnterMovie100.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            mov100 = Button(window, text = '100', style = "red.TButton")
            mov100.grid(column = 3, row = 3, pady = 7)
            
        def movie200():
            def close():
                question.destroy()
            def correctmovie200():
                ans = Ans200.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 200 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Movie 200')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans200 = Entry(question, width = 10)
            Ans200.grid(column = 0, row = 1, pady = 10)
            EnterMovie200 = Button(question, text = 'Enter', command = correctmovie200)
            EnterMovie200.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            mov200 = Button(window, text = '200', style = "red.TButton")
            mov200.grid(column = 3, row = 4, pady = 7)
            
        def movie300():
            def close():
                question.destroy()
            def correctmovie300():
                ans = Ans300.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 300 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Movie 300')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans300 = Entry(question, width = 10)
            Ans300.grid(column = 0, row = 1, pady = 10)
            EnterMovie300 = Button(question, text = 'Enter', command = correctmovie300)
            EnterMovie300.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            mov300 = Button(window, text = '300', style = "red.TButton")
            mov300.grid(column = 3, row = 5, pady = 7)

        def movie400():
            def close():
                question.destroy()
            def correctmovie400():
                ans = Ans400.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 400 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Movie 400')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans400 = Entry(question, width = 10)
            Ans400.grid(column = 0, row = 1, pady = 10)
            EnterMovie400 = Button(question, text = 'Enter', command = correctmovie400)
            EnterMovie400.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            mov400 = Button(window, text = '400', style = "red.TButton")
            mov400.grid(column = 3, row = 6, pady = 7)
            
        def movie500():
            def close():
                question.destroy()
            def correctmovie500():
                ans = Ans500.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 500 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Movie 500')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans500 = Entry(question, width = 10)
            Ans500.grid(column = 0, row = 1, pady = 10)
            EnterMovie500 = Button(question, text = 'Enter', command = correctmovie500)
            EnterMovie500.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            mov500 = Button(window, text = '500', style = "red.TButton")
            mov500.grid(column = 3, row = 7, pady = 7)
        
        def sci100():
            def close():
                question.destroy()
            def correctsci100():
                ans = Ans100.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 100 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Science 100')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans100 = Entry(question, width = 10)
            Ans100.grid(column = 0, row = 1, pady = 10)
            EnterScience100 = Button(question, text = 'Enter', command = correctsci100)
            EnterScience100.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            sci100 = Button(window, text = '100', style = "red.TButton")
            sci100.grid(column = 4, row = 3, pady = 7)
            
        def sci200():
            def close():
                question.destroy()
            def correctsci200():
                ans = Ans200.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 200 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Science 200')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans200 = Entry(question, width = 10)
            Ans200.grid(column = 0, row = 1, pady = 10)
            EnterScience200 = Button(question, text = 'Enter', command = correctsci200)
            EnterScience200.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            sci200 = Button(window, text = '200', style = "red.TButton")
            sci200.grid(column = 4, row = 4, pady = 7)
            
        def sci300():
            def close():
                question.destroy()
            def correctsci300():
                ans = Ans300.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 300 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Science 300')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans300 = Entry(question, width = 10)
            Ans300.grid(column = 0, row = 1, pady = 10)
            EnterScience300 = Button(question, text = 'Enter', command = correctsci300)
            EnterScience300.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            sci300 = Button(window, text = '300', style = "red.TButton")
            sci300.grid(column = 4, row = 5, pady = 7)

        def sci400():
            def close():
                question.destroy()
            def correctsci400():
                ans = Ans400.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 400 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Science 400')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans400 = Entry(question, width = 10)
            Ans400.grid(column = 0, row = 1, pady = 10)
            EnterScience400 = Button(question, text = 'Enter', command = correctsci400)
            EnterScience400.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            sci400 = Button(window, text = '400', style = "red.TButton")
            sci400.grid(column = 4, row = 6, pady = 7)
            
        def sci500():
            def close():
                question.destroy()
            def correctsci500():
                ans = Ans500.get()
                if ans == "yo":
                    messagebox.showinfo('','Answer is Correct! Add 500 to your team score.')
                else:
                    messagebox.showinfo('', 'Answer is Wrong!')
            question = Toplevel()
            question.geometry("300x300")
            question.title('Science 500')
            Q = Label(question, text='Who was killed that inititated World War 1?')
            Q.grid(column = 0, row = 0, padx = 15, pady = 15, sticky=N+S+W+E)
            Ans500 = Entry(question, width = 10)
            Ans500.grid(column = 0, row = 1, pady = 10)
            EnterScience500 = Button(question, text = 'Enter', command = correctsci500)
            EnterScience500.grid(column = 0, row = 2, pady = 5)
            Home = Button(question, text = 'Back to Home', command = close)
            Home.grid(column = 0, row = 6)
            sci500 = Button(window, text = '500', style = "red.TButton")
            sci500.grid(column = 4, row = 7, pady = 7)
            
        def endgame():
            def playagain():
                global play_again
                play_again = True
                end.destroy()
                
            def exitgame():
                global play_again
                play_again = False
                end.destroy()
                
            high = 0
            teamwon = ""
            window.destroy()
            end = Tk()
            end.title("Game Finished")
            end.geometry('500x400')
            end.configure(background = "cyan")
            
            style = ttk.Style() 
            style.theme_use("clam")
            style.configure("end.TLabel", background = "blue", foreground = "white")
            style.configure("start.TButton", background = "green", foreground = "white")
            style.configure("quit.TButton", background = "red", foreground = "white")
            
            for i in (counter1, counter2, counter3, counter4, counter5):
                if i > high:
                    high = i
            
            if high == counter1:
                teamwon = "Team 1"
            elif high == counter2:
                teamwon = "Team 2"
            elif high == counter3:
                teamwon = "Team 3"
            elif high == counter4:
                teamwon = "Team 4"
            elif high == counter5:
                teamwon = "Team 5"
                
            conclusion = Label(end, text = "Thanks For Playing!", font = ("Courier", 40), style = "end.TLabel")
            conclusion.grid(column = 0, row = 0, pady = 10, padx = 20)
            
            result = Label(end, text = teamwon + " won Python Jeopardy with a score of " + str(high), style = "end.TLabel", font = ("Courier", 15))
            result.grid(column = 0, row = 2, pady = 20, padx = 20)
            
            PlayAgain = Button(end, text = "Play Again", command = playagain, style = "start.TButton")
            PlayAgain.grid(column = 0, row = 3, pady = 20, padx = 20)
            
            ExitGame = Button(end, text = "Exit Game", command = exitgame, style = "quit.TButton")
            ExitGame.grid(column = 0, row = 4, padx = 20)
            
        window = Tk()
        window.title("Yo")
        window.geometry('900x800')
        window.configure(background = "cyan")
        
        style = ttk.Style() 
        style.theme_use("clam")
        style.configure("red.TButton", background = "red")
        style.configure("q.TButton", background = "blue", foreground = "white")
        style.configure("scorelabel.TLabel", background = "black", foreground = "white", font = ("Arial Bold", 16))
        style.configure("cyan.TLabel", background = "cyan")
        
        header = PhotoImage(file = "jeopardygame.png")
        jeoheader = Label(window, image = header)
        jeoheader.grid(column = 2, row = 0, pady = 15)
        History_Header = Label(window, text = 'History', font = ("Calibri", 25), style = "scorelabel.TLabel")
        History_Header.grid(column = 0, row = 1, padx = 20)
        Sports_Header = Label(window, text = 'Sports', font = ("Calibri", 25), style = "scorelabel.TLabel")
        Sports_Header.grid(column = 1, row = 1, padx = 70)
        Geo_Header = Label(window, text = 'Geography', font = ("Calibri", 25), style = "scorelabel.TLabel")
        Geo_Header.grid(column = 2, row = 1)
        Movies_Header = Label(window, text = 'Movies', font = ("Calibri", 25), style = "scorelabel.TLabel")
        Movies_Header.grid(column = 3, row = 1, padx = 70)
        Science_Header = Label(window, text = 'Science', font = ("Calibri", 25), style = "scorelabel.TLabel")
        Science_Header.grid(column = 4, row = 1, padx = 20)

        blank1 = Label(window, style = "cyan.TLabel")
        blank1.grid(column = 0, row = 2)
        blank2 = Label(window, style = "cyan.TLabel")
        blank2.grid(column = 1, row = 2)

        hist100 = Button(window, text='100', style = "q.TButton", command = history100)
        hist100.grid(column = 0, row = 3, pady = 7)
        hist200 = Button(window, text='200', style = "q.TButton", command = history200)
        hist200.grid(column = 0, row = 4, pady = 7)
        hist300 = Button(window, text='300', style = "q.TButton", command = history300)
        hist300.grid(column = 0, row = 5, pady = 7)
        hist400 = Button(window, text='400', style = "q.TButton", command = history400)
        hist400.grid(column = 0, row = 6, pady = 7)
        hist500 = Button(window, text='500', style = "q.TButton", command = history500)
        hist500.grid(column = 0, row = 7, pady = 7)

        sport100 = Button(window, text='100', style = "q.TButton", command = sports100)
        sport100.grid(column = 1, row = 3, pady = 7)
        sport200 = Button(window, text='200', style = "q.TButton", command = sports200)
        sport200.grid(column = 1, row = 4, pady = 7)
        sport300 = Button(window, text='300', style = "q.TButton", command = sports300)
        sport300.grid(column = 1, row = 5, pady = 7)
        sport400 = Button(window, text='400', style = "q.TButton", command = sports400)
        sport400.grid(column = 1, row = 6, pady = 7)
        sport500 = Button(window, text='500', style = "q.TButton", command = sports500)
        sport500.grid(column = 1, row = 7, pady = 7)
        
        geo100 = Button(window, text='100', style = "q.TButton", command = geography100)
        geo100.grid(column = 2, row = 3, pady = 7)
        geo200 = Button(window, text='200', style = "q.TButton", command = geography200)
        geo200.grid(column = 2, row = 4, pady = 7)
        geo300 = Button(window, text='300', style = "q.TButton", command = geography300)
        geo300.grid(column = 2, row = 5, pady = 7)
        geo400 = Button(window, text='400', style = "q.TButton", command = geography400)
        geo400.grid(column = 2, row = 6, pady = 7)
        geo500 = Button(window, text='500', style = "q.TButton", command = geography500)
        geo500.grid(column = 2, row = 7, pady = 7)
        
        mov100 = Button(window, text='100', style = "q.TButton", command = movie100)
        mov100.grid(column = 3, row = 3, pady = 7)
        mov200 = Button(window, text='200', style = "q.TButton", command = movie200)
        mov200.grid(column = 3, row = 4, pady = 7)
        mov300 = Button(window, text='300', style = "q.TButton", command = movie300)
        mov300.grid(column = 3, row = 5, pady = 7)
        mov400 = Button(window, text='400', style = "q.TButton", command = movie400)
        mov400.grid(column = 3, row = 6, pady = 7)
        mov500 = Button(window, text='500', style = "q.TButton", command = movie500)
        mov500.grid(column = 3, row = 7, pady = 7)
        
        sci100 = Button(window, text='100', style = "q.TButton", command = sci100)
        sci100.grid(column = 4, row = 3, pady = 7)
        sci200 = Button(window, text='200', style = "q.TButton", command = sci200)
        sci200.grid(column = 4, row = 4, pady = 7)
        sci300 = Button(window, text='300', style = "q.TButton", command = sci300)
        sci300.grid(column = 4, row = 5, pady = 7)
        sci400 = Button(window, text='400', style = "q.TButton", command = sci400)
        sci400.grid(column = 4, row = 6, pady = 7)
        sci500 = Button(window, text='500', style = "q.TButton", command = sci500)
        sci500.grid(column = 4, row = 7, pady = 7)
        
        finishgame = Button(window, text = 'End Game', command = endgame)
        finishgame.grid(column = 2, row = 11, pady = 5)
        
        global scoreteam1
        global scoreteam2
        global scoreteam3
        global scoreteam4
        global scoreteam5
            
        if num_of_teams == "1":
            t1 = Label(window, text = 'Team 1', style = "scorelabel.TLabel")
            t1.grid(column = 2, row = 8, pady = 10)
            team1 = Button(window, text='Add Score (+100)', command = team1score)
            team1.grid(column = 2, row = 10, pady = 20)
            t = Label(window, text=0, font = ("Arial Bold", 20))
            t.grid(column = 2, row = 9)

        elif num_of_teams == "2":
            t1 = Label(window, text = 'Team 1', style = "scorelabel.TLabel")
            t1.grid(column = 1, row = 8, pady = 10)
            team1 = Button(window, text='Add Score (+100)', command = team1score)
            team1.grid(column = 1, row = 10, pady = 20)
            t = Label(window, text=0, font = ("Arial Bold", 20))
            t.grid(column = 1, row = 9)
                
            t2 = Label(window, text = 'Team 2', style = "scorelabel.TLabel")
            t2.grid(column = 2, row = 8, pady = 10)
            team2 = Button(window, text='Add Score (+100)', command = team2score)
            team2.grid(column = 2, row = 10, pady = 20)
            tt = Label(window, text=0, font = ("Arial Bold", 20))
            tt.grid(column = 2, row = 9)

        elif num_of_teams == "3":
            t1 = Label(window, text = 'Team 1', style = "scorelabel.TLabel")
            t1.grid(column = 1, row = 8, pady = 10)
            team1 = Button(window, text='Add Score (+100)', command = team1score)
            team1.grid(column = 1, row = 10, pady = 20)
            t = Label(window, text=0, font = ("Arial Bold", 20))
            t.grid(column = 1, row = 9)
                
            t2 = Label(window, text = 'Team 2', style = "scorelabel.TLabel")
            t2.grid(column = 2, row = 8, pady = 10)
            team2 = Button(window, text='Add Score (+100)', command = team2score)
            team2.grid(column = 2, row = 10, pady = 20)
            tt = Label(window, text=0, font = ("Arial Bold", 20))
            tt.grid(column = 2, row = 9)
        
            t3 = Label(window, text = 'Team 3', style = "scorelabel.TLabel")
            t3.grid(column = 3, row = 8, pady = 10)
            team3 = Button(window, text='Add Score (+100)', command = team3score)
            team3.grid(column = 3, row = 10, pady = 20)
            ttt = Label(window, text=0, font = ("Arial Bold", 20))
            ttt.grid(column = 3, row = 9)
           
        elif num_of_teams == "4":
            t1 = Label(window, text = 'Team 1', style = "scorelabel.TLabel")
            t1.grid(column = 0, row = 8, pady = 10)
            team1 = Button(window, text='Add Score (+100)', command = team1score)
            team1.grid(column = 0, row = 10, pady = 20)
            t = Label(window, text=0, font = ("Arial Bold", 20))
            t.grid(column = 0, row = 9)
                
            t2 = Label(window, text = 'Team 2', style = "scorelabel.TLabel")
            t2.grid(column = 1, row = 8, pady = 10)
            team2 = Button(window, text='Add Score (+100)', command = team2score)
            team2.grid(column = 1, row = 10, pady = 20)
            tt = Label(window, text=0, font = ("Arial Bold", 20))
            tt.grid(column = 1, row = 9)
        
            t3 = Label(window, text = 'Team 3', style = "scorelabel.TLabel")
            t3.grid(column = 2, row = 8, pady = 10)
            team3 = Button(window, text='Add Score (+100)', command = team3score)
            team3.grid(column = 2, row = 10, pady = 20)
            ttt = Label(window, text=0, font = ("Arial Bold", 20))
            ttt.grid(column = 2, row = 9)
            
            t4 = Label(window, text = 'Team 4', style = "scorelabel.TLabel")
            t4.grid(column = 3, row = 8, pady = 10)
            team4 = Button(window, text='Add Score (+100)', command = team4score)
            team4.grid(column = 3, row = 10, pady = 20)
            tttt = Label(window, text=0, font = ("Arial Bold", 20))
            tttt.grid(column = 3, row = 9)
            
        else:
            t1 = Label(window, text = 'Team 1', style = "scorelabel.TLabel")
            t1.grid(column = 0, row = 8, pady = 10)
            team1 = Button(window, text='Add Score (+100)', command = team1score)
            team1.grid(column = 0, row = 10, pady = 20)
            t = Label(window, text=0, font = ("Arial Bold", 20))
            t.grid(column = 0, row = 9)
                
            t2 = Label(window, text = 'Team 2', style = "scorelabel.TLabel")
            t2.grid(column = 1, row = 8, pady = 10)
            team2 = Button(window, text='Add Score (+100)', command = team2score)
            team2.grid(column = 1, row = 10, pady = 20)
            tt = Label(window, text=0, font = ("Arial Bold", 20))
            tt.grid(column = 1, row = 9)
        
            t3 = Label(window, text = 'Team 3', style = "scorelabel.TLabel")
            t3.grid(column = 2, row = 8, pady = 10)
            team3 = Button(window, text='Add Score (+100)', command = team3score)
            team3.grid(column = 2, row = 10, pady = 20)
            ttt = Label(window, text=0, font = ("Arial Bold", 20))
            ttt.grid(column = 2, row = 9)
            
            t4 = Label(window, text = 'Team 4', style = "scorelabel.TLabel")
            t4.grid(column = 3, row = 8, pady = 10)
            team4 = Button(window, text='Add Score (+100)', command = team4score)
            team4.grid(column = 3, row = 10, pady = 20)
            tttt = Label(window, text=0, font = ("Arial Bold", 20))
            tttt.grid(column = 3, row = 9)
            
            t5 = Label(window, text = 'Team 5', style = "scorelabel.TLabel")
            t5.grid(column = 4, row = 8, pady = 10)
            team5 = Button(window, text='Add Score (+100)', command = team5score)
            team5.grid(column = 4, row = 10, pady = 20)
            ttttt = Label(window, text=0, font = ("Arial Bold", 20))
            ttttt.grid(column = 4, row = 9)

        window.mainloop()

    start = Tk()
    start.title("Home")
    start.geometry('410x500')
    start.configure(bg = 'cyan')
    
    style = ttk.Style() 
    style.theme_use("clam")
    style.configure("red.TButton", background = "red")
    style.configure("q.TButton", background = "blue", foreground = "white")
    style.configure("scorelabel.TLabel", background = "black", foreground = "white")
    style.configure("white.TLabel", background = "white")
    style.configure("title.TLabel", background = "blue", foreground = 'white')
    style.configure("start.TButton", background = "green", foreground = "white")
    style.configure("quit.TButton", background = "red", foreground = "white")
    
    logo = PhotoImage(file = 'jeopardynew.png')
    welcome = Label(start, text = 'Welcome to Python Jepoardy!', font = ("Courier", 25), style = "title.TLabel")
    welcome.grid(column = 0, row = 0, pady = 10)
    jeopardylogo = Label(start, image = logo)
    jeopardylogo.grid(column = 0, row = 1)
    instructions = Label(start, text = 'Press the "Start Game" button to start playing!', style = "title.TLabel")
    instructions.grid(column = 0, row = 2, pady = 10)
    numteam = Label(start, text = 'Select the number of teams playing', style = "title.TLabel")
    numteam.grid(column = 0, row = 3, pady = 10)

    teamselect = Combobox(start)
    teamselect['values'] = [1,2,3,4,5]
    teamselect.current(0)
    teamselect.grid(column = 0, row = 4, pady = 10)

    startgame = Button(start, text = 'Start Game', style = "start.TButton", command = playgame)
    startgame.grid(column = 0, row = 5, pady = 30)
    
    quitgame = Button(start, text = "Quit Application", style = "quit.TButton", command = quitapp)
    quitgame.grid(column = 0, row = 6)
    
    start.mainloop()
