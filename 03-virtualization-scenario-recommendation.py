class Virtualization:
    benefits = ["Cost efficiency", "Scalability", "Resource optimization"]
    drawbacks = ["Performance overhead", "Security risks", "Complexity"]

    @staticmethod
    def list_benefits():
        return Virtualization.benefits

    @staticmethod
    def list_drawbacks():
        return Virtualization.drawbacks

    @staticmethod
    def suggest(scenario):
        scenario = scenario.lower()
        if "cost" in scenario:
            return "Virtualization is beneficial for cost savings."
        if "performance" in scenario:
            return "Virtualization may not be ideal due to overhead."
        if "scalability" in scenario:
            return "Virtualization is a good choice for scaling resources."
        if "security" in scenario:
            return "Virtualization may introduce security risks."
        if "hardware" in scenario:
            return "Virtualization reduces dependency on physical hardware."
        return "Depends on the specific use case."

if __name__ == "__main__":
    print("Benefits:", Virtualization.list_benefits())
    print("Drawbacks:", Virtualization.list_drawbacks())

    print("\nExample scenarios you can type:")
    print("- I want to reduce infrastructure cost.")
    print("- I need better scalability.")
    print("- I want to maximize performance.")
    print("- I have security concerns.")
    print("- I want to minimize hardware usage.")

    scenario = input("\nEnter your scenario: ")
    print(Virtualization.suggest(scenario))
