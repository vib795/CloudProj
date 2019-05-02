import sqlite3
import sys
from mpi4py import MPI

name = sys.argv[1]
conn = sqlite3.connect('stripped_address.db')

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

c = conn.cursor()

with open("resultsN.txt", "w+") as f:
	if rank == 0:
		c.execute("SELECT COUNT(*) FROM OFAC_Names_List WHERE (ID BETWEEN 1 AND 1520) AND Query_String=?;", (name,))
		result = c.fetchone()
		comm.Barrier()
		if result[0] == 1:
			f.write(str(result[0]))
	elif rank == 1:
		c.execute("SELECT COUNT(*) FROM OFAC_Names_List WHERE (ID BETWEEN 1521 AND 3040) AND Query_String=?;", (name,))
		result = c.fetchone()
		comm.Barrier()
		if result[0] == 1:
			f.write(str(result[0]))
	elif rank == 2:
		c.execute("SELECT COUNT(*) FROM OFAC_Names_List WHERE (ID BETWEEN 3041 AND 4560) AND Query_String=?;", (name,))
		result = c.fetchone()
		comm.Barrier()
		if result[0] == 1:
			f.write(str(result[0]))
	elif rank == 3:
		c.execute("SELECT COUNT(*) FROM OFAC_Names_List WHERE (ID BETWEEN 4561 AND 6080) AND Query_String=?;", (name,))
		result = c.fetchone()
		comm.Barrier()
		if result[0] == 1:
			f.write(str(result[0]))
	else:
		c.execute("SELECT COUNT(*) FROM OFAC_Names_List WHERE (ID BETWEEN 6081 AND 7601) AND Query_String=?;", (name,))
		result = c.fetchone()
		comm.Barrier()
		if result[0] == 1:
			f.write(str(result[0]))
f.close()