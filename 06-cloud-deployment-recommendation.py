'''
Write a Python program that takes user input (security level, budget, scalability need) and recommends the most suitable deployment model: Public, Private, or Hybrid.
'''

def recommend_deployment(security, budget, scalability):
    if security == "high" and budget == "high" and scalability == "high":
        return "Private Cloud is best for maximum security, control, and scalability."
    if security == "high" and budget == "high" and scalability == "medium":
        return "Private Cloud ensures high security and control with good scalability."
    if security == "high" and budget == "high" and scalability == "low":
        return "Private Cloud is ideal for high security, though scalability is limited."

    if security == "high" and budget == "medium" and scalability == "high":
        return "Hybrid Cloud balances security and scalability while managing costs."
    if security == "high" and budget == "medium" and scalability == "medium":
        return "Hybrid Cloud provides strong security with moderate cost efficiency."
    if security == "high" and budget == "medium" and scalability == "low":
        return "Hybrid Cloud is a secure option, but consider scaling limitations."

    if security == "high" and budget == "low" and scalability == "high":
        return "Hybrid Cloud is the only viable option, but security may be costly."
    if security == "high" and budget == "low" and scalability == "medium":
        return "Hybrid Cloud is recommended, but security features may be limited."
    if security == "high" and budget == "low" and scalability == "low":
        return "Private Cloud is best for security, but costs may be a concern."

    if security == "medium" and budget == "high" and scalability == "high":
        return "Hybrid Cloud allows flexibility while maintaining performance."
    if security == "medium" and budget == "high" and scalability == "medium":
        return "Hybrid Cloud gives balanced control and efficiency."
    if security == "medium" and budget == "high" and scalability == "low":
        return "Hybrid Cloud is ideal for stable workloads with lower scalability needs."

    if security == "medium" and budget == "medium" and scalability == "high":
        return "Hybrid Cloud is the best choice for a balanced approach."
    if security == "medium" and budget == "medium" and scalability == "medium":
        return "Hybrid Cloud provides a good balance of security, cost, and scalability."
    if security == "medium" and budget == "medium" and scalability == "low":
        return "Hybrid Cloud offers control and flexibility, but scaling may be limited."

    if security == "medium" and budget == "low" and scalability == "high":
        return "Public Cloud is the most affordable and scalable choice."
    if security == "medium" and budget == "low" and scalability == "medium":
        return "Public Cloud is cost-effective with moderate scalability."
    if security == "medium" and budget == "low" and scalability == "low":
        return "Public Cloud is budget-friendly but lacks advanced security."

    if security == "low" and budget == "high" and scalability == "high":
        return "Public Cloud provides the best performance for highly scalable applications."
    if security == "low" and budget == "high" and scalability == "medium":
        return "Public Cloud is a good option, offering flexibility and performance."
    if security == "low" and budget == "high" and scalability == "low":
        return "Public Cloud is suitable for cost-effective hosting."

    if security == "low" and budget == "medium" and scalability == "high":
        return "Public Cloud is the best scalable option with moderate costs."
    if security == "low" and budget == "medium" and scalability == "medium":
        return "Public Cloud is affordable and offers decent performance."
    if security == "low" and budget == "medium" and scalability == "low":
        return "Public Cloud is a simple and cost-effective choice."

    if security == "low" and budget == "low" and scalability == "high":
        return "Public Cloud is the only affordable and scalable solution."
    if security == "low" and budget == "low" and scalability == "medium":
        return "Public Cloud is cost-effective with moderate scaling potential."
    if security == "low" and budget == "low" and scalability == "low":
        return "Public Cloud is the best budget-friendly option but offers limited security."

    return "Hybrid Cloud is recommended for mixed or uncertain requirements."

if __name__ == "__main__":
    print("\nChoose from: low / medium / high")
    security = input("Enter security level: ").strip().lower()
    budget = input("Enter budget: ").strip().lower()
    scalability = input("Enter scalability need: ").strip().lower()

    print("\nBest Cloud Deployment Model:")
    print(recommend_deployment(security, budget, scalability))
