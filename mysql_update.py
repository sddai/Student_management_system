import pymysql

# 根据学号更改学号
def Update_Student_id(Student_id,New_Student_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'UPDATE `Student_information` set Student_id = "{b}" where Student_id = "{a}"'.format(a=Student_id, b=New_Student_id)
    print(sql)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print('修改'+ Student_id + '学号成功')

# 根据学号更改姓名
def Update_Student_name(Student_id,New_Student_name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'UPDATE `Student_information` set Student_name = "{b}" where Student_id = "{a}"'.format(a=Student_id, b=New_Student_name)
    print(sql)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print('学号:'+ Student_id + '姓名修改成功')


# 根据学号更改性别
def Update_Gender(Student_id,New_Gender):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'UPDATE `Student_information` set Gender = "{b}" where Student_id = "{a}"'.format(a=Student_id, b=New_Gender)
    print(sql)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print('学号:'+ Student_id + '性别修改成功')

# 根据课程名称更改课程名称
def Update_Course_title(Course_title,New_Course_title):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'UPDATE `subjectinfo` set  Course_title= "{b}" where Course_title = "{a}"'.format(a=Course_title, b=New_Course_title)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print('科目:'+ Course_title + '修改成功')

# 根据课程编号更改课程编号
def Update_Course_id(Course_id, New_Course_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'UPDATE `subjectinfo` set  Course_id= "{b}" where Course_id = "{a}"'.format(a=Course_id,
                                                                                            b=New_Course_id)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print('科目:' + Course_id + '修改成功')



#根据学号修改成绩表学号
def Update_Grade_student_id(Student_id,New_Student_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'UPDATE `grade_table` set  Student_id= "{b}" where Student_id = "{a}"'.format(a=Student_id, b=New_Student_id)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print('学号'+ Student_id + '修改成功')


# 根据学号在成绩表修改课程编号
def Update_Grade_course_id(Student_id, New_Course_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'UPDATE `grade_table` set  Course_id= "{b}" where Student_id = "{a}"'.format(a=Student_id, b=New_Course_id)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print('科目编号' + Student_id + '修改成功')


# 根据学号修改成绩表成绩
def Update_Grade_grade(Student_id, New_Grade):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'UPDATE `grade_table` set  Grade = "{b}" where Student_id = "{a}"'.format(a=Student_id, b=New_Grade)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print('成绩' + Student_id + '修改成功')