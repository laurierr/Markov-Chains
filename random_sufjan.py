import MarkovChain

File = open("carrie_and_lowell_lyrics.txt")


decision = raw_input("Set weight on 2 or 3 (less is more...random) > ")
length = raw_input("enter a number of words you want to see. normal is about 70: ")

if int(decision) == 2:
    markov = MarkovChain.MarkovChain(File, decision)
    print(markov.generate_text_two(int(length)))
elif int(decision) == 3:
    markov = MarkovChain.MarkovChain(File, decision)
    print(markov.generate_text_three(int(length)))
