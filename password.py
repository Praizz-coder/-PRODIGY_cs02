import re


def check_password_strength(password):
    # Define the criteria
    criteria = {
        "length": len(password) >= 12,  # Length criteria is now 12 for "Very Strong"
        "lowercase": re.search(r"[a-z]", password) is not None,
        "uppercase": re.search(r"[A-Z]", password) is not None,
        "digit": re.search(r"\d", password) is not None,
        "special_char": re.search(r"[!@#$%^&*(),.?\":{}|<>" "]", password) is not None
    }

    # Calculate strength score
    strength_score = sum(criteria.values())

    # Feedback messages
    feedback = []

    if not criteria["length"]:
        feedback.append("Your password should be at least 12 characters long.")
    if not criteria["lowercase"]:
        feedback.append("Add at least one lowercase letter.")
    if not criteria["uppercase"]:
        feedback.append("Add at least one uppercase letter.")
    if not criteria["digit"]:
        feedback.append("Include at least one digit.")
    if not criteria["special_char"]:
        feedback.append("Add at least one special character (e.g., @, #, $, etc.).")

    # Evaluate password strength based on score
    if strength_score == 5:
        return "Very Strong Password", feedback
    elif strength_score == 4:
        return "Strong Password", feedback
    elif strength_score == 3:
        return "Moderate Password", feedback
    else:
        return "Weak Password", feedback


def password_strength_feedback(password):
    # Evaluate the password
    strength, feedback = check_password_strength(password)

    # Print results
    print(f"Password Strength: {strength}")

    if feedback:
        print("\nSuggestions for Improvement:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    else:
        print("Great job! Your password is secure.")


# Example usage
password = input("Enter a password: ")
password_strength_feedback(password)