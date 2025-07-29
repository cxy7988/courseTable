from data import AppleMaps, Course, Geo, School, Weeks


school = School(
    duration=75,   # 每节课时间为 45 分钟
    timetable=[
        (8, 30),   # 上午第一节课时间为 8:30 至 9:15
        (10, 00),
        (11, 30),
        (13, 00),
        (14, 30),
        (16, 00),
        (17, 30),
        (19, 00),
    ],
    start=(2025, 9, 1),  # 开学第一周当周周一至周日以内的任意日期
    courses=[
        Course(
            name="MGS4998*02",
            teacher="Kashif Ullah Khan",
            classroom="CBPM C226",
            location=None,     # Apple Maps 实例
            weekday=2,
            weeks=Weeks(1, 16) ,        # 数字数组拼合
            indexes=[2],
        ),

        Course(
            name="MGS4998*02",
            teacher="Kashif Ullah Khan",
            classroom="TCBPM C226",
            location=None,     # Apple Maps 实例
            weekday=4,
            weeks=Weeks(1, 16) ,        # 数字数组拼合
            indexes=[2],                 # 等价于 [9, 10, 11]
        ),

        Course(
            "CPS2232*10",
            "Hemn B. Abdalla",
            "TBD",
            None,
            1,
            Weeks(1, 16),
            [6],
        ),

        Course(
            "CPS2232*10",
            "Hemn B. Abdalla",
            "TBD",
            None,
            3,
            Weeks(1, 16),
            [6],
        ),

        Course(
            "CPS4982*02",
            "Yue Zhao",
            "GHK C103",
            None,
            2,
            Weeks(1, 16),
            [6],
        ),

        Course(
            "CPS4982*02",
            "Yue Zhao",
            "GHK C103",
            None,
            4,
            Weeks(1, 16),
            [6],
        ),


        Course(
            "MGS3520*01",
            "Ying Liu",
            "CBPM A201",
            None,
            2,
            Weeks(1, 16),
            [8],
        ),

        Course(
            "MGS3520*01",
            "Ying Liu",
            "CBPM A201",
            None,
            4,
            Weeks(1, 16),
            [8],
        ),

        Course(
            "MGS4701*01",
            "Chungil Chae",
            "CBPM A203",
            None,
            2,
            Weeks(1, 16),
            [7],
        ),

        Course(
            "MGS4701*01",
            "Chungil Chae",
            "CBPM A203",
            None,
            4,
            Weeks(1, 16),
            [7],
        ),

        Course(
            "MATH3700*02",
            "Guanchao Tong",
            "CSMT 208",
            None,
            2,
            Weeks(1, 16),
            [4],
        ),
        
        Course(
            "MATH3700*02",
            "Guanchao Tong",
            "CSMT 208",
            None,
            4,
            Weeks(1, 16),
            [4],
        ),
    ],
)

# 生成ics格式的课表文件
with open("课表.ics", "w", encoding = "utf-8") as w:
    w.write(school.generate())

# 生成CSV格式的课表文件
csv_filename = school.generate_csv("课表.csv")
print(f"课表已生成:")
print(f"- ICS格式: 课表.ics")
print(f"- CSV格式: {csv_filename}")
