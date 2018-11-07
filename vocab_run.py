
from vocab_collector import Collect_Vocab
import traceback
from errors import ExitApp

if __name__ == "__main__":
    try:
        cv = Collect_Vocab('vocab_REAL.db')
        cv.sign_in()
        while cv.is_user == True:
            cv.action_list()
            
    except ExitApp as e:
        print(e)
    except Exception as e:
        print("Error Occurred: {}".format(e))
        traceback.print_tb(e)
        
    finally:
        if cv.conn:
            cv.conn.close()
