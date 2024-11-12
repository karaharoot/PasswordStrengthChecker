Password Strength Checker created by Harout Karakossian

This password strength checker is a Python program that evaluates the strength of a user-provided password based on several security criteria. It provides a score out of 10, along with suggestions to improve the password’s strength if necessary. The program is ideal for helping users create secure passwords by emphasizing length, character diversity, and avoiding common weaknesses.

Features

- Scoring System: The password is evaluated on a 10-point scale, with higher scores indicating stronger passwords.
- Strength Criteria:
  - Length (up to 2 points): Longer passwords get more points.
  - Character Diversity (4 points): Uses a mix of uppercase letters, lowercase letters, numbers, and special characters.
  - Avoiding Common Patterns (2 points): Deducts points if the password contains dictionary words or keyboard patterns.
  - Repetition and Sequence Check (2 points): Deducts points if the password has repetitive or sequential characters.
- Feedback: If the password is weak in any area, suggestions are provided for improvement.

Requirements

- Python 3.x
- re module (Python standard library)

Usage

1. Run the Program: Open a terminal or command prompt.
2. Enter Password: Run the script and input a password when prompted.
3. View Results: The program outputs the password's score and any suggestions for strengthening it.

Example Output

Enter your password to check its strength: Tac0Truck!
Password Score: 8/10 (Strong)
Your password is strong!


Code Walkthrough

1. Imports and Setup:
   - The re module is used for regular expression checks, which helps identify the presence of different character types in the password.

2. Function: check_password_strength(password)
   - The function takes a single argument, password, which is the password the user wants to evaluate.

3. Scoring Criteria:
   - Length Check: Adds 1 point if the password has at least 8 characters and another point if it has more than 12 characters.
   - Character Variety Check: Uses regular expressions to check for uppercase letters, lowercase letters, digits, and special characters. Each criterion met adds 1 point to the score.
   - Pattern Avoidance: Checks if the password contains any common weak patterns (like "password" or "12345"). If none of these patterns are found, it adds 1 point.
   - Repetition and Sequence Check: Checks for repeated characters (e.g., "aaaa") or sequences (e.g., "1234" or "abcd"). If these are avoided, the password gains additional points.

4. Strength Levels:
   - Based on the score, the program assigns a descriptive strength level: "Very Strong," "Strong," "Moderate," "Weak," or "Very Weak."

5. Feedback:
   - If any of the criteria are not met, the program provides specific suggestions to help the user improve their password strength.

6. Final Output:
   - The program prints the final score (out of 10) and displays the password's strength level along with any recommendations.

This structure makes the program easy to understand and use, helping users quickly identify weaknesses in their password choices and to create a more secure password.
