'''
Write a function that takes hypervisor names as input (like "VMware ESXi", "KVM", "VirtualBox") and identifies whether it's Type 1 or Type 2 based on an internal dictionary.
'''

def hypervisor_type(name):
    types = {
        "VMware ESXi": "Type 1",
        "KVM": "Type 1",
        "Xen": "Type 1",
        "Microsoft Hyper-V": "Type 1",
        "VirtualBox": "Type 2",
        "VMware Workstation": "Type 2",
        "Parallels Desktop": "Type 2"
    }
    return types.get(name, "Unknown Hypervisor")

if __name__ == "__main__":
    name = input("Enter hypervisor name: ")
    print(f"{name} is {hypervisor_type(name)}")
