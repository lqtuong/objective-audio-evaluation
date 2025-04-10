#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment
import json

gt = {}
with open("gt.txt", "r") as f:
    for line in f.readlines():
        name, _, text, _ = line.split('|')
        gt[name] = text
        
scratch = {}
with open("scratch.txt", "r") as f:
    for line in f.readlines():
        name, _, text, _ = line.split('|')
        scratch[name] = text


wavs_dict = {"GT": [], "scratch": []}
folder_to_question = {"GT": [], "scratch": []}

gt_count = 1
for name in gt:
    wavs_dict['GT'].append(
        {
            "title": str(f"Nội dung: {gt[name]}"),
            "audio_path": name,
            "name": str(f"gt_{gt_count}")
        }
    )
    folder_to_question['GT'].append(f"gt_{gt_count}")
    gt_count += 1

gen_count = 1
for name in scratch:
    wavs_dict["scratch"].append(
        {
            "title": str(f"Nội dung: {scratch[name]}"),
            "audio_path": name,
            "name": str(f"gen_{gen_count}")
        }
    )
    folder_to_question['scratch'].append(f"gen_{gen_count}")
    gen_count += 1

json.dump(folder_to_question, open('folder_to_questions.json', 'w+')) 
    
wavs_list = [wavs_dict[f] for f in wavs_dict]
from itertools import chain
wavs_list = list(chain(*wavs_list))

def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")

    html = template.render(
        page_title="MOS Evaluation",
        form_url="https://script.google.com/macros/s/AKfycbzsjiF96oVWLHsMsATUfuXIKWVfMGpn6-mXdyG2skLfzchuvu6kHjnAMPK-iXe6jaDewg/exec",
        form_id=1,
        questions=wavs_list
    )
    print(html)


if __name__ == "__main__":
    main()
