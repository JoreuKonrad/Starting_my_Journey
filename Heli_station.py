#Creating a fuel station for helicopters

import pandas as pd
import random
import datetime

#Creating Client DataFrame
client = []
Client = pd.DataFrame(client, columns=['ID','Model','Company'])

#Lists of Helicopter Companies and Models
List_Companies = ('Agusta','Bell','Airbus')
List_Agusta = ('AW109','AW119')
List_Airbus = ('H125','H130','H135')
List_Bell = ('B505','B407','B429')

#Generating Clients and inserting them to Client DataFrame
for x in range(5):
    ID = random.choice(range(1000,9999))
    Company = random.choice(List_Companies)
    Model = 0
    if Company == 'Agusta':
        Model = random.choice(List_Agusta)
    if Company == 'Airbus':
        Model = random.choice(List_Airbus)
    if Company == 'Bell':
        Model = random.choice(List_Bell)
    Cliente = {'ID':ID,'Model':Model,'Company':Company}
    Client.loc[len(Client)] = [ID,Model,Company]

#Setting ID column as index
#Client = Client.set_index('ID')

#Printing
print('')
print('Client List:')
print(Client)
print('')

#Creating the Station DataFrame
station = ()
Station = pd.DataFrame(station,columns=['ID','Model','Company','Fuel_Filled'])

#Generating the Client frequencies
for x in range(5):
    ID = random.choice(Client['ID'])
    FClient = Client[Client['ID'] == ID]
    Station = pd.concat([Station, FClient], axis=0, ignore_index=True)

    #Creating a probability if the client asked for fuel
    Prob_Fill = random.choice(range(1,10))
    if Prob_Fill <= 3:
        Station.loc[x,'Fuel_Filled'] = random.choice(range(100,350))
    if Prob_Fill > 3:
        Station.loc[x,'Fuel_Filled'] = 0

    #Creating the arrival column and inserting a date
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2020, 2, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    Station.loc[x,'Arrival'] = random_date

    #Creating the departure date
    Depature = random_date + datetime.timedelta(days=random.choice(range(0,3)))
    Station.loc[x, 'Depature'] = Depature

    #Calculating the Total Bill
    parking_tax = (1 + Depature.day - random_date.day) * 200
    fuel_Price = 5.9
    fuel_bill = fuel_Price * Station.loc[x, 'Fuel_Filled']
    total_bill = parking_tax + fuel_bill
    Station.loc[x, 'Parking_Tax'] = parking_tax
    Station.loc[x, 'Fuel_Price'] = fuel_Price
    Station.loc[x, 'Fuel_Bill'] = fuel_bill
    Station.loc[x, 'Total_Bill'] = total_bill

print(Station.sort_values(by='Arrival',ignore_index=True))


