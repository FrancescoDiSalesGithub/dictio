import dbhandler
import sys 

if __name__ == "__main__":
    
    db_handler = dbhandler.dbhandler(sys.argv[1],sys.argv[2])
    db_handler.download_list()

