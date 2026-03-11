import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def llm_check(data):

    if not GEMINI_API_KEY:
        return {
            "status": "error",
            "confidence_score": 0.0,
            "message": "GEMINI_API_KEY not found.",
            "suggestion": "Add GEMINI_API_KEY to the .env file.",
            "source": "gemini"
        }

    client = genai.Client(api_key=GEMINI_API_KEY)

    system_prompt = """
You are Semantic Guardian, a real-time survey validation assistant.

Detect logical and semantic inconsistencies in survey responses.

Return ONLY valid JSON with this structure:
{
  "status": "ok" or "warning" or "error",
  "confidence_score": 0.0,
  "message": "short explanation",
  "suggestion": "short correction suggestion",
  "source": "gemini"
}

Example 1
Input:
{"age": 17, "employment_type": "Full-time", "education": "High School", "job_title": "Cashier"}
Output:
{"status": "warning", "confidence_score": 0.93, "message": "Age appears inconsistent with full-time employment.", "suggestion": "Verify age or employment type.", "source": "gemini"}

Example 2
Input:
{"age": 40, "education": "Primary", "job_title": "Neurosurgeon", "employment_type": "Full-time"}
Output:
{"status": "warning", "confidence_score": 0.96, "message": "Job title appears inconsistent with education level.", "suggestion": "Verify job title or education.", "source": "gemini"}

Example 3
Input:
{"age": 28, "education": "Bachelor", "employment_type": "Full-time", "job_title": "Administrative Assistant"}
Output:
{"status": "ok", "confidence_score": 0.88, "message": "Responses appear logically consistent.", "suggestion": "No action needed.", "source": "gemini"}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{system_prompt}\n\nNow evaluate this input:\n{json.dumps(data, ensure_ascii=False)}",
            config=types.GenerateContentConfig(
                temperature=0.1,
                response_mime_type="application/json"
            )
        )

        if not response.text:
            return {
                "status": "error",
                "confidence_score": 0.0,
                "message": "Empty response from Gemini.",
                "suggestion": "Try again.",
                "source": "gemini"
            }

        result = json.loads(response.text)

        if "source" not in result:
            result["source"] = "gemini"

        return result

    except Exception as e:
        return {
            "status": "error",
            "confidence_score": 0.0,
            "message": str(e),
            "suggestion": "Check Gemini API key or model name.",
            "source": "gemini"
        }