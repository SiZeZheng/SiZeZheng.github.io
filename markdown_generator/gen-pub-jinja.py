from jinja2 import Environment, FileSystemLoader

# Define your papers here
preprints = [
    {
        "id": "P1",
        "title": "ATOM: LOW-BIT QUANTIZATION FOR EFFICIENT AND ACCURATE LLM SERVING",
        "authors": "Yilong Zhao, Chien-Yu Lin, Kan Zhu, Zihao Ye, Lequn Chen, **Size Zheng**, Luis Ceze, Arvind Krishnamurthy, Tianqi Chen, Baris Kasikci",
        "venue": "arXiv 2023",
        "year": "2023",
        "links": [
            {"url": "https://arxiv.org/abs/2310.19102", "text": "PDF"},
            {"url": "https://arxiv.org/abs/2310.19102", "text": "link"}
        ]
    },
    # Add more papers as needed
]

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.j2')
output = template.render(papers=preprints)

# Print the generated Markdown
with open("./publications.md", "w") as fout:
    print(output, file=fout)