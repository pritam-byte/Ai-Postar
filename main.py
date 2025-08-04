from symptom_checker import check_symptoms
from image_analyzer import classify_xray
from health_chatbot import health_assistant

def main():
    print("\n--- AI in Healthcare Demo ---")
    while True:
        print("\n1. Symptom-based Prediction")
        print("2. Chest X-ray Classification")
        print("3. Voice-based Health Chatbot")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            check_symptoms()
        elif choice == '2':
            classify_xray()
        elif choice == '3':
            health_assistant()
        elif choice == '4':
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
