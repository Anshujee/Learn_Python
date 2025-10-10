import sys

instance_type = sys.argv[1]

if instance_type == 't2.micro':
    print("We will create a t2.micro instance")
elif instance_type == 't2.small':
    print("We will create a t2.small instance")
elif instance_type == 't2.medium':
    print("We will not alloed to create a t2.medium instance")
elif instance_type == 't2.large':
    print("We will not alloed to create a t2.large instance")
else:
    print("Please provide a valid instance type")
