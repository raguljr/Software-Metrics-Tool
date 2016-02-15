import re
def frr(sf):
    fp=open(sf,"r")
    con=fp.read()
    fp.close()
    co=0
    ll=0

    fp=open(sf,"r")

    for l in fp.readlines():
        if bool(l.strip())==False:
            co=co+1
    
    cl=con.count("//")
    tl=con.count("\n")
    nn=re.sub(r'//.*',"",con)
    sc=nn.count(";")
    ll=con.split().count("if")+con.split().count("while")+con.split().count("void")

    return "line of code:",str(tl),"\nBlank lines",str(co),"\nComment lines:",str(cl),"\nExecutable physical: ",str(tl-cl-co),"\nExecutable logical:",str(sc+ll)
    
