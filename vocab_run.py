
import traceback
import vocabtrainer as vt

if __name__ == "__main__":
    try:
        user = vt.vocab_manager.Collect_Vocab('myvocab.db')
        user.sign_in()
        while user.is_user == True:
            user.action_list()
            
    except vt.errors.ExitApp as e:
        print(e)
    except Exception as e:
        print("Error Occurred: {}".format(e))
        traceback.print_tb(e)
        
    finally:
        if user.conn:
            user.conn.close()
