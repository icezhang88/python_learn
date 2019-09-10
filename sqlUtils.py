import pymysql
import json


edge_config={
    "host": "192.168.1.240",
    "user": "root",
    "password": "qhlk@2017",
    "database": "itsu_dev"
}


def selectData(table):

    db=pymysql.connect(**edge_config)
    cursor=db.cursor()
    cursor.execute("select * from  "+table)
    data=cursor.fetchall()
    cursor.close()
    db.close()
    return data



def selectAllTableData():
    tables=["equipment","equipment_info","equipments_attr","group_control","point","point_info","prediction_rule_table","section"];
    for table in tables:
        data = selectData(table)
        for item in data:
            jsonData={"table":table,"host":"host","data":data}
            print(str(json.dumps(jsonData).encode("utf-8")))



if __name__ == '__main__':
    selectAllTableData()






