# MapReduce
Mapreduce programs
-------------------------------
There are 3 scripts in this project, implemented using the Map reduce concept:

Math stats - mathstats.py -  Given a text file name on the command-line containing one number per line, prints out the sum, count, and standard-deviation of all the numbers in the file.
All statistics will be found in one pass through the data.small.txt and large.txt are the input files for this program.

Palendrome prime number finder - primes.py -  Outputs all the prime numbers which are palindromes between 2 and 10 million.

Password cracking - passCrack.py - Given a string of characters on the command line, finds what string hashes to it.  
Passwords are sometimes stored in a hashed form, so if the database is breached, the passwords are not easily usable. 
For this script, assumption is that we have a hash of a password in hex form. Given this hash on the command line, finds what password hashes to it. 
Only the first 5 characters of the hash are checked. Assuming passwords are 4 or fewer characters containing only lowercase letters and numbers.  
Using MapReduce to quickly look through all combinations for a match.Prints out the input hash string and the valid passwords which hash to it, if any. 
Using hashlib md5 hexdigest()and using the first 5 characters. Here are some passwords to crack: d077f, 0832c, 1a1dc, ee269, 0fe63
