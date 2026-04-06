# 5_func.py

def print_info(name, phone, address, email):
    contact_info = f"연락처:\t{phone}\n이메일:/t{email}"
    return f"이름:\t{name}\n{contact_info}\n주소:\t{address}"

def print_info(name, phone, address, email=""):
    contact_info = f"연락처:\t{phone}\n이메일:\t{email}"
    print(f"이름:\t{name}\n{contact_info}\n주소:\t{address}")

print_info("이강혁", "010-4568-4435", "청주")
person = return_info(
    email="rhdrur44018@a.ut.ac.kr", phone="010-4568-4435",
    address="국립한국교통대학교", name="이강혁"
    )
print(person)