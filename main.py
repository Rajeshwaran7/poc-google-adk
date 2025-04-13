from multi_tool_agent.agent import root_agent

def main():
    print("Financial Assistant Agent is running!")
    
    # Example of using the agent
    print("\nExample mortgage calculation:")
    response = root_agent.generate(
        messages=[
            {"role": "user", "content": "Calculate monthly payment for a $300,000 loan with 4.5% interest over 30 years"}
        ]
    )
    print(response.text)
    
    print("\nExample currency conversion:")
    response = root_agent.generate(
        messages=[
            {"role": "user", "content": "Convert 100 USD to EUR"}
        ]
    )
    print(response.text)


if __name__ == "__main__":
    main()
