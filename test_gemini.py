import google.generativeai as genai

# Test Gemini API Connection
print("Testing Google Gemini API...")
print("-" * 50)

# Configure API
api_key = "AIzaSyDiWMYDAabH1oZ95IBg8GkYppi2DHDy-wM"
genai.configure(api_key=api_key)

print("✓ API Key configured")

# List available models
print("\nAvailable models:")
try:
    models = genai.list_models()
    for model in models:
        print(f"  - {model.name}")
except Exception as e:
    print(f"✗ Error listing models: {e}")

# Try to generate content
print("\n" + "-" * 50)
print("Testing content generation...")
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
    print("✓ Model loaded successfully")
    
    response = model.generate_content("What is AI?")
    print("✓ API request successful!")
    print(f"\nResponse: {response.text[:200]}...")
except Exception as e:
    print(f"✗ Error: {e}")
