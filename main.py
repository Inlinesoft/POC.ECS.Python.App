import smtplib
import datetime
import time
from utilities import email

def start_process():
    try:
        start_time = datetime.datetime.now()
        time.sleep(30)
        end_time = datetime.datetime.now()
        _email = email.Email()
        is_email_sent = _email.send_mail_using_smtp(
            send_from='kashif.mehali@gmail.com',
            send_to='kashif.ali@hotmail.co.uk',
            subject='A test email from poc.ecs.python.app - ' +
                    datetime.datetime.strftime(datetime.datetime.now(), '%a %d-%b-%Y %X'),
            text='A test email from poc.ecs.python.app - \r\n' +
                    'Start Time : ' + datetime.datetime.strftime(start_time, '%a %d-%b-%Y %X') + '\r\n' +
                    'End Time : ' + datetime.datetime.strftime(end_time, '%a %d-%b-%Y %X'),
            text_type='html')


        print ("Email sent!")
    except Exception as exp:
        print (f"Something went wrong... : {exp}" )


if __name__ == "__main__":

    print("****************************************************************************************************")
    print("*                                                                                                  *")
    print("*                                [START] >>> POC.ECS.Python.App                                    *")
    print("*                                                                                                  *")
    print("****************************************************************************************************")

    # call the main method
    start_process()

    print("****************************************************************************************************")
    print("*                                                                                                  *")
    print("*                                 [END] >>> POC.ECS.Python.App                                     *")
    print("*                                                                                                  *")
    print("****************************************************************************************************")