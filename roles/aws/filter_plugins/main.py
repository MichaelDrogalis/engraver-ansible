import boto.ec2

def aws_nodes(name, role, aws_region):
  ips = []
  conn = boto.ec2.connect_to_region(aws_region)

  for r in conn.get_all_reservations():
    for i in r.instances:
      if (i.tags.get("Name") == name) and (i.state == "running"):
        if i.tags.get("Role") == role:
          ips.append(i.ip_address)
  return ips

class FilterModule(object):
    ''' Ansible jinja2 filters '''

    def filters(self):
      return {
        'aws_nodes': aws_nodes,
      }
