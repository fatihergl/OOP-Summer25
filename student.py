students = [
 {
  first_name : "Fatih Murat"
last_name : "Ergul"
index_number : 35239
nationality : "Turkish"
starting_date : "2025-03-13"
courses : ["Object-oriented programing"] } ,





 {
    first_name : "akber"
last_name : "cavus"
index_number : 1111111
nationality : "Turkish"
starting_date : "2025-03-13"
courses :[ "Object-oriented programing"] 
} ,



 {
    first_name : "aslr"
last_name : "cakss"
index_number : 222222
nationality : "Turkish"
starting_date : "2025-03-13"
courses : ["Object-oriented programing"] }  ]


def add_student(first_name, last_name, index_number, nationalty, starting_date, courses):
    students.append({"first_name": first_name, "last_name": last_name, "index_number": index_number, "nationalty": nationalty, "startin_date": starting_date, "courses": courses})


def display_students():
    for student in students:
        print(student["first_name"], student["last_name"], "-", student["index_number"])


display_students()
print("\nAdding a new student...\n")
add_student("alex", "maxi", "112233")
display_students()
