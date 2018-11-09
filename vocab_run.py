
from vocab_collector import Collect_Vocab
import traceback
from errors import ExitApp

if __name__ == "__main__":
    try:
        user = Collect_Vocab('vocab_REAL.db')
        user.sign_in()
        while user.is_user == True:
            user.action_list()
            
    except ExitApp as e:
        print(e)
    except Exception as e:
        print("Error Occurred: {}".format(e))
        traceback.print_tb(e)
        
    finally:
        if user.conn:
            user.conn.close()
