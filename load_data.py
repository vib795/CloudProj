from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

Base = declarative_base()

class LoadNames(Base):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'Names'
    __table_args__ = {'sqlite_autoincrement': True}
    #tell SQLAlchemy the name of column and its attributes:
    id = Column(Integer, primary_key=True, nullable=False) 
    Number1 = Column(Integer)
    Number2 = Column(Integer)
    Aka = Column(String)
    Name = Column(String)
    NulledOut = Column(Integer)

if __name__ == "__main__":
    t = time()

    #Create the database
    engine = create_engine('sqlite:///mydatabase.db')
    Base.metadata.create_all(engine)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:
        file_name = "/home/utkarshsingh/CloudComputing/ofac_cc_proj/FILES/OFAC_FILES/aka_names_csv_format.csv" #CSV file used
        data = Load_Data(file_name) 

        for i in data:
            record = Price_History(**{
                'Number1' : i[0],
                'Number2' : i[1],
                'Aka' : i[2],
                'Name' : i[3],
                'NulledOut' : i[4]
            })
            s.add(record) #Add all the records

        s.commit() #Attempt to commit all the records
    except:
        s.rollback() #Rollback the changes on error
    finally:
        s.close() #Close the connection
   # print "Time elapsed: " + str(time() - t) + " s." #0.091s