import re
import numpy as np
import random

def prep_fill_in_the_blank(wordexample_tuple_list):
    '''
    Saves examples and corresponding word value in tuple
    '''
    word_example_list = []
    for item_index in range(len(wordexample_tuple_list)):
        word = wordexample_tuple_list[item_index][0]
        ex_list = re.split(';',wordexample_tuple_list[item_index][1])
        word_example_list.append((word,ex_list))
    return word_example_list
    
def rem_word_from_sentence(word_example_list):
    word_blank_list = []
    for word_set in word_example_list:
        blank_sentences = []
        for sentence in word_set[1]:
            if sentence != ' ':
                if word_set[0].lower() in sentence.lower():
                    blank = '_'*len(word_set[0])
                    sentence = sentence.lower().replace(word_set[0].lower(),blank)
                    blank_sentences.append(sentence)
        word_blank_list.append((word_set[0],blank_sentences))
    return word_blank_list

def get_response_fill_in_the_blank(word,test_ex):
    print("Enter the word that fills the blank.\n")
    print("\n{}\nYour answer:".format(test_ex))
    response = input()
    if 'exit' == response.lower:
        return None
    return response

def check_response_quiz(target_word,response):
    '''
    .lower() --->  this is very rudimentary.. eg German nouns need to be capitalized. This is to avoid if someone enters a word as capitalized, if it's at the beginning of a sentence, say.
    '''
    if response.lower() == target_word.lower():
        return True
    return False
    
def get_total_score(points,total_points_possible):
    score = round(points/float(total_points_possible)*100,2)
    return score
    
def test_fill_in_the_blank(word_example_list):
    points = 0
    count = 0
    if len(word_example_list) > 0:
        for word_set in word_example_list:
            word = word_set[0]
            num_ex = len(word_set[1])
            rand_index = np.random.randint(low=0,high=num_ex)
            test_ex = word_set[1][rand_index]
            response = get_response_fill_in_the_blank(word,test_ex)
            if response != None:
                success = check_response_quiz(word,response)
                if success:
                    points += 1
                    print("\nWay to go!\n")
                else:
                    print("\nHmmmmm.. not exactly. Let's try the next word.\n")
                count += 1
        score = get_total_score(points,count)
    else:
        print("No example sentences were found. Try another quiz!")
        return None
    return score

def get_response_flashcard(wordmeaning_tuple):
    print("\nWhat is the meaning of this word: \n")
    print(wordmeaning_tuple[0],"\n")
    response = input()
    if 'exit' == response.lower:
        return None
    success = check_response_quiz(wordmeaning_tuple[1],response)
    if success:
        print("\nGreat job!\n")
    else:
        print("\nThis was the correct meaning: {}\n".format(wordmeaning_tuple[1]))
    return success
    

def test_flashcards(word_meaning_list):
    points = 0
    count = 0
    for pair in word_meaning_list:
        success = get_response_flashcard(pair)
        if success != None: 
            if success == True:
                points += 1
                count += 1
            else:
                count += 1
    score = get_total_score(points,count)
    return score


def show_score(score):
    if score < 70:
        msg = "Great job practicing! Keep at it and you will improve."
    elif score < 90:
        msg = "Not bad! On this track you'll know these words like the back of your hand!"
    elif score < 100:
        msg = "Great work!"
    else:
        msg = "Perfect score! I think you gotta find some harder words."
    print("\nYour score: {}% \n{}".format(score,msg))
    return None


def prep_multchoicedict(wordmeaning_tuple,possible_meanings_list):
    #select at random wrong meanings for the target word
    list_target_removed = possible_meanings_list.copy()
    list_target_removed.remove(wordmeaning_tuple[1])
    if len(list_target_removed) < 3:
        rand_indices = random.sample(range(len(list_target_removed)),len(list_target_removed))
    else:
        rand_indices = random.sample(range(len(list_target_removed)),3)
    wrong_options = [list_target_removed[j] for j in rand_indices]
    
    #choose the answer index at random:
    goal_len = len(wrong_options)+1
    answer_index = random.choice(random.sample(range(goal_len),1))
    
    #prep dictionary for presenting multiple choice question
    dict_options = {}
    for i in range(goal_len):
        if i == answer_index:
            dict_options[str(i+1)] = (wordmeaning_tuple[1],True)
        else:
            if len(wrong_options) > 0:
                dict_options[str(i+1)] = (wrong_options[0],False)
                wrong_options.remove(wrong_options[0])
            else:
                print("Hmmmm something funny happened while making the multiple choice dict.")
    return dict_options


def get_response_multiplechoice(wordmeaning_tuple,possible_meanings_list):
    print("\nWhich of the meanings below (enter the corresponding number) best matches this word: \n\n{}\n".format(wordmeaning_tuple[0]))
    options_dict = prep_multchoicedict(wordmeaning_tuple,possible_meanings_list)
    for key, value in options_dict.items():
        print("{} --> {}\n".format(key,value[0]))
    response = input()
    if 'exit' in response.lower():
        return None
    if response.isdigit():
        if int(response) <= len(options_dict):
            success = options_dict[response][1]
            if success:
                print("\nGreat job!\n")
            else:
                print("\nThe correct meaning was: {}\n".format(wordmeaning_tuple[1]))
            return success
        else:
            print("Please choose the corresponding number")
            get_response_multiplechoice(wordmeaning_tuple,possible_meanings_list)
    return None

def get_possible_choices(word_meaning_list):
    possible_meanings = []
    for pair in word_meaning_list:
        possible_meanings.append(pair[1])
    return possible_meanings
        

def test_multiplechoice(word_meaning_list):
    points = 0
    count = 0
    word_meaning_list = get_possible_choices(word_meaning_list)
    for pair in word_meaning_list:
        success = get_response_multiplechoice(pair,possible_meanings)
        if success != None:
            if success == True:
                points += 1
                count += 1
            else:
                count += 1
    score = get_total_score(points,count)
    return score
                
