def get_course_info(courses_file_path, schedule_file_path, course_name):
    coursefile = open(courses_file_path, 'r', encoding='utf8')
    schedulefile = open(schedule_file_path, 'r', encoding='utf8')
    courseinfo = []
    for line in coursefile:
        if course_name in line:
            url = f'{line[len(course_name)+2:]}'.strip()
            courseinfo.append(url)
    for line in schedulefile:
        if course_name in line:
            startdata = f'{line[len(course_name) + 2:]}'.strip()
            courseinfo.append(startdata)
    return courseinfo
print(get_course_info('courses.txt', 'schedule (1).txt', "FullStack Developer"))
















