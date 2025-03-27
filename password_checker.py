def check_password(password):
      #Function to check password strength based on simple rules

  if len(password) < 8:
      return " Weak Password! Must be at least 8 characters long."

  if password.isdigit() or password.islower() or password.isupper():
      return "Medium Password. Try using a mix of uppercase, lowercase, and numbers."

  return " Strong Password! ✅"

def main():
  #Main function to take user input and check password strength
  print("🔍 Simple Password Strength Checker 🔍")

  password = input("Enter your password: ")  # Take password input
  result = check_password(password)  # Check strength
  print("\n" + result)  # Display result

if __name__ == "__main__":
  main()  # Run the program