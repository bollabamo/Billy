import csv
import os
import sys

ifile  = open('input.csv', "rb")
ofile  = open('output.csv', "wb")
complete = 0
incomplete = 0
first = 1
second = 1
username = ''
prior_user = ''

writer = csv.writer(ofile)
reader = csv.reader(ifile)
writer.writerow(["Username", "First Name", "Last Name", "Completed Mapped Items", "Incomplete Mapped Items", "Email", "Manager", "VP Name", "Sub-department"])
for row in reader:
  if(first == 1):
    prior_user = row[3]
    first = 0
  else:
    prior_user = username
  username = row[3]
  if(username != prior_user):
      writer.writerow([prior_user, fname, lname, complete, incomplete, email, manager, vp, sub])
      complete = 0
      incomplete = 0
  fname = row[4]
  lname = row[5]
  email = row[6]
  manager = row[7]
  vp = row[8]
  sub = row[9]
  status = row[2]
  if(status == "Completed"):
      complete += 1
  elif(status == "Incomplete"):
      incomplete += 1

writer.writerow([username, fname, lname, complete, incomplete, email, manager, vp, sub])
complete = 0
incomplete = 0