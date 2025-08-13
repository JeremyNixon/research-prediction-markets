"""
Example script for loading OpenAI API key from environment variables.
"""

import os
from dotenv import load_dotenv

def load_openai_key():
    """
    Load OpenAI API key from .env file.
    
    Returns:
        str: OpenAI API key
        
    Raises:
        ValueError: If API key is not found
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the API key
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables. Make sure .env file exists and contains the key.")
    
    return api_key

def load_anthropic_key():
    """
    Load Anthropic API key from .env file.
    
    Returns:
        str: Anthropic API key
        
    Raises:
        ValueError: If API key is not found
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the API key
    api_key = os.getenv('ANTHROPIC_API_KEY')
    
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found in environment variables. Make sure .env file exists and contains the key.")
    
    return api_key

def example_usage():
    """
    Example of how to use the API keys with OpenAI and Anthropic clients.
    """
    try:
        # Load OpenAI API key
        openai_key = load_openai_key()
        print("✅ OpenAI API key loaded successfully!")
        
        # Example: Initialize OpenAI client (uncomment when openai package is installed)
        # from openai import OpenAI
        # openai_client = OpenAI(api_key=openai_key)
        # print("OpenAI client initialized")
        
        # For security, only show first and last 4 characters
        masked_openai_key = f"{openai_key[:7]}...{openai_key[-4:]}"
        print(f"Using OpenAI API key: {masked_openai_key}")
        
        # Load Anthropic API key
        anthropic_key = load_anthropic_key()
        print("✅ Anthropic API key loaded successfully!")
        
        # Example: Initialize Anthropic client (uncomment when anthropic package is installed)
        # import anthropic
        # anthropic_client = anthropic.Anthropic(api_key=anthropic_key)
        # print("Anthropic client initialized")
        
        # For security, only show first and last 4 characters
        masked_anthropic_key = f"{anthropic_key[:7]}...{anthropic_key[-4:]}"
        print(f"Using Anthropic API key: {masked_anthropic_key}")
        
    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    example_usage()
