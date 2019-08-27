import speech_recognition
from time import sleep
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("Chatbot")
bot_name = "ChatBot: "
#o vetor conversation armazena as perguntas e respostas, onde a primeira string é uma pergunta e sucessora a sua respectiva resposta e assim por diante

conversation = [
                #Greetings
                'Hello', "Hi!",
                "Hi", "Hello!",
                "what's up", "I don't use What's App.",
                "Joke", "Why was Hypno so energetic? He wasn’t Drowzee anymore!",
                "Tell me a joke", "What do you call a low fat Pokémon? Butterfree!",
                "Funny", "I do the best that I can.",
                "Useless", "If you ask about Pokémon natures I'll be more useful.",
                "How are you?", "I'm fine, thinking about how Pokémon natures are fantastic.",
                "are you ok?", "I'm fine, thinking about how Pokémon natures are fantastic.",
                "Who are you?", "I'm your personal assistant to help you to discover the effects of Pokémon natures.",
                "what's your name?", "You can see my name, can't you?. You can change my name spelling the words 'Configure a new name'.",
                "name", "You can see my name, can't you?. You can change my name spelling the words 'Configure a new name'.",
                #General information
                "Nature", "Like you probably already know, each Pokémon in main game series have stats. Natures are a mechanic that influences how a Pokémon stats grow. A Pokémon Nature usually affects the value of two of its stats, ultimately increasing one of its non-HP stats (Attack, Defense, Special Attack, Special Defense, or Speed) by 10% and decreasing another by 10%.",
                "Guide", "You can ask me all natures individually, or ask by stats, that I'll list all natures which enhance the stat that you asked for.",
                "trick room", "Trick Room is a Pokémon move that reverses the move order. Lower Pokémon with a lower speed stat attack first, while those with a higher speed stat will attack last. So, the best natures to a Trick Room team are those that decrease the speed status: Brave, Relaxed, Quiet and Sassy.",
                "tricky room", "Trick Room is a Pokémon move that reverses the move order. Lower Pokémon with a lower speed stat attack first, while those with a higher speed stat will attack last. So, the best natures to a Trick Room team are those that decrease the speed status: Brave, Relaxed, Quiet and Sassy.",
                "Neutral", "Neutral natures are those that just keep the original stats, that is, they won't induce any modification. They are Hardy, Docile, Serious, Quirky, and Bashful.",
                "Special", "There are two types of special stats: special attack and special defense.",
                "Mixed", "Mixed Pokémon are those which use both attack and special attack movements.",
                "Best", "The best nature to choose is a relative question. Depends of what you want to do with your Pokémon. If it is focused in physical attacks though, the ones that raise speed or attack can be useful. All depends of your strategy.",
                #Natures by stats
                "Attack", "The natures that boosts attack are Adamant, Brave, Naughty, and Lonely.",
                "Defense", "The natures that boosts defense are Bold, Relaxed, Impish, and Lax.",
                "Speed", "The natures that boosts speed are Timid, Hasty, Jolly, and Naive. Hey, if you are talking about the text speed, just spell the words 'Text speed'.",
                "Special Attack", "The natures that boosts special attack are Modest, Quiet, Mild, and Rash.",
                "Special Defense", "The natures that boosts special defense are Calm, Gentle, Sassy, and Careful.",
                #Natures individually: Attack boosts
                "Adamant", "Adamant nature boots 10% attack and decreases 10% special attack. It's most useful to Pokémon which purely uses physical attacks.",
                "Brave", "Brave nature boosts 10% attack and decreases 10% speed. Just use this nature on Pokémon that speed is not important or Trick Rooms teams.",
                "Naughty", "Naughty nature boosts 10% attack and decreases 10% special defense. Use this nature on 'mixed' Pokémon, which both attack and special attack are important but special defense isn't.",
                "Lonely", "Lonely nature boosts 10% attack and decreases 10% defense. Use this nature on 'mixed' Pokémon, which both attack and special attack are important but defense isn't.",
                #Natures individually: Defense boosts
                "Bold", "Bold nature will boost 10% of your Pokémon defense and will decrease 10% of your attack. This nature is useful in certain support, tank, or any Pokémon which needs defense to stay longer in battle. Of course, this Pokémon won't have attack as a priority.",
                "Impish", "Impish nature will boost 10% of your Pokémon defense and will decrease 10% of your special attack. This nature is useful in certain support, tank, or any Pokémon which needs defense to stay longer in battle. Of course, this Pokémon won't have special attack as a priority.",
                "Relaxed", "Relaxed nature boosts 10% defense and decreases 10% of your speed. Just use this nature on Pokémon that speed is not important or Trick Rooms teams.",
                "Lacks", "Lax nature boosts 10% defense and decreases 10% of your special defense. This nature is rarely used in competitive battles.",
                #Natures individually: Special Attack boosts
                "Modest", "Modest nature boots 10% special attack and decreases 10% attack. It's most useful to Pokémon which purely uses special attacks.",
                "Quiet", "Quiet nature boosts 10% special attack and decreases 10% speed. Just use this nature on Pokémon that speed is not important or Trick Rooms teams.",
                "Mild", "Mild nature boosts 10% special attack and decreases 10% defense. Use this nature on 'mixed' Pokémon, which both attack and special attack are important but defense isn't.",
                "Rash", "Rash nature boosts 10% special attack and decreases 10% special defense. Use this nature on 'mixed' Pokémon, which both attack and special attack are important but special defense isn't.",
                #Natures individually: Special Defense boosts
                "Calm", "Calm nature will boost 10% of your Pokémon special defense and will decrease 10% of your attack. This nature is useful in certain support, tank, or any Pokémon which needs special defense to stay longer in battle. Of course, this Pokémon won't have attack as a priority.",
                "Careful", "Careful nature will boost 10% of your Pokémon special defense and will decrease 10% of your special attack. This nature is useful in certain support, tank, or any Pokémon which needs special defense to stay longer in battle. Of course, this Pokémon won't have special attack as a priority.",
                "Sassy", "Sassy nature boosts 10% special defense and decreases 10% of your speed. Just use this nature on Pokémon that speed is not important or Trick Rooms teams.",
                "Gentle", "Gentle nature boosts 10% special defense and decreases 10% of your defense. This nature is rarely used in competitive battles.",
                #Natures individually: Speed boosts
                "Timid", "Timid nature will raise 10% of your speed stat and decrease 10% of your attack. It's extremely used in Pokémon with high special attack, the 'glass cannon' ones.",
                "Hasty", "Hasty nature boosts 10% of speed and decreases 10% defense. Commonly used in 'mixed' Pokémon that needs speed to do well in battle.",
                "Jolly", "Jolly nature will raise 10% of your speed stat and decrease 10% of your special attack. It's extremely used in Pokémon with high attack.",
                "Naive", "Naive nature boosts 10% of speed and decreases 10% special defense. Commonly used in 'mixed' Pokémon that needs speed to do well in battle.",
                #Natures individually: The neutral ones
                "Hardy", "This nature is a neutral one. Neutral natures are those that just keep the original stats, that is, they won't induce any modification.",
                "Quirky", "This nature is a neutral one. Neutral natures are those that just keep the original stats, that is, they won't induce any modification.",
                "Bashful", "This nature is a neutral one. Neutral natures are those that just keep the original stats, that is, they won't induce any modification.",
                "Serious", "This nature is a neutral one. Neutral natures are those that just keep the original stats, that is, they won't induce any modification.",
                "Docile", "This nature is a neutral one. Neutral natures are those that just keep the original stats, that is, they won't induce any modification.",
                #Bot configurations: keywords to
                "Configure a new name", "Please say my new name, I'm listening:",
                "close", "Closing the application...",
                "exit", "Closing the application...",
                "text speed", "Please choose a text speed:",
                "text speedy", "Please choose a text speed:"
               ]

bot.storage.drop()
trainer_chatbot = ListTrainer(bot)
trainer_chatbot.train(conversation)

#text speed:
text_speed_options = [0.01, 0.025, 0.035, 0.055]
text_speed = text_speed_options[2]

#loading bot:
for i in range(1, 4):
    print("Loading bot in {}...".format(i))
    sleep(1)
sleep(1)
print('\n' + bot_name, end='')
for charactere in "Hello! My name is {}. I'm your personal assistant to help you to discover the effects of Pokémon natures. Just talk to me, and I'll help you.".format(bot_name[:-2]):
    print(charactere, end='')
    if charactere == '.':
        sleep(1)
    sleep(text_speed)
print()

while True:
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        sleep(2)
        print("\nI'm listening... ")
        audio = recognizer.listen(source)

        try:
            question = recognizer.recognize_google(audio)
            #aparentemente o método listen chama o método Microphone que por sua vez recebe o aúdio source como parâmetro
            print('\nYou said: - ' + str(question)[0].upper() + str(question)[1:])
            answer = bot.get_response(question)
            if float(answer.confidence) > 0.5:
                sleep(1)
                print('\n'+bot_name, end='')
                for charactere in str(answer):
                    if charactere == '.':
                        print(charactere, end='')
                        sleep(1)
                    elif charactere == ',':
                        print(charactere, end='')
                        sleep(0.5)
                    elif charactere == '?':
                        print(charactere, end='')
                        sleep(3)
                    else:
                        print(charactere, end='')
                        sleep(text_speed)

                #These lines below describes how the bot changes its own name:
                if str(answer) == "Please say my new name, I'm listening:":
                    audio = recognizer.listen(source)
                    new_name = recognizer.recognize_google(audio)
                    sleep(1)
                    print('\n' + bot_name, end='')
                    for charactere in "Is my new name {}? Please say yes or no to confirm.".format(new_name):
                        print(charactere, end='')
                        sleep(text_speed)
                    print("\nI'm listening... ")
                    audio = recognizer.listen(source)
                    yes_or_no = recognizer.recognize_google(audio)
                    if yes_or_no == 'yes':
                        bot_name = new_name[0].upper()+ new_name[1:] + ": "
                        print('\n'+bot_name, end='')
                        for charactere in str(new_name[0].upper()+ new_name[1:]+ "? I loved it!"):
                            print(charactere, end='')
                            sleep(text_speed)
                        print()
                    elif yes_or_no == 'no':
                        print('\n'+bot_name, end='')
                        for charactere in "Name change cancelled.":
                            print(charactere, end='')
                            sleep(text_speed)
                        print()
                    else:
                        print('\n'+bot_name, end='')
                        for charactere in "You didn't type it correctly, please try again.":
                            print(charactere, end='')
                            sleep(text_speed)
                        print()

                #Changing the text speed:
                elif str(answer) == "Please choose a text speed:":
                    changed = 0
                    while changed == 0:
                        sleep(1)
                        for charactere in "\n1- REALLY FAST\n2- FAST\n3- NORMAL\n4- SLOW\n\nThe current text speed is the option {}.".format(text_speed_options.index(text_speed)+1):
                            print(charactere, end='')
                            sleep(text_speed)
                        sleep(1)
                        print("\nListening the new text speed option...")
                        sleep(1)
                        audio = recognizer.listen(source)
                        new_speed = recognizer.recognize_google(audio)
                        print('\nYou said: - ' + str(question)[0].upper() + str(new_speed)[1:])
                        if str(new_speed) == 'really fast' or str(new_speed) =='one':
                            text_speed = text_speed_options[0]
                            sleep(1)
                            print('\n' + bot_name, end='')
                            for charactere in str("New text speed set successfully."):
                                print(charactere, end='')
                                sleep(text_speed)
                            print()
                            changed = 1
                        elif str(new_speed) == 'fast' or str(new_speed) =='two':
                            text_speed = text_speed_options[1]
                            sleep(1)
                            print('\n' + bot_name, end='')
                            for charactere in str("New text speed set successfully."):
                                print(charactere, end='')
                                sleep(text_speed)

                            print()
                            changed = 1
                        elif str(new_speed) == 'normal' or str(new_speed) =='three':
                            text_speed = text_speed_options[2]
                            sleep(1)
                            print('\n' + bot_name, end='')
                            for charactere in str("New text speed set successfully."):
                                print(charactere, end='')
                                sleep(text_speed)
                            print()
                            changed = 1
                        elif str(new_speed) == 'slow' or str(new_speed) == 'four':
                            text_speed = text_speed_options[3]
                            sleep(1)
                            print('\n' + bot_name, end='')
                            for charactere in str("New text speed set successfully."):
                                print(charactere, end='')
                                sleep(text_speed)
                            print()
                            changed = 1
                        else:
                            sleep(1)
                            print('\n' + bot_name, end='')
                            for charactere in str("You didn't spelled it correctly, please try again."):
                                print(charactere, end='')
                                sleep(text_speed)
                            print()
                #Closing the bot:
                elif str(answer) == "Closing the application...":
                    break
            else:
                sleep(1)
                print(bot_name + "Hmm, it seems that I don't know the answer for that specific question... for now.")
        except speech_recognition.UnknownValueError:
            sleep(1)
            print('\n'+bot_name + "Couldn't understand nothing that you've said.")
