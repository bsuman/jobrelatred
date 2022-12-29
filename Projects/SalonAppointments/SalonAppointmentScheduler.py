import psycopg2 as pgsql

mydb = pgsql.connect("dbname=salon_info user=postgres password=Mario123")
curr = mydb.cursor()


def displayServices(records, serviceIds):
    for service in records:
        serviceIds.append(int(service[0]))
        print(str(service[0]) + ': ' + str(service[1]))
    service_id = int(input())
    return service_id


def findEmployeeInfo(phone_number, service_id):
    query = "select * from customers where phone = \'" + phone_number + "\'"
    curr.execute(query)
    customers = curr.fetchall()
    if len(customers) == 0:
        print("I don't have a record for that phone number, what's your name?")
        name = input()
        query = "insert into customers (phone,name) values (\'" + phone_number + "\',\'" + name + "\') RETURNING customer_id"
        curr.execute(query)
        records = curr.fetchall()
        mydb.commit()
        customer_id = records[0][0]
        print("What date and time would you like your cut,{}? Please use the format yyyy-mm-dd hh:mm, for example 1999-01-08 04:05".format(name))
        time = input()
        print("I have put you down for a cut at {}, {}.".format(time, name))
        query = "insert into appointments (customer_id,service_id,time) values (\'" + str(customer_id) + "\',\'" + str(service_id) + "\',\'" + time + "\')"
        curr.execute(query)
        mydb.commit()
    else:
        customer = customers[0]
        customer_id = customer[0]
        name = customer[2]
        print("What date and time would you like your cut,{}? Please use the format yyyy-mm-dd hh:mm, for example 1999-01-08 04:05".format(name))
        time = input()
        query = "insert into appointments (customer_id,service_id,time) values (\'" + str(customer_id) + "\',\'" + str(
            service_id) + "\',\'" + time + "\')"
        curr.execute(query)
        mydb.commit()
        print("I have put you down for a cut at {}, {}.".format(time, name))


def startApp():
    curr.execute("select * from services")
    records = curr.fetchall()
    serviceIds = []
    phone_number = -1
    print("Welcome to the Salon Appointment App")
    print("Choose one of the following services")
    while True:
        service_id = displayServices(records, serviceIds)
        if service_id in serviceIds:
            print("please provide your phone number:")
            phone_number = input()
            break
        else:
            print("Chosen service not among the provided services. Please choose the valid service!")

    findEmployeeInfo(phone_number, service_id)


startApp()
