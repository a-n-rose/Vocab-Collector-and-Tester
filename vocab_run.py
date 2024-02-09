
import traceback
import vocab_lowkey as vlk

if __name__ == "__main__":
    try:
        user = vlk.vocab_manager.Collect_Vocab('vocab_test.db')
        user.sign_in()
        while user.is_user == True:
            user.action_list()
            
    except vlk.errors.ExitApp as e:
        print(e)
    except Exception as e:
        print("Error Occurred: {}".format(e))
        traceback.print_tb(e)
        
    finally:
        if user.conn:
            user.conn.close()
