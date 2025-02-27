from jinja2 import Environment, FileSystemLoader

# Define your papers here
preprints = [
    {
        "id": "P3",
        "title": "ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference",
        "authors": "Hanshi Sun, Li-Wen Chang, Wenlei Bao, Size Zheng, Ningxin Zheng, Xin Liu, Harry Dong, Yuejie Chi, Beidi Chen",
        "venue": "arXiv",
        "year": "2024",
        "links": [
            {"url": "https://arxiv.org/abs/2410.21465", "text": "PDF"},
            {"url": "https://arxiv.org/abs/2410.21465", "text": "link"}
        ]
    },
    {
        "id": "P2",
        "title": "ATOM: LOW-BIT QUANTIZATION FOR EFFICIENT AND ACCURATE LLM SERVING",
        "authors": "Yilong Zhao, Chien-Yu Lin, Kan Zhu, Zihao Ye, Lequn Chen, Size Zheng, Luis Ceze, Arvind Krishnamurthy, Tianqi Chen, Baris Kasikci",
        "venue": "arXiv",
        "year": "2023",
        "links": [
            {"url": "https://arxiv.org/abs/2310.19102", "text": "PDF"},
            {"url": "https://arxiv.org/abs/2310.19102", "text": "link"}
        ]
    },
    # Add more papers as needed
    {
        "id": "P1",
        "title": "HASCO: Towards Agile HArdware and Software CO-design for Tensor Computation",
        "authors": "Qingcheng Xiao, Size Zheng, Bingzhe Wu, Pengcheng Xu, Xuehai Qian, Yun Liang",
        "venue": "CoRR",
        "year": "2021",
        "links": [
            {"url": "../files/ISCA21-xqc.pdf", "text": "PDF"},
            {"url": "https://arxiv.org/abs/2105.01585", "text": "link"}
        ]
    },
]

journals = [
    # {
    #     "id": "",
    #     "title": "",
    #     "authors": "",
    #     "venue": "",
    #     "year": "",
    #     "links": [
    #         {"url": "", "text": "PDF"},
    #         {"url": "", "text": "link"}
    #     ]
    # },
    # Add more papers as needed
    {
        "id": "J3",
        "title": "Rubick: A Unified Infrastructure for Analyzing, Exploring, and Implementing Spatial Architectures via Dataflow Decomposition",
        "authors": "Liqiang Lu, Zizhang Luo, Size Zheng, Jieming Yin, Jason Cong, Yun Liang, Jianwei Yin",
        "venue": "TCAD",
        "year": "2023",
        "links": [
            {"url": "../files/TCAD-2023.pdf", "text": "PDF"},
            {"url": "https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10330679", "text": "link"}
        ]
    },
    {
        "id": "J2",
        "title": "NeoFlow: A Flexible Framework for Enabling Efficient Compilation for High Performance DNN Training",
        "authors": "Size Zheng, Renze Chen, Yicheng Jin, Anjiang Wei, Bingyang Wu, Xiuhong Li, Shengen Yan, Yun Liang",
        "venue": "TPDS",
        "year": "2021",
        "links": [
            {"url": "../files/NeoFlow-OpenAccess-Version.pdf", "text": "PDF"},
            {"url": "https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9664259", "text": "link"}
        ]
    },
    {
        "id": "J1",
        "title": "Accelerating convolutional neural networks on FPGAs (中文)",
        "authors": "Liqiang Lu, Size Zheng, Qingcheng Xiao, Deming Chen, Yun Liang",
        "venue": "SCIENTIA SINICA Informationis",
        "year": "2019",
        "links": [
            {"url": "../files/N112018-00291.pdf", "text": "PDF"},
            {"url": "https://ceca.pku.edu.cn/docs/20200113152559178152.pdf", "text": "link"}
        ]
    },
]

conferences = [
    # {
    #     "id": "",
    #     "title": "",
    #     "authors": "",
    #     "venue": "",
    #     "year": "",
    #     "links": [
    #         {"url": "", "text": "PDF"},
    #         {"url": "", "text": "link"}
    #     ]
    # },
    {
        "id": "C19",
        "title": "TileLink: Generating Efficient Compute-Communication Overlapping Kernels using Tile-Centric Primitives",
        "authors": "Size Zheng, Jin Fang, Xuegui Zheng, Qi Hou, Wenlei Bao, Ningxin Zheng, Ziheng Jiang, Dongyang Wang, Jianxi Ye, Haibin Lin, Li-Wen Chang, Xin Liu",
        "venue": "MLSys",
        "year": "2025",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ]
    },
    {
        "id": "C18",
        "title": "COMET: Fine-grained Computation-communication Overlapping for Mixture-of-Experts",
        "authors": "Shulai Zhang, Ningxin Zheng, Haibin Lin, Ziheng Jiang, Wenlei Bao, Chengquan Jiang, Qi Hou, Weihao Cui, Size Zheng, Li-Wen Chang, Quan Chen, Xin Liu",
        "venue": "MLSys",
        "year": "2025",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ]
    },
    {
        "id": "C17",
        "title": "DyREM: Dynamically Mitigating Quantum Readout Error with Embedded Accelerator",
        "authors": "Kaiwen Zhou, Liqiang Lu, Hanyu Zhang, Debin Xiang, Chenning Tao, xinkui zhao, Size Zheng and Jianwei Yin",
        "venue": "DAC",
        "year": "2025",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ]
    },
    {
        "id": "C16",
        "title": "ArkVale: Efficient Generative LLM Inference with Recallable Key-Value Eviction",
        "authors": "Renze Chen, Zhuofeng Wang, Beiquan Cao, Tong Wu, Size Zheng, Xiuhong Li, Xuechao Wei, Shengen Yan, Meng Li, Yun Liang",
        "venue": "NeurIPS",
        "year": "2024",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ]
    },
    {
        "id": "C15",
        "title": "SpecPIM: Accelerating Speculative Inference on PIM-Enabled System via Architecture-Dataflow Co-Exploration",
        "authors": "Cong Li, Zhe Zhou, Size Zheng, Jiaxi Zhang, Yun Liang, Guangyu Sun",
        "venue": "ASPLOS",
        "year": "2024",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ]
    },
    {
        "id": "C14",
        "title": "MAGIS: Memory Optimization via Coordinated Graph Transformation and Scheduling for DNN",
        "authors": "Renze Chen, Zijian Ding, Size Zheng, Chengrui Zhang, Jingwen Leng, Xuanzhe Liu, Yun Liang",
        "venue": "ASPLOS",
        "year": "2024",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ]
    },
    {
        "id": "C13",
        "title": "vMCU: Coordinated Memory Management and Kernel Optimization for DNN Inference on MCUs",
        "authors": "Size Zheng, Renze Chen, Meng Li, Zihao Ye, Luis Ceze, Yun Liang",
        "venue": "MLSys",
        "year": "2024",
        "links": [
            {"url": "../files/vMCU.pdf", "text": "PDF"},
            {"url": "", "text": "link"}
        ]
    },
    {
        "id": "C12",
        "title": "ATOM: LOW-BIT QUANTIZATION FOR EFFICIENT AND ACCURATE LLM SERVING",
        "authors": "Yilong Zhao, Chien-Yu Lin, Kan Zhu, Zihao Ye, Lequn Chen, Size Zheng, Luis Ceze, Arvind Krishnamurthy, Tianqi Chen, Baris Kasikci",
        "venue": "MLSys",
        "year": "2024",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ]
    },
    {
        "id": "C11",
        "title": "SpREM: Exploiting Hamming Sparsity for Fast Quantum Readout Error Mitigation",
        "authors": "Hanyu Zhang, Liqiang Lu, Siwei Tan, Size Zheng, Jia Yu and Jianwei Yin",
        "venue": "DAC",
        "year": "2024",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ]
    },
    {
        "id": "C10",
        "title": "MoteNN: Memory Optimization via Fine-grained Scheduling for Deep Neural Networks on Tiny Devices",
        "authors": "Renze Chen, Zijian Ding, Size Zheng, Meng Li, Yun Liang",
        "venue": "DAC",
        "year": "2024",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ]
    },
    {
        "id": "C9",
        "title": "TileFlow: A Framework for Modeling Fusion Dataflow via Tree-based Analysis",
        "authors": "Size Zheng, Siyuan Chen, Siyuan Gao, Liancheng Jia, Guangyu Sun, Runsheng Wang, Yun Liang",
        "venue": "MICRO",
        "year": "2023",
        "links": [
            {"url": "../files/micro23-101.pdf", "text": "PDF"},
            {"url": "https://dl.acm.org/doi/10.1145/3613424.3623792", "text": "link"}
        ]
    },
    {
        "id": "C8",
        "title": "ARES: A Mapping Framework of DNNs towards Diverse PIMs with General Abstractions",
        "authors": "Xiuping Cui, Size Zheng, Tianyu Jia, Le Ye and Yun Liang",
        "venue": "ICCAD",
        "year": "2023",
        "links": [
            {"url": "../files/ARES_A_Mapping_Framework_of_DNNs_Towards_Diverse_PIMs_with_General_Abstractions.pdf", "text": "PDF"},
            {"url": "https://ieeexplore.ieee.org/document/10323777", "text": "link"}
        ]
    },
    {
        "id": "C7",
        "title": "Memory and Computation Coordinated Mapping of DNNs onto Complex Heterogeneous SoC",
        "authors": "Size Zheng, Siyuan Chen, Yun Liang",
        "venue": "DAC",
        "year": "2023",
        "links": [
            {"url": "../files/COMB-Final.pdf", "text": "PDF"},
            {"url": "https://ieeexplore.ieee.org/document/10247951", "text": "link"}
        ]
    },
    {
        "id": "C6",
        "title": "Rubick: A Synthesis Framework for Spatial Architectures via Dataflow Decomposition",
        "authors": "Zizhang Luo, Liqiang Lu, Size Zheng, Jieming Yin, Jason Cong, Jianwei Yin, Yun Liang",
        "venue": "DAC",
        "year": "2023",
        "links": [
            {"url": "../files/Rubick_final.pdf", "text": "PDF"},
            {"url": "https://ieeexplore.ieee.org/document/10247743", "text": "link"}
        ]
    },
    {
        "id": "C5",
        "title": "Chimera: An Analytical Optimizing Framework for Effective Compute-intensive Operators Fusion",
        "authors": "Size Zheng, Siyuan Chen, Peidi Song, Renze Chen, Xiuhong Li, Shengen Yan, Dahua Lin, Jingwen Leng, Yun Liang",
        "venue": "HPCA",
        "year": "2023",
        "links": [
            {"url": "../files/7A-3.pdf", "text": "PDF"},
            {"url": "https://ieeexplore.ieee.org/document/10071018/", "text": "link"}
        ]
    },
    {
        "id": "C4",
        "title": "AMOS: Enabling Automatic Mapping for Tensor Computations On Spatial Accelerators with Hardware Abstraction",
        "authors": "Size Zheng, Renze Chen, Anjiang Wei, Yicheng Jin, Qin Han, Liqiang Lu, Bingyang Wu, Xiuhong Li, Shengen Yan, Yun Liang",
        "venue": "ISCA",
        "year": "2022",
        "links": [
            {"url": "../files/AMOS_ISCA_22_Final.pdf", "text": "PDF"},
            {"url": "https://dl.acm.org/doi/abs/10.1145/3470496.3527440", "text": "link"}
        ]
    },
    {
        "id": "C3",
        "title": "HASCO: Towards Agile HArdware and Software CO-design for Tensor Computation",
        "authors": "Qingcheng Xiao, Size Zheng, Bingzhe Wu, Pengcheng Xu, Xuehai Qian, Yun Liang",
        "venue": "ISCA",
        "year": "2021",
        "links": [
            {"url": "../files/ISCA21-xqc.pdf", "text": "PDF"},
            {"url": "https://dl.acm.org/doi/10.1109/ISCA52012.2021.00086", "text": "link"}
        ]
    },
    {
        "id": "C2",
        "title": "SuSy: A Programming Model for Productive Construction of High-Performance Systolic Arrays on FPGAs",
        "authors": "Yi-Hsiang Lai, Hongbo Rong, Size Zheng, Weihao Zhang, Xiuping Cui, Yunshan Jia, Jie Wang, Brendan Sullivan, Zhiru Zhang, Yun Liang, Youhui Zhang, Jason Cong, Nithin George, Jose Alvarez, Christopher J. Hughes, Pradeep Dubey",
        "venue": "ICCAD",
        "year": "2020",
        "links": [
            {"url": "../files/susy.pdf", "text": "PDF"},
            {"url": "https://dl.acm.org/doi/abs/10.1145/3400302.3415644", "text": "link"}
        ]
    },
    {
        "id": "C1",
        "title": "FlexTensor: An Automatic Schedule Exploration and Optimization Framework for Tensor Computation on Heterogeneous System",
        "authors": "Size Zheng, Yun Liang, Shuo Wang, Renze Chen, Kaiwen Sheng",
        "venue": "ASPLOS",
        "year": "2020",
        "links": [
            {"url": "../files/flextensor.pdf", "text": "PDF"},
            {"url": "https://dl.acm.org/doi/10.1145/3373376.3378508", "text": "link"}
        ]
    },
]

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('publication-jinja.j2')


# Print the generated Markdown
with open("./publications.md", "w") as fout:
    fout.write("""
---
title: "Publications"
permalink: /publications/
author_profile: true
---

<!-- See a full list on  [Google Scholar](https://scholar.google.com/citations?user=_7Q8uIYAAAAJ&hl=en)   -->
               """)
    fout.write("""
---

## Preprint      
               """)
    output = template.render(papers=preprints)
    print(output, file=fout)
    fout.write("""
---

## Journal     
               """)
    output = template.render(papers=journals)
    print(output, file=fout)
    fout.write("""
---

## Conference     
               """)
    output = template.render(papers=conferences)
    print(output, file=fout)