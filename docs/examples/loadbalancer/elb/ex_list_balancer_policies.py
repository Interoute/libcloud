from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

ACCESS_ID = 'your access id'
SECRET_KEY = 'your secret key'

cls = get_driver(Provider.ELB)
driver = cls(key=ACCESS_ID, secret=SECRET_KEY)

balancer = driver.list_balancers()[0]
policies = driver.ex_list_balancer_policies(balancer=balancer)

print(balancer)
print(policies)
