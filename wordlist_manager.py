import re
import numpy as np

def prep_fill_in_the_blank(wordtuple_list,exampletuple_list):
    '''
    Saves examples and corresponding word value in tuple
    '''
    word_example_list = []
    for item_index in range(len(wordtuple_list)):
        word = wordtuple_list[item_index][0]
        ex_list = re.split(';',exampletuple_list[item_index][0])
        word_example_list.append((word,ex_list))
    return word_example_list
    
    
def rem_word_from_sentence(word_example_list):
    word_blank_list = []
    for word_set in word_example_list:
        blank_sentences = []
        for sentence in word_set[1]:
            if sentence != ' ':
                if word_set[0] in sentence:
                    blank = '_'*len(word_set[0])
                    sentence = sentence.replace(word_set[0],blank)
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

def check_response_fill_in_the_blank(target_word,response):
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
    for word_set in word_example_list:
        word = word_set[0]
        num_ex = len(word_set[1])
        rand_index = np.random.randint(low=0,high=num_ex)
        test_ex = word_set[1][rand_index]
        response = get_response_fill_in_the_blank(word,test_ex)
        if response != None:
            success = check_response_fill_in_the_blank(word,response)
            if success:
                points += 1
                print("\nWay to go!\n")
            else:
                print("\nHmmmmm.. not exactly. Let's try the next word.\n")
            count += 1
    score = get_total_score(points,count)
    return score
        
