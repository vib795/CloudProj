import sqlite3
import sys
from mpi4py import MPI

address = sys.argv[1]
conn = sqlite3.connect('stripped_address.db')

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

c = conn.cursor()

with open("results.txt", "w+") as f:
	if rank == 0:
		c.execute("SELECT COUNT(*) FROM OFAC_Address_List WHERE (ID BETWEEN 1 AND 1601) AND Query_String=?;", (address,))
		result = c.fetchone()
		comm.Barrier()
		if result[0] == 1:
			f.write(str(result[0]))
	elif rank == 1:
		c.execute("SELECT COUNT(*) FROM OFAC_Address_List WHERE (ID BETWEEN 1602 AND 3203) AND Query_String=?;", (address,))
		result = c.fetchone()
		comm.Barrier()
		if result[0] == 1:
			f.write(str(result[0]))
	elif rank == 2:
		c.execute("SELECT COUNT(*) FROM OFAC_Address_List WHERE (ID BETWEEN 3204 AND 4804) AND Query_String=?;", (address,))
		result = c.fetchone()
		comm.Barrier()
		if result[0] == 1:
			f.write(str(result[0]))
	elif rank == 3:
		c.execute("SELECT COUNT(*) FROM OFAC_Address_List WHERE (ID BETWEEN 4805 AND 6405) AND Query_String=?;", (address,))
		result = c.fetchone()
		comm.Barrier()
		if result[0] == 1:
			f.write(str(result[0]))
	else:
		c.execute("SELECT COUNT(*) FROM OFAC_Address_List WHERE (ID BETWEEN 6406 AND 8006) AND Query_String=?;", (address,))
		result = c.fetchone()
		comm.Barrier()
		if result[0] == 1:
			f.write(str(result[0]))
f.close()