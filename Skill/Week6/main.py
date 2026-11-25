import csv
import json
from datetime import datetime
from pathlib import Path
import requests

BASE_DIR = Path(__file__).resolve().parent
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"
INPUT_FILE = BASE_DIR / "golden_set.json"
OUTPUT_FILE = BASE_DIR / "baseline_results.csv"
RELEASE = "v0.1"

def get_llm_answer(question):
    payload = {"model": MODEL_NAME, "prompt": question, "stream": False,
               "options": {"temperature": 0}}
    response = requests.post(OLLAMA_URL, json=payload, timeout=180)
    response.raise_for_status()
    return response.json().get("response", "").strip()

def calculate_score(answer, keywords):
    answer = answer.lower()
    matched = [word for word in keywords if word.lower() in answer]
    missing = [word for word in keywords if word.lower() not in answer]
    score = (len(matched) / len(keywords) * 100) if keywords else 0
    return round(score, 2), matched, missing

def main():
    with INPUT_FILE.open(encoding="utf-8") as f:
        questions = json.load(f)

    print("\\n======================================")
    print("GOLDEN QUESTION SET")
    print("======================================")
    print("Total Questions:", len(questions))
    print("Model:", MODEL_NAME)

    results, total_score, successful = [], 0, 0
    print("\\nBASELINE RUN STARTED — Release", RELEASE)

    for number, item in enumerate(questions, start=1):
        print("\\n--------------------------------------")
        print(f"Question {number}: {item['id']}")
        print("Question:", item["question"])
        try:
            answer = get_llm_answer(item["question"])
            score, matched, missing = calculate_score(answer, item["keywords"])
            status = "PASS" if score >= 60 else "REVIEW"
            total_score += score
            successful += 1
            print("\\nLLM Answer:\\n", answer)
            print("\\nExpected Answer:\\n", item["expected_answer"])
            print("Matched Keywords:", matched)
            print("Missing Keywords:", missing)
            print("Score:", score, "%")
            print("Status:", status)
            results.append({
                "Question_ID": item["id"], "Question": item["question"],
                "Expected_Answer": item["expected_answer"], "LLM_Answer": answer,
                "Matched_Keywords": ", ".join(matched),
                "Missing_Keywords": ", ".join(missing), "Score": score,
                "Status": status, "Source": item["source"],
                "Model": MODEL_NAME, "Release": RELEASE
            })
        except requests.RequestException as exc:
            print("Error:", exc)
            results.append({
                "Question_ID": item["id"], "Question": item["question"],
                "Expected_Answer": item["expected_answer"], "LLM_Answer": "",
                "Matched_Keywords": "", "Missing_Keywords": ", ".join(item["keywords"]),
                "Score": 0, "Status": "ERROR", "Source": item["source"],
                "Model": MODEL_NAME, "Release": RELEASE
            })

    fields = ["Question_ID","Question","Expected_Answer","LLM_Answer",
              "Matched_Keywords","Missing_Keywords","Score","Status",
              "Source","Model","Release"]
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    average = total_score / successful if successful else 0
    passed = sum(r["Status"] == "PASS" for r in results)
    review = sum(r["Status"] == "REVIEW" for r in results)
    errors = sum(r["Status"] == "ERROR" for r in results)
    print("\\n======================================")
    print("BASELINE EVALUATION SUMMARY")
    print("======================================")
    print("Release Version:", RELEASE)
    print("Model:", MODEL_NAME)
    print("Total Questions:", len(questions))
    print("Successful Responses:", successful)
    print("Passed Questions:", passed)
    print("Questions for Review:", review)
    print("Failed Requests:", errors)
    print("Average Keyword Coverage:", round(average, 2), "%")
    print("Evaluation Date:", datetime.now())
    print("\\nResults saved to:", OUTPUT_FILE.name)
    print("\\nBASELINE RUN COMPLETED!")
    print("Release", RELEASE, "created successfully.")

if __name__ == "__main__":
    main()
