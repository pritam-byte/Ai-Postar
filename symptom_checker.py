def check_symptoms():
    print("\n--- Symptom Checker ---")
    symptoms_db = {
        "fever": "Flu or Viral Infection",
        "cough": "Common Cold or COVID-19",
        "chest pain": "Heart Disease or Anxiety",
        "headache": "Migraine or Dehydration",
        "rash": "Allergy or Skin Infection"
    }

    symptoms = input("Enter symptoms separated by commas: ").lower().split(',')
    predictions = set()

    for s in symptoms:
        s = s.strip()
        if s in symptoms_db:
            predictions.add(symptoms_db[s])

    if predictions:
        print("Possible illnesses:", ", ".join(predictions))
    else:
        print("No matching illnesses found. Please consult a doctor.")
