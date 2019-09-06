import pymysql

edge_config={
    "host": "192.168.1.240",
    "user": "root",
    "password": "qhlk@2017",
    "database": "itsu_dev"
}

cloud_config={
    "host": "192.168.1.240",
    "user": "root",
    "password": "qhlk@2017",
    "database": "hjcloud_cloud"
}

def selectData(table):

    db=pymysql.connect(**edge_config)
    cursor=db.cursor()
    cursor.execute("select * from  "+table)
    data=cursor.fetchall()
    cursor.close()
    db.close()
    return data
def insertData(data,table):

    if table=="equipment":
        sql="insert into equipment values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)";
    elif table=="equipment_info":
        sql="insert into equipment_info values(%s,%s,%s,%s,%s,%s,%s)";
    elif table=="equipments_attr":
        sql = "insert into equipments_attr values (%s,%s,%s,%s,%s,%s,%s)";
    elif table=="group_control":
        sql = "insert into group_control values (%s,%s,%s,%s,%s,%s,%s,%s)";
    elif table=="point":
        sql = "insert into point values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)";
    elif table=="point_info":
        sql = "insert into point_info values(%s,%s,%s,%s)";
    elif table == "prediction_rule_table":
        sql = "insert into prediction_rule_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)";
    elif table == "section":
        sql = "insert into  section values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'2',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ";
    else:
        pass


    print(data)
    try:
        db=pymysql.connect(**cloud_config)
        cursor=db.cursor()
        print(sql)
        cursor.execute(sql,data)
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        print("error:======>"+str(e)




              )


if __name__ == '__main__':
    tables=["equipment","equipment_info","equipments_attr","group_control","point","point_info","prediction_rule_table","section"];
    for table in tables:
        data = selectData(table)
        for item in data:
            insertData(item,table)




