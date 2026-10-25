import os
from google import genai

def analyze_with_gemini_argon(code_snippet: str, prompt_context: str = "Analyze this contract for security flaws:") -> str:
    """
    Sends complex code/bytecode or transaction payloads to Gemini 4 Argon
    using the official Google GenAI SDK.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
        
    client = genai.Client(api_key=api_key)
    
    response = client.models.generate_content(
        model='gemini-4-argon',
        contents=f"{prompt_context}\n\n```solidity\n{code_snippet}\n```",
    )
    return response.text

if __name__ == "__main__":
    sample_code = "contract Vulnerable { mapping(address => uint) balances; function withdraw() public { (bool success, ) = msg.sender.call{value: balances[msg.sender]}(''); require(success); balances[msg.sender] = 0; } }"
    print("Module loaded. Call analyze_with_gemini_argon(code_snippet) with a valid API key.")
  
