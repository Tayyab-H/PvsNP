import os
import glob
import re

def extract_headers_and_summaries(filepath, max_len=1000):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return f"Error reading {filepath}: {e}"

    # Extract markdown headers
    headers = re.findall(r'^(#{1,4}\s+.*)', content, re.MULTILINE)
    
    # Just return a small snippet or the headers
    summary = f"--- {os.path.basename(filepath)} ---\n"
    summary += f"File size: {len(content)} chars\n"
    summary += "Headers:\n" + "\n".join(headers[:30]) + "\n"
    if len(headers) > 30:
        summary += "... (more headers truncated)\n"
    return summary

def main():
    root = r"d:\projects\P vs NP"
    gemini_dir = os.path.join(root, "Gemini")
    
    if not os.path.exists(gemini_dir):
        os.makedirs(gemini_dir)
        
    out_file = os.path.join(gemini_dir, "synthesis_summary.txt")
    
    files_to_check = [
        os.path.join(root, "ideas.md"),
        os.path.join(root, "New Model.MD")
    ]
    
    # Get latest research files (e.g. C280 to C293, and state files)
    research_dir = os.path.join(root, "research")
    if os.path.exists(research_dir):
        all_research = glob.glob(os.path.join(research_dir, "*.md"))
        # sort by modified time
        all_research.sort(key=os.path.getmtime, reverse=True)
        files_to_check.extend(all_research[:20]) # top 20 most recent
    
    with open(out_file, 'w', encoding='utf-8') as out:
        for f in files_to_check:
            if os.path.exists(f):
                out.write(extract_headers_and_summaries(f) + "\n\n")
            else:
                out.write(f"File not found: {f}\n\n")
                
    print(f"Summary written to {out_file}")

if __name__ == '__main__':
    main()
