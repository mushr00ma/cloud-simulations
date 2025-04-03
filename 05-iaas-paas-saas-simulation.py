'''
Simulate user interaction with IaaS, PaaS, and SaaS layers using Python classes. Show how each model abstracts infrastructure differently with practical examples (e.g., hosting a web app).
'''

class IaaS:
    def __init__(self):
        self.instances = []

    def provision_vm(self, name, os_type):
        self.instances.append((name, os_type))
        return f"Provisioned VM: {name} with {os_type}"

    def list_vms(self):
        return f"IaaS Instances: {', '.join(f'{name} ({os})' for name, os in self.instances) if self.instances else 'None'}"


class PaaS:
    def __init__(self):
        self.apps = []

    def deploy_app(self, app_name, runtime):
        self.apps.append((app_name, runtime))
        return f"Deployed {app_name} using {runtime} on PaaS"

    def list_apps(self):
        return f"PaaS Applications: {', '.join(f'{app} ({runtime})' for app, runtime in self.apps) if self.apps else 'None'}"


class SaaS:
    def __init__(self):
        self.services = {"Google Docs": "Document Editing", "Dropbox": "Cloud Storage", "Salesforce": "CRM"}

    def use_service(self, service_name):
        return f"Using {service_name}: {self.services.get(service_name, 'Service not available')}"

    def list_services(self):
        return f"Available SaaS Services: {', '.join(self.services.keys())}"


if __name__ == "__main__":
    iaas = IaaS()
    paas = PaaS()
    saas = SaaS()

    print(iaas.provision_vm("Ubuntu-Server", "Linux"))
    print(iaas.provision_vm("Windows-VM", "Windows"))
    print(iaas.list_vms())

    print(paas.deploy_app("WebApp", "Python Flask"))
    print(paas.deploy_app("DataProcessor", "Node.js"))
    print(paas.list_apps())

    print(saas.use_service("Google Docs"))
    print(saas.use_service("Slack"))
    print(saas.list_services())
