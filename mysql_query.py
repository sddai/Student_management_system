import pymysql



# 查询学生总人数
def select_student_total_people():
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT COUNT(*) FROM student_information'
    cursor.execute(sql)
    db.commit()
    Server_content =cursor.fetchall()
    # 将元组转换成列表
    Server_content_list = list(Server_content[0])[0]
    cursor.close()
    db.close()
    return Server_content_list


# 根据学号查询学生信息
def select_student_information(student_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT student_name, student_id, gender,birth,departments,address FROM `student_information` WHERE student_id = "{}"'.format(student_id)
    cursor.execute(sql)
    db.commit()
    server_content =cursor.fetchall()
    # 将元组转换成列表
    server_content_list = list(server_content)
    cursor.close()
    db.close()
    return server_content_list


# 查询所有学生信息展示
def select_student_all():
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT student_name, student_id, gender,birth,departments,address FROM `student_information`'
    cursor.execute(sql)
    db.commit()
    server_content =cursor.fetchall()
    # 将元组转换成列表
    server_content_list = list(server_content)
    cursor.close()
    db.close()
    return server_content_list


# 根据名字查询一个或者多个学生信息
def select_student_name(student_name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT student_name, student_id, gender,birth,departments,address FROM `student_information` WHERE student_name = "{}"'.format(student_name)
    cursor.execute(sql)
    db.commit()
    server_content =cursor.fetchall()
    student_list = list(server_content)
    return student_list


# 根据地区查询
def select_student_address(address):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT student_Name, student_id, gender,birth,departments,address FROM `student_information` WHERE address like "%{}%"'.format(
        address)
    cursor.execute(sql)
    db.commit()
    server_content = cursor.fetchall()
    student = list(server_content)
    return student


# 根据性别查询
def select_student_gender(gender):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT student_Name, student_id, gender,birth,departments,address FROM `student_information` WHERE gender = "{}"'.format(
        gender)
    cursor.execute(sql)
    db.commit()
    server_content = cursor.fetchall()
    student = list(server_content)
    return student


# 根据年龄查询
def select_student_age(age):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT student_Name, student_id, gender,birth,departments,address FROM `student_information` WHERE birth = 2019-"{}"'.format(
        age)
    cursor.execute(sql)
    db.commit()
    server_content = cursor.fetchall()
    student = list(server_content)
    return student


# 根据院系查询
def select_student_departments(departments):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT student_Name, student_id, gender,birth,departments,address FROM `student_information` WHERE departments = "{}"'.format(
        departments)
    cursor.execute(sql)
    db.commit()
    server_content = cursor.fetchall()
    student_list = list(server_content)
    return student_list


# 查询所有科目信息
def select_all_course_title():
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    # 获取结果为字典
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = 'SELECT course_title,course_id FROM `course`'
    cursor.execute(sql)
    db.commit()
    all_course = cursor.fetchall()
    all_course_list = list(all_course)
    cursor.close()
    db.close()
    return all_course_list


# 根据科目名字查询科目信息
def select_course_title(course_title):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT course_title,course_id FROM `course` where course_title = "{}"'.format(course_title)
    cursor.execute(sql)
    db.commit()
    course_content = cursor.fetchall()
    course_content_list = list(course_content)
    cursor.close()
    db.close()
    return course_content_list


# 根据课程名称查询课程编号
def select_course_title_id(course_title):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT course_id FROM `course` where course_title = "{}"'.format(course_title)
    cursor.execute(sql)
    db.commit()
    course_id = cursor.fetchall()
    try:
        course_id_list = list(course_id)[0]
        course_id_str = course_id_list[0]
    except:
        course_id_list = list(course_id)
        course_id_str = course_id_list
    cursor.close()
    db.close()
    return course_id_str


# 根据科目编号查询科目信息
def select_course_id(course_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT course_title,course_id FROM `course` where course_id = "{}"'.format(course_id)
    cursor.execute(sql)
    db.commit()
    course_content = cursor.fetchall()
    course_content_list = list(course_content)
    cursor.close()
    db.close()
    return course_content_list


# 查询所有成绩
def select_all_grade():
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'select student_information.student_name,student_information.student_id,course.course_title,grade_table.grade from student_information left join grade_table on student_information.student_id=grade_table.student_id left join  course on grade_table.course_id=course.course_id'
    cursor.execute(sql)
    db.commit()
    all_course = cursor.fetchall()
    # 讲遍历出的内容拼接成列表
    all_course_list = list(all_course)
    return all_course_list


# 根据学号查询学生成绩
def select_student_id_grade(student_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'select student_information.student_Name,student_information.student_id,course.course_title,grade_table.Grade from student_information left join grade_table on student_information.student_id=grade_table.student_id left join  course on grade_table.course_id=course.course_id WHERE student_information.Student_id = "{}"'.format(student_id)
    cursor.execute(sql)
    db.commit()
    student_content = cursor.fetchall()
    student_content_list = list(student_content)
    return student_content_list


# 根据学生姓名查询学生成绩
def select_student_name_grade(student_name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'select student_information.student_name,student_information.student_id,course.course_title,grade_table.grade from student_information left join grade_table on student_information.student_id=grade_table.student_id left join  course on grade_table.course_id=course.course_id WHERE student_information.student_Name = "{}"'.format(student_name)
    cursor.execute(sql)
    db.commit()
    student_content = cursor.fetchall()
    student_content_list = list(student_content)
    return student_content_list


# 根据学号和课程编号查询单一科目成绩唯一性
def select_grade_uniqu(student_id,course_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT * FROM grade_table WHERE student_id = "{}" and course_id = "{}"'.format(student_id,course_id)
    cursor.execute(sql)
    db.commit()
    grade_content = cursor.fetchall()
    grade_content_list = list(grade_content)
    return grade_content_list


# 利用学号连表查询获取两张表都存在的学号的信息
def select_synchronous(student_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT * FROM student_information JOIN grade_table on student_information.student_id=grade_table.student_id WHERE student_information.student_id = "{}"'.format(student_id)
    cursor.execute(sql)
    db.commit()
    grade_content = cursor.fetchall()
    grade_content_list = list(grade_content)
    return grade_content_list


# if __name__ == '__main__':
#     Select_Student_address('成都')

