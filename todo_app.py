import typer
import datetime
from datetime import date
app=typer.Typer()
@app.command()
def add(t: str):
    time=''
    time = typer.prompt("deadline?(dd/mm/yyyy)")
    at=''
    at = typer.prompt("at?(HH:MM)")
    t=time+" at "+at+" "+t+'\n'
    file1=open("tasks.txt",'a')
    file1.write(t)
    file1.close()
@app.command()
def read():
    today1 = datetime.datetime.now()
    file1=open("tasks.txt",'r')
    res=file1.readlines()
    file1.close()
    for i in range(0,len(res)):
        u=res[i]
        d=int(u[0]+u[1])
        m=int(u[3]+u[4])
        y=int(u[6]+u[7]+u[8]+u[9])
        h=int(u[14]+u[15])
        min=int(u[17]+u[18])
        now=datetime.datetime(y,m,d,h,min)
        lefttime=str(now-today1)
        print((i+1),". ",res[i])
        if(lefttime[0]=="-"):
            print("Overdue")
        else:
            print("Time left is:",lefttime)
@app.command()
def delete(num: int):
    with open(r"tasks.txt", 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        for number, line in enumerate(lines):
            if number not in [num-1]:
                fp.write(line)
if __name__ == "__main__":
    app()
