def Openfile():
    f= open("answers.txt","w+")
    
    for i in range(5):
         f.write("This Question has been answered by Benard %d\r\n" % (i+1))
    f.close()
    
    f=open("answers.txt", "r")
    if f.mode == 'r':
      contents =f.read()
    print (contents)
    
    fl =f.readlines()
    for x in fl:
        print(x)

if __name__== "__main__":
  Openfile()