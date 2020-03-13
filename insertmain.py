import cx_Oracle

filename='222.csv'
fileobj = open(filename, mode='rb')
head = fileobj.readline().strip().decode('utf-8')
#此处需要读取文件头一共几个
nextline = fileobj.readline().strip().decode('utf-8')


while len(nextline) > 0:
    rlis=[]
    lis=[]
    datalist = nextline.split(',')
    for i in range(31):
        if datalist[i].replace('"','')=='':
            rlis.append('999')
        else:
            rlis.append(datalist[i].replace('"',''))
        pass
    rlis=tuple(rlis)
    nextline = fileobj.readline().strip().decode('utf-8')
    #print(rlis)
    lis.append(rlis)
    orcConfig ='nwom/nwom@10.18.12.22:1521/nwom'
    conn = cx_Oracle.connect(orcConfig)
    cursor = conn.cursor()
    sql="insert into SS_ANALYSIS_CELL_TS VALUES(:a,:b,:c,:d,:e,:f,:g,:h,:TO_DATE(:i,'YYYY-MM-DD'),:TO_DATE(:j,'YYYY-MM-DD'),:k,:l,:m,:n,:o,:p,:q,:r,:s,:t,:u,:v,:w,:x,:y,:z,:a1,:a2,:a3,:a4,:a5)"
    cursor.prepare(sql)
    cursor.executemany(None,lis)
    conn.commit()
    cursor.close()
    conn.close()
    print("插入成功了")

fileobj.close()

# liss=[]
# for i in range(10000):
#     liss.append(('3'))
#     pass
