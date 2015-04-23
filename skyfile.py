import core
from sky.api import permanent, ephemeral, infrastructure
from sky.networking import create_network, create_subnets

@infrastructure(environment='test', requires=['network', 'database', 'application', 'api', 'load_balancer'])
def cloud():
    print('make all')

@permanent
@infrastructure(environment='test')
def network():
    network = create_network(network_class='b', internet_connected=True)
    public_subnets = create_subnets(network, zones=['us-east-1b', 'us-east-1c'], byte_aligned=True, public=True)
    private_subnets = create_subnets(network, zones=['us-east-1b', 'us-east-1c'], byte_aligned=True)

@permanent
@infrastructure(environment='test', requires=['network'])
def database():
    print('make database')
    print('test', core.infrastructure['network'].resource['public_subnets'])

@ephemeral
@infrastructure(environment='test', requires=['network', 'database'])
def application():
    print('make application')

@ephemeral
@infrastructure(environment='test', requires=['network', 'application'])
def load_balancer():
    print('make load_balancer')

@ephemeral
@infrastructure(environment='test', requires=['network', 'database'])
def api():
    print('make api')
