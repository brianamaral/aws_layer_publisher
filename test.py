from boto3.session import Session

session = Session()

for region in session.get_available_regions("lambda"):
    print(region)
