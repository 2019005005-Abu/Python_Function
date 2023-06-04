from functools import reduce
def add(first,last):
    return first+last
print(add(100,200));

add1=add(100,300);
print(add1)
add2=add(-400,-900);
print(add2);

n=[100,200,300];
print(100  in n);
print(200 is n);

def signal(flag):
    if (flag=='Green'):
        return ("Proceed");
    elif (flag=='yellow'):
        return ("wait");
    else:
        return ("Stop");
Signal_mode=signal("Green");
print(Signal_mode);

##Arguments
'''
1.Positional  Arguments
2.Keyword Arguments
3.
4.
'''
##Position Arguments
def students(firstName,lastName,SI,Year):
    print("My FirstName is",firstName);
    print("My LastName is",lastName);
    print("System Id",SI);
    print("I am working",Year); 
allData=students("Abu Al Shahriar","Rifat",2019005005,2023);
print(allData);

'''
Mathematice Function
'''
def add(a,b):return a+b;
print(add(100,200));
def multiple_three(a,b,c):return a+b+c;
print(multiple_three(100,200,300));
def misc(a,b,c):return a+b+c;
print(misc(-100,-300,67));
def addition(*args):
    return sum(args);
print(addition(1,2,3,4,5,6));

def add2(*args):
    return  sum(args);
print(add2(100,34,50))

def addition1(**kwards):
    print(kwards);
    print(type(kwards));
    print(kwards.items)
addition1(a=1,b=2,c=3);

def sample1(a,b,c):
    print(a);
    print(b);
    print(c);
var_1=(1,2,3);
sample1(*var_1);

def add1(a,b,c,d):
    print('a--',a);
    print('b--',b);
    print('c--',c);
    print('d--',d);
    return sum(var);
var=(1,2,3,4);
add1(*var);

def sample2(a,b,c):
    print(a);
    print(b);
    print(c);
var3={'a':'apple','b':'ball','c':'cat'}
sample2(**var3);

def sample3(a,b,c,d):
    print(a);
    print(b);
    print(c);
    print(d);
var4=(10,20,30,40);
sample3(*var4);

def sample4(a,b,c,d,e,f,g):
    print('a--',a);
    print('args--',args);
    print('d--',d,'e--',e);
    print('kwargs--',kwargs);

args=(3,4);
kwargs={'f':45,'g':67};
sample4(1,*args,d=12,e=13,**kwargs);

##Lamda Function
#which function has no name that is Called Lamda Function
adding_lamda=lambda x,y:x+y;
print(adding_lamda(100,200))
subtraction_lamda=lambda x1,y1:x1-y1;
print(subtraction_lamda);
multiple_lamda=lambda x2,y2:x2*y2;
print(multiple_lamda(100,2))
division_lamda=lambda x3,y3:x3/y3;
print(division_lamda(100,2))

list_1=[1,2,3,4,5];
list_2=[4,5,6,7];
mapping1=list(map(lambda x,y:x+y,list_1,list_2));
print(mapping1);
reducing1=reduce(lambda x,y:x+y,list_1);
print(reducing1);
reducing2=reduce(lambda x,y: x if x>y else y,list_2);
print(reducing2);
filter1=filter(lambda x:x%2==0,[1,3,5,7,9,11]);
print(filter1);








