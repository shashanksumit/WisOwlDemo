from reader import DocumentReader
from matcher import BERTMatcher
class JobMatcher:
    def __init__(self, jd_path, resume_path):
        self.jd_reader = DocumentReader(jd_path)
        self.resume_reader = DocumentReader(resume_path)

    def run(self):
        jd_text = self.jd_reader.read()
        resume_text = self.resume_reader.read()

        matcher = BERTMatcher(jd_text, resume_text)
        score = matcher.compute_similarity()

        print(f"\n✅ Match Score: {score}%")
        if score > 70:
            print("✅ Good match! Resume aligns well with the JD.")
        else:
            print("❌ Low match. May need to improve alignment.")


# --- Run the project ---
if __name__ == "__main__":
    jd_path = input("Enter Job Description file path: ")
    resume_path = input("Enter Resume file path: ")
    
    job_matcher = JobMatcher(jd_path, resume_path)
    job_matcher.run()