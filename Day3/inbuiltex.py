# Print function
print("Hello, DevOps Engineers!")

# Input function
user_name = input("Enter your name: ")
print(f"Welcome, {user_name}!")

# Type Conversion Example
num_str = "100"
num_int = int(num_str)  # Convert string to integer
num_float = float(num_int)  # Convert integer to float

print(type(num_str), type(num_int), type(num_float))  # <class 'str'> <class 'int'> <class 'float'>


# Math functions
print(abs(-10))   # 10
print(pow(2, 3))  # 8
print(round(3.14159, 2))  # 3.14
print(min(10, 5, 20))  # 5
print(max(10, 5, 20))  # 20
print(sum([1, 2, 3, 4, 5]))  # 15

#String Functions
text = " DevOps Automation "
print(len(text))  # 18
print(text.lower())  # " devops automation "
print(text.upper())  # " DEVOPS AUTOMATION "
print(text.strip())  # "DevOps Automation"
print(text.replace("DevOps", "Cloud"))  # " Cloud Automation "
print(text.split())  # ['DevOps', 'Automation']


#List Functions
tools = ["Terraform", "Ansible", "Docker", "Kubernetes"]
print(len(tools))  # 4
tools.append("Jenkins")
print(tools)  # ['Terraform', 'Ansible', 'Docker', 'Kubernetes', 'Jenkins']
tools.pop()
print(tools)  # ['Terraform', 'Ansible', 'Docker', 'Kubernetes']
tools.sort()
print(tools)  # ['Ansible', 'Docker', 'Kubernetes', 'Terraform'] #arrange the list alphabetically
tools.reverse()
print(tools)  # ['Terraform', 'Kubernetes', 'Docker', 'Ansible'] #arrange the list reverse order.


# Dictionary Functions
devops_tools = {"CI/CD": "Jenkins", "Containerization": "Docker", "Orchestration": "Kubernetes"}

print(devops_tools.keys())  # dict_keys(['CI/CD', 'Containerization', 'Orchestration'])
print(devops_tools.values())  # dict_values(['Jenkins', 'Docker', 'Kubernetes'])
print(devops_tools.get("CI/CD"))  # Jenkins
devops_tools.pop("CI/CD")
print(devops_tools)  # {'Containerization': 'Docker', 'Orchestration': 'Kubernetes'}
