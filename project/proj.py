import mysql.connector as mconn
import numpy as np
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model  import LinearRegression
import matplotlib.pyplot as plt


def preger(a1,a2):
    a1=np.array(a1)
    a2=np.array(a2)
    a2=a2.reshape(-1,1)
    a1=a1.reshape(-1,1)
    mode=[[1,1/x,1/(x*x)] for x in a1]
    #print(mode)
    model=LinearRegression()
    model.fit(mode,a2)
    a=[]
    a=list(model.intercept_)
    a.extend(model.coef_[0][1:])
    #b=[a[0]+a[1]/x+a[2]/(x*x) for x in range(10,100)]
    #plt.scatter([x for x in range(10,100)],b,color='g')
    return a

def pred_price(d,n,p0,ca):
    p=[x for x in range(1,3*p0)]
    a=[]
    b=[]
    for x in p:
        temp=profit(x,d,n,p0,ca)
        a.append(temp[0])
        b.append(temp[1])
    return p[a.index(max(a))],max(a),b[a.index(max(a))]
    #return ((4*(coeff_arr[1])**2-12*coeff_arr[0]*coeff_arr[2]))/(6*coeff_arr[0])

def profit(p,d,n,p0,ca):
    if d*(ca[0]+ca[1]/p+ca[2]/(p*p))>n:
        #print(d*(ca[0]+ca[1]*p+ca[2]*p*p))
        #print(d*n*p-n*p0)
        return [n*p-n*p0,n]
#    print(ca[0]+ca[1]/p+ca[2]/(p*p)*d)
    return [d*(ca[0]+ca[1]/p+ca[2]/(p*p))*p-n*p0 , d*(ca[0]+ca[1]/p+ca[2]/(p*p))]
    
    
mydb=mconn.connect(host="localhost",user="root",passwd="")
cur=mydb.cursor()

#cur.execute("show databases")
#for i in cur:
#    print(i)
cur.execute("use myproject")
#cur2.execute("use myproject")
cur.execute("select * from ml_table")
array11=[]
array12=[]
array21=[]
array22=[]
array31=[]
srray11=[]
srray12=[]
srray21=[]
srray22=[]
srray31=[]
for i in cur:
    if i[0]==1 and i[1]=='i1':
        array11.append(i[2])
        srray11.append(i[3])
    if i[0]==1 and i[1]=='i2':
        array12.append(i[2])
        srray12.append(i[3])
    if i[0]==2 and i[1]=='i1':
        array21.append(i[2])
        srray21.append(i[3])
    if i[0]==2 and i[1]=='i2':
        array22.append(i[2])
        srray22.append(i[3])
    if i[0]==3 and i[1]=='i1':
        array31.append(i[2])
        srray31.append(i[3])

n=[]
d=[]
p0=[]
cur.execute("select * from item_info")
ans=[]
ans1=[]
for i in cur:
    n=[]
    d=[]
    p0=[]
    if i[0]==1 and i[1]=='i1':
        n.append(i[2])
        d.append(i[4])
        p0.append(i[3])
        pred=preger(array11,srray11)
        p=pred_price(d[0],n[0],p0[0],pred)
        sql="update item_info set curr_price={} where shop_id ='1' and item_id='i1' ".format(p[0])
        #cur2.execute(sql)
        ans.append(p[0])
        ans1.append(sql)

        
    if i[0]==1 and i[1]=='i2':
        n.append(i[2])
        d.append(i[4])
        p0.append(i[3])
        pred=preger(array12,srray12)
        p=pred_price(d[0],n[0],p0[0],pred)
        
        sql="update item_info set curr_price={} where shop_id ='1' and item_id='i2' ".format(p[0])
        #cur2.execute(sql)
        ans.append(p[0])
        ans1.append(sql)
    if i[0]==2 and i[1]=='i1':
        n.append(i[2])
        d.append(i[4])
        p0.append(i[3])
        pred=preger(array21,srray21)
        p=pred_price(d[0],n[0],p0[0],pred)
        sql="update item_info set curr_price={} where shop_id ='2' and item_id='i1' ".format(p[0])
        #cur2.execute(sql)
        ans.append(p[0])
        ans1.append(sql)
    if i[0]==2 and i[1]=='i2':
        n.append(i[2])
        d.append(i[4])
        p0.append(i[3])
        pred=preger(array22,srray22)
        p=pred_price(d[0],n[0],p0[0],pred)
        #cur2=mydb.cursor(buffered=True)
        #cur2.execute("use myproject")
        sql="update item_info set curr_price={} where shop_id ='2' and item_id='i2' ".format(p[0])
        #cur2.execute(sql)
        ans.append(p[0])
        ans1.append(sql)
    if i[0]==3 and i[1]=='i1':
        n.append(i[2])
        d.append(i[4])
        p0.append(i[3])
        pred=preger(array31,srray31)
        p=pred_price(d[0],n[0],p0[0],pred)
        sql="update item_info set curr_price={} where shop_id ='3' and item_id='i1' ".format(p[0])
        #cur2.execute(sql)
        ans.append(p[0])
        ans1.append(sql)
'''
print(pred_price(100,100,20,pred))
val=1
sql="update item_info set item_id = 'rahul' where shop_id = {}".format(val)
        
cur.execute(sql)

cur.execute("select * from item_info")
for i in cur:
    print(i)
cur.execute ("""
   UPDATE item_info
   SET item_id="rhul"
   where shop_id=1
""")
cur.execute("select * from item_info")
for i in cur:
    print(i)
'''
for i in ans1:
    cur.execute(i)

mydb.commit()
mydb.close()



