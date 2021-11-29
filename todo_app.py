import typer

app=typer.Typer()
@app.command()
def add(t: str):
    t=t+'\n'
    file1=open("tasks.txt",'a')
    file1.write(t)
    file1.close()
@app.command()
def read():
    file1=open("tasks.txt",'r')
    res=file1.readlines()
    file1.close()
    for i in range(0,len(res)):
        print((i+1),". ",res[i])
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