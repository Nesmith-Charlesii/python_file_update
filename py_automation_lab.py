allow_list_txt = "allow_ip_list.txt"
remove_list_txt = "remove_ip_list.txt"

with open(allow_list_txt, "r") as file:
    allow_ip_list = file.read()

with open(remove_list_txt, "r") as file:
    remove_ip_list = file.read()

def remove_new_line(string):
    return string.replace("\n", "")

cleaned_remove_list = remove_new_line(remove_ip_list)

allow_ip_list = allow_ip_list.split()
cleaned_remove_list = cleaned_remove_list.split(",")

for ip in allow_ip_list:
    if ip in cleaned_remove_list:
        allow_ip_list.remove(ip)

allow_ip_list = " ".join(allow_ip_list)

with open(allow_list_txt, "w") as file:
    file.write(allow_ip_list)

with open(allow_list_txt, "r") as file:
    updated_ip_list = file.read()

print(updated_ip_list)