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
    
def search_and_rm_word(word_set:tuple, sentence:str) -> tuple:
    """Checks if the word or parts of the word are in the sentence. 

    Returns word or section of the word found in 'sentence'. If nothing found,
    returns None.

    German nouns contain relevant articles that change form in 
    different contexts, e.g. "Das Haus gefällt mir" and "Sie ist im Haus".
    This function aims to handle (at a basic level) such changes.
    """
    if word_set[0].lower() in sentence.lower():
        word_tmp = word_set[0]
        
    #problem here:
    #removes all capitalized letters which are necessary in some languages
    # If the word has two parts, e.g. "das Haus", will look for either one
    elif len(word_set[0].lower().split()) == 2:
        if word_set[0].lower().split()[0] in sentence.lower():
            word_tmp = word_set[0].split()[0]
        elif word_set[0].lower().split()[1] in sentence.lower():
            word_tmp = word_set[0].split()[1]
        # TODO raise warning otherwise
    blank = '_'*len(word_tmp)
    start_index = sentence.lower().index(word_tmp.lower())
    sentence = sentence.replace(sentence[start_index:start_index+len(blank)],blank)
    return tuple((word_tmp, sentence))

# Needs to be adapted to handle more complexities of language
# Perhaps improvable with nltk? 
# TODO add warnings for when cases are clearly missed.
# TODO clean this function up
def rem_word_from_sentence(word_example_list):
    word_blank_list = []
    for word_set in word_example_list:
        blank_sentences = []
        for sentence in word_set[1]:
            if sentence != '':
                # TODO might not need word_tmp, aka the word actually present in sentence
                word_tmp, sentence_w_blank = search_and_rm_word(word_set, sentence)
                blank_sentences.append(sentence_w_blank)
        word_blank_list.append((word_tmp,blank_sentences))
    return word_blank_list

def get_response_fill_in_the_blank(word,test_ex):
    print("Enter the word that fills the blank.\n")
    print("\n{}\nYour answer:".format(test_ex))
    response = input()
    if 'exit' == response.lower():
        return None
    return response

def check_response_quiz(target_word,response):
    '''
    .lower() --->  this is very rudimentary.. eg German nouns need to be capitalized. This is to avoid if someone enters a word as capitalized, if it's at the beginning of a sentence, say.
    '''
    if response.lower() == target_word.lower():
        print("\nWay to go!")
        return True
    elif response.lower() in target_word.lower():
        print("\nThat's not quite the full answer, but we'll give you the points.")
        print(f"The Correct answer: {target_word}")
        return True
    return False
    
def get_total_score(points,total_points_possible):
    score = round(points/float(total_points_possible)*100,2)
    return score
    
# Bad name for a function: TODO replace word "test" 
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
                else:
                    print(f"\nHmmmmm.. not exactly. The correct answer: {word}")
                    print("Let's try the next word.\n")
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

def prep_wrong_meanings(target_meaning, possible_meanings_list):
    # select at random wrong meanings for the target word
    # save them to a new list 'wrong_options'
    list_target_removed = possible_meanings_list.copy()
    list_target_removed.remove(target_meaning)
    if len(list_target_removed) < 3:
        rand_indices = random.sample(range(len(list_target_removed)),len(list_target_removed))
    else:
        rand_indices = random.sample(range(len(list_target_removed)),3)
    wrong_options = [list_target_removed[j] for j in rand_indices]
    return wrong_options

def get_answer_index(goal_len):
    answer_index = random.choice(random.sample(range(goal_len),1))
    return answer_index
    
def setup_multchoice_dict(goal_len, answer_index, target_meaning, wrongmeaning_list):
    ''' This assigns a random index for the answer 
    so that the answer is not always in the same spot when 
    presenting options to the user. The possible meanings are put in random
    order when the list was made'''
    dict_options = {}
    for i in range(goal_len):
        if i == answer_index:
            dict_options[str(i+1)] = (target_meaning,True)
        else:
            if len(wrongmeaning_list) > 0:
                dict_options[str(i+1)] = (wrongmeaning_list[0],False)
                wrongmeaning_list.remove(wrongmeaning_list[0])
            else:
                print("Hmmmm something funny happened while making the multiple choice dict.")
    return dict_options

def prep_multchoicedict(wordmeaning_tuple,possible_meanings_list):
    #prep wrong options
    wrong_options = prep_wrong_meanings(wordmeaning_tuple[1],possible_meanings_list)
    
    #choose the answer index at random:
    goal_len = len(wrong_options)+1
    answer_index = get_answer_index(goal_len)
    
    #prep dictionary for presenting multiple choice question
    multchoice_dict = setup_multchoice_dict(goal_len,answer_index,wordmeaning_tuple[1],wrong_options)
    return multchoice_dict


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
    possible_meanings = get_possible_choices(word_meaning_list)
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
                
