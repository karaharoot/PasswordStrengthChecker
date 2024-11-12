import re

def check_password_strength(password):
    score = 0
    strength_feedback = []

    if len(password) >= 8:
        score += 1
        if len(password) > 12:
            score += 1
    else:
        strength_feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        strength_feedback.append("Add uppercase letters for a stronger password.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        strength_feedback.append("Add lowercase letters for a stronger password.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        strength_feedback.append("Add numbers to strengthen your password.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        strength_feedback.append("Add special characters (e.g., !, @, #) for better security.")

    common_patterns = ["password", "12345", "qwerty", "letmein"]
    if not any(pattern in password.lower() for pattern in common_patterns):
        score += 1
    else:
        strength_feedback.append("Avoid common phrases or patterns (e.g., 'password', '12345').")

    if not re.search(r"(.)\1{2,}", password):
        score += 1
    else:
        strength_feedback.append("Avoid using the same character repeatedly.")

    if not re.search(r"(012|123|234|345|456|567|678|789|abc|bcd|cde|def)", password.lower()):
        score += 1
    else:
        strength_feedback.append("Avoid sequential characters or simple patterns (e.g., 'abcd', '1234').")

    strength_levels = {
        range(9, 11): "Very Strong",
        range(7, 9): "Strong",
        range(5, 7): "Moderate",
        range(3, 5): "Weak",
        range(0, 3): "Very Weak"
    }
    
    password_strength = next((level for range_, level in strength_levels.items() if score in range_), "Very Weak")

    print(f"Password Score: {score}/10 ({password_strength})")
    if strength_feedback:
        print("Suggestions to improve password strength:")
        for suggestion in strength_feedback:
            print(f"- {suggestion}")
    else:
        print("Your password is strong!")

    return password_strength

password = input("Enter a password to check its strength: ")
check_password_strength(password)
