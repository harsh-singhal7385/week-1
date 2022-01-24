with open('file.txt','r+') as f:
    f.seek(len(f.read())+5)

    f.write("\nabc, lmn, pqr, xyz\n")
    f.write("111, 222, 333, 444\n")
    print(" My Data has been Appended Successfully to file named file.txt")
f.close()
