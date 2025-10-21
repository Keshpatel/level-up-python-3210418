import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards


# creating idetify_palindrome(text) function 

def idetify_palindrome(textValue):
    print(f"\n🔍 Checking text: '{textValue}'")
    
    # Step 1 - Convert to lowercase
    lower_text = textValue.lower()
    print(f"Step 1 - Lowercase: {lower_text}")
    
    # Step 2 - Remove all non-alphanumeric characters
    cleaned = re.sub(r'[^a-z0-9]', '', lower_text)
    print(f"Step 2 - Cleaned: {cleaned}")
    
    # Step 3 - Reverse the cleaned string
    reversed_text = cleaned[::-1]
    print(f"Step 3 - Reversed: {reversed_text}")
    
    # Step 4 - Compare
    if cleaned == reversed_text:
        print(f"✅ '{textValue}' is a palindrome!\n")
    else:
        print(f"❌ '{textValue}' is NOT a palindrome.\n")

# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog"))  # true
    idetify_palindrome("Python")
    idetify_palindrome("Go hang a salami, I'm a lasagna hog")

