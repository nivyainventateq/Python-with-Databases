from userfile import SampleDatabase

def main():
    db=SampleDatabase()
    while True:
        print("\n")
        print("press 1 to insert new data")
        print("press 2 to display data")
        print("press 3 to delete data")
        print("press 4 to update data")
        print("press 5 to exit program")
        print("\n")
        try:
            choice=int(input())
            if(choice==1):       # insert
                userid=int(input("enter user id:"))
                username=input("enter username:")
                phone=int(input("enter user phoneno:"))
                db.insert(userid,username,phone)
                pass
            elif choice==2:      # display
                db.fetch()
                pass
            elif choice==3:      # delete
                userid=int(input("enter userid which u wanna to delete:"))
                db.delete(userid)
                pass
            elif choice==4:      # update
                userid = int(input("enter id of existing user:"))
                username = input("enter new name:")
                phone = int(input("enter new phoneno:"))
                db.update(userid, username, phone)
                pass
            elif choice==5:
                break
            else:
                print("Invalid input.... Plz Try again")
        except Exception as e:
            print(e)
            print("Invalid details")

if __name__== '__main__':
    main()

