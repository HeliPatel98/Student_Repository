from datetime import datetime, timedelta
from typing import Tuple, Iterator
import os
from prettytable import PrettyTable

def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """The function describes date and time of specific dates before and of between."""
    date1:str = "27 Feb 2020"
    date2:str = "27 Feb 2019"
    date5:str = "1 Feb 2019"
    date6:str = "30 Sep 2019"

    dt1:datetime = datetime.strptime(date1, "%d %b %Y")
    dt2:datetime = datetime.strptime(date2, "%d %b %Y")
    dt5:datetime = datetime.strptime(date5, "%d %b %Y")
    dt6:datetime = datetime.strptime(date6, "%d %b %Y")


    num_days:int = 3
    dt3:datetime = dt1 + timedelta(days=num_days)
    dt4:datetime = dt2 + timedelta(days=num_days)
    
    

    delta:datetime = dt6 - dt5
 

    return (dt3,dt4,delta.days)


def file_reader(path,fields,sep,header=False) -> Iterator[Tuple[str]]:
    """ This function fetches the text file and converts it into tuple when header is true otherwise raises a ValueError for different values."""
    path:str
    sep:str
    fields:int
    header:bool
    a:list = []
    count:int = 0
    try:
        f:IO = open(path)
    except FileNotFoundError:
        print("File not found")
    else:
        for line in f:
            line1 = line.rstrip("\n")
            if header==True and count==0:
                count=1
                continue
            line2 = line1.split(sep)
            count +=1
            
            try:
                if len(line2) != fields:
                    raise ValueError
            except ValueError:

                raise ValueError(f'the file name: {path} \n the line number in the file where the problem occurred:  {count} \n the number of fields found in the line: {len(line)} \n the number of fields expected in the line:{fields}')        
                
            yield (tuple(line2))     
 
            
            

class FileAnalyzer:
    """ The class defines the way to print the pretty table from the python files."""
    def __init__(self, directory: str) -> None:
        """ Directory is get and then stored in a dictionary."""
        self.directory: str = os.getcwd()
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        self.directory=directory
        self.analyze_files()

    def analyze_files(self) -> None:
        """ The directory is changed to working dircetory and functions,lines,characters and classes are counted in python files."""
        path:str = os.chdir(self.directory)
        files : list = os.listdir(path)
        line_count:int=0
        char_count:int=0
        func_count:int=0
        class_count:int=0
        for filename in files:
            if filename.endswith('.py'):
                try:
                    f1=os.path.join(self.directory,filename)
                    file = open(filename,"r")
                except FileNotFoundError:
                    print("File Not Found")
                else:
                    line_count:int=0
                    char_count:int=0
                    func_count:int=0
                    class_count:int=0

                     
                    for line in file:

                        for c in line:
                            char_count+=1
                        line = line.strip()
                        if line.startswith('def '):
                            func_count+=1
                        elif line.startswith('class '):
                            class_count+=1
                        line_count+=1
                file.close()

                self.files_summary[filename] = {'classes':class_count,'functions':func_count,'lines':line_count, 'chars':char_count}
        return self.files_summary




    def pretty_print(self) -> None:
        """ The values are fetched and print with pretty tables."""
        x: PrettyTable = PrettyTable()
        list_file:list = []
        list_classes:list = []
        list_functions:list = []
        list_lines:list = []
        list_characters:list = []
        for k,value in self.files_summary.items():
            list_classes.append(value["classes"])
            list_functions.append(value["functions"])
            list_lines.append(value["lines"])
            list_characters.append(value["chars"])
            list_file.append(k)
        x.add_column("Files",list_file)
        x.add_column("classes",list_classes)
        x.add_column("Functions",list_functions)
        x.add_column("Lines",list_lines)
        x.add_column("Characters",list_characters)
        print(x)
        
if __name__=="__main__":
    date_arithmetic()
    print(list(file_reader("test123.txt",3,sep="|", header=True)))
    f=FileAnalyzer("C:/Users/User/Desktop/Python/.vscode/Python")
    f.pretty_print()   
    