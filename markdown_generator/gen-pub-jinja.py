from jinja2 import Environment, FileSystemLoader

# Venue type definitions - easily maintainable lists
PREPRINT_VENUES = [
    "arXiv",
    "CoRR",
    # Add more preprint venues here as needed
]

JOURNAL_VENUES = [
    "TCAD",
    "TPDS",
    "SCIENTIA SINICA Informationis",
    "TC",
    # Add more journal venues here as needed
]

# ============================================================================
# UNIFIED PUBLICATION LIST - Maintain all papers here in a single list
# ============================================================================
# Each paper should have:
#   - title, authors, venue, year, links (required)
#   - first_author: True if you are first author, False if co-author (required)
#   - organization: "at_peking_university" | "at_bytedance_seed" | 
#                   "at_washington_university" | "at_deepseek" | 
#                   "as_independent_researcher" (required)
# ============================================================================

all_publications = [
    # First author publications at Peking University
    {
        "title": "vMCU: Coordinated Memory Management and Kernel Optimization for DNN Inference on MCUs",
        "authors": "Size Zheng, Renze Chen, Meng Li, Zihao Ye, Luis Ceze, Yun Liang",
        "venue": "MLSys",
        "year": "2024",
        "links": [
            {"url": "../files/vMCU.pdf", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": True,
        "organization": "at_peking_university"
    },
    {
        "title": "TileFlow: A Framework for Modeling Fusion Dataflow via Tree-based Analysis",
        "authors": "Size Zheng, Siyuan Chen, Siyuan Gao, Liancheng Jia, Guangyu Sun, Runsheng Wang, Yun Liang",
        "venue": "MICRO",
        "year": "2023",
        "links": [
            {"url": "../files/micro23-101.pdf", "text": "PDF"},
            {"url": "https://dl.acm.org/doi/10.1145/3613424.3623792", "text": "link"}
        ],
        "first_author": True,
        "organization": "at_peking_university"
    },
    {
        "title": "Memory and Computation Coordinated Mapping of DNNs onto Complex Heterogeneous SoC",
        "authors": "Size Zheng, Siyuan Chen, Yun Liang",
        "venue": "DAC",
        "year": "2023",
        "links": [
            {"url": "../files/COMB-Final.pdf", "text": "PDF"},
            {"url": "https://ieeexplore.ieee.org/document/10247951", "text": "link"}
        ],
        "first_author": True,
        "organization": "at_peking_university"
    },
    {
        "title": "Chimera: An Analytical Optimizing Framework for Effective Compute-intensive Operators Fusion",
        "authors": "Size Zheng, Siyuan Chen, Peidi Song, Renze Chen, Xiuhong Li, Shengen Yan, Dahua Lin, Jingwen Leng, Yun Liang",
        "venue": "HPCA",
        "year": "2023",
        "links": [
            {"url": "../files/7A-3.pdf", "text": "PDF"},
            {"url": "https://ieeexplore.ieee.org/document/10071018/", "text": "link"}
        ],
        "first_author": True,
        "organization": "at_peking_university"
    },
    {
        "title": "AMOS: Enabling Automatic Mapping for Tensor Computations On Spatial Accelerators with Hardware Abstraction",
        "authors": "Size Zheng, Renze Chen, Anjiang Wei, Yicheng Jin, Qin Han, Liqiang Lu, Bingyang Wu, Xiuhong Li, Shengen Yan, Yun Liang",
        "venue": "ISCA",
        "year": "2022",
        "links": [
            {"url": "../files/AMOS_ISCA_22_Final.pdf", "text": "PDF"},
            {"url": "https://dl.acm.org/doi/abs/10.1145/3470496.3527440", "text": "link"}
        ],
        "first_author": True,
        "organization": "at_peking_university"
    },
    {
        "title": "FlexTensor: An Automatic Schedule Exploration and Optimization Framework for Tensor Computation on Heterogeneous System",
        "authors": "Size Zheng, Yun Liang, Shuo Wang, Renze Chen, Kaiwen Sheng",
        "venue": "ASPLOS",
        "year": "2020",
        "links": [
            {"url": "../files/flextensor.pdf", "text": "PDF"},
            {"url": "https://dl.acm.org/doi/10.1145/3373376.3378508", "text": "link"}
        ],
        "first_author": True,
        "organization": "at_peking_university",
        "google_scholar": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=TMZWR1gAAAAJ&citation_for_view=TMZWR1gAAAAJ:qjMakFHDy7sC"
    },
    # First author publications at ByteDance SEED
    {
        "title": "Triton-distributed: Programming Overlapping Kernels on Distributed AI Systems with the Triton Compiler",
        "authors": "Size Zheng, Wenlei Bao, Qi Hou, Xuegui Zheng, Jin Fang, Chenhui Huang, Tianqi Li, Haojie Duanmu, Renze Chen, Ruifan Xu, Yifan Guo, Ningxin Zheng, Ziheng Jiang, Xinyi Di, Dongyang Wang, Jianxi Ye, Haibin Lin, Li-Wen Chang, Liqiang Lu, Yun Liang, Jidong Zhai, Xin Liu",
        "venue": "arXiv",
        "year": "2025",
        "links": [
            {"url": "https://arxiv.org/abs/2504.19442", "text": "PDF"},
            {"url": "https://arxiv.org/abs/2504.19442", "text": "link"}
        ],
        "first_author": True,
        "organization": "at_bytedance_seed"
    },
    {
        "title": "TileLink: Generating Efficient Compute-Communication Overlapping Kernels using Tile-Centric Primitives",
        "authors": "Size Zheng, Jin Fang, Xuegui Zheng, Qi Hou, Wenlei Bao, Ningxin Zheng, Ziheng Jiang, Dongyang Wang, Jianxi Ye, Haibin Lin, Li-Wen Chang, Xin Liu",
        "venue": "MLSys",
        "year": "2025",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": True,
        "organization": "at_bytedance_seed"
    },
    # Co-author publications at Peking University
    {
        "title": "DynaMo: Runtime Switchable Quantization for MoE with Cross-Dataset Adaptation",
        "authors": "Zihao Zheng, Xiuping Cui, Size Zheng, Maoliang Li, Jiayu Chen, Yun Liang, Xiang Chen",
        "venue": "DATE",
        "year": "2026",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_peking_university"
    },
    {
        "title": "LATIAS: A General Architecture-Operator Model for Spatial Accelerators with Complex Topology and Memory Hierarchy",
        "authors": "Chengrui Zhang, Liancheng Jia, Chu Wang, Tianqi Li, Renze Chen, Xiuping Cui, Size Zheng, Shengen Yan, Xiuhong Li, Yu Wang, Xiang Chen, Yun Liang",
        "venue": "DATE",
        "year": "2026",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_peking_university"
    },
    {
        "title": "ArkVale: Efficient Generative LLM Inference with Recallable Key-Value Eviction",
        "authors": "Renze Chen, Zhuofeng Wang, Beiquan Cao, Tong Wu, Size Zheng, Xiuhong Li, Xuechao Wei, Shengen Yan, Meng Li, Yun Liang",
        "venue": "NeurIPS",
        "year": "2024",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_peking_university"
    },
    {
        "title": "SpecPIM: Accelerating Speculative Inference on PIM-Enabled System via Architecture-Dataflow Co-Exploration",
        "authors": "Cong Li, Zhe Zhou, Size Zheng, Jiaxi Zhang, Yun Liang, Guangyu Sun",
        "venue": "ASPLOS",
        "year": "2024",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_peking_university"
    },
    {
        "title": "MAGIS: Memory Optimization via Coordinated Graph Transformation and Scheduling for DNN",
        "authors": "Renze Chen, Zijian Ding, Size Zheng, Chengrui Zhang, Jingwen Leng, Xuanzhe Liu, Yun Liang",
        "venue": "ASPLOS",
        "year": "2024",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_peking_university"
    },
    {
        "title": "MoteNN: Memory Optimization via Fine-grained Scheduling for Deep Neural Networks on Tiny Devices",
        "authors": "Renze Chen, Zijian Ding, Size Zheng, Meng Li, Yun Liang",
        "venue": "DAC",
        "year": "2024",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_peking_university"
    },
    {
        "title": "ARES: A Mapping Framework of DNNs towards Diverse PIMs with General Abstractions",
        "authors": "Xiuping Cui, Size Zheng, Tianyu Jia, Le Ye and Yun Liang",
        "venue": "ICCAD",
        "year": "2023",
        "links": [
            {"url": "../files/ARES_A_Mapping_Framework_of_DNNs_Towards_Diverse_PIMs_with_General_Abstractions.pdf", "text": "PDF"},
            {"url": "https://ieeexplore.ieee.org/document/10323777", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_peking_university"
    },
    {
        "title": "Rubick: A Synthesis Framework for Spatial Architectures via Dataflow Decomposition",
        "authors": "Zizhang Luo, Liqiang Lu, Size Zheng, Jieming Yin, Jason Cong, Jianwei Yin, Yun Liang",
        "venue": "DAC",
        "year": "2023",
        "links": [
            {"url": "../files/Rubick_final.pdf", "text": "PDF"},
            {"url": "https://ieeexplore.ieee.org/document/10247743", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_peking_university"
    },
    {
        "title": "Rubick: A Unified Infrastructure for Analyzing, Exploring, and Implementing Spatial Architectures via Dataflow Decomposition",
        "authors": "Liqiang Lu, Zizhang Luo, Size Zheng, Jieming Yin, Jason Cong, Yun Liang, Jianwei Yin",
        "venue": "TCAD",
        "year": "2023",
        "links": [
            {"url": "../files/TCAD-2023.pdf", "text": "PDF"},
            {"url": "https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10330679", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_peking_university"
    },
    {
        "title": "HASCO: Towards Agile HArdware and Software CO-design for Tensor Computation",
        "authors": "Qingcheng Xiao, Size Zheng, Bingzhe Wu, Pengcheng Xu, Xuehai Qian, Yun Liang",
        "venue": "ISCA",
        "year": "2021",
        "links": [
            {"url": "../files/ISCA21-xqc.pdf", "text": "PDF"},
            {"url": "https://dl.acm.org/doi/10.1109/ISCA52012.2021.00086", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_peking_university"
    },
    {
        "title": "NeoFlow: A Flexible Framework for Enabling Efficient Compilation for High Performance DNN Training",
        "authors": "Size Zheng, Renze Chen, Yicheng Jin, Anjiang Wei, Bingyang Wu, Xiuhong Li, Shengen Yan, Yun Liang",
        "venue": "TPDS",
        "year": "2021",
        "links": [
            {"url": "../files/NeoFlow-OpenAccess-Version.pdf", "text": "PDF"},
            {"url": "https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9664259", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_peking_university"
    },
    {
        "title": "SuSy: A Programming Model for Productive Construction of High-Performance Systolic Arrays on FPGAs",
        "authors": "Yi-Hsiang Lai, Hongbo Rong, Size Zheng, Weihao Zhang, Xiuping Cui, Yunshan Jia, Jie Wang, Brendan Sullivan, Zhiru Zhang, Yun Liang, Youhui Zhang, Jason Cong, Nithin George, Jose Alvarez, Christopher J. Hughes, Pradeep Dubey",
        "venue": "ICCAD",
        "year": "2020",
        "links": [
            {"url": "../files/susy.pdf", "text": "PDF"},
            {"url": "https://dl.acm.org/doi/abs/10.1145/3400302.3415644", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_peking_university"
    },
    {
        "title": "Accelerating convolutional neural networks on FPGAs (中文)",
        "authors": "Liqiang Lu, Size Zheng, Qingcheng Xiao, Deming Chen, Yun Liang",
        "venue": "SCIENTIA SINICA Informationis",
        "year": "2019",
        "links": [
            {"url": "../files/N112018-00291.pdf", "text": "PDF"},
            {"url": "https://ceca.pku.edu.cn/docs/20200113152559178152.pdf", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_peking_university"
    },
    # Co-author publications at University of Washington
    {
        "title": "ATOM: LOW-BIT QUANTIZATION FOR EFFICIENT AND ACCURATE LLM SERVING",
        "authors": "Yilong Zhao, Chien-Yu Lin, Kan Zhu, Zihao Ye, Lequn Chen, Size Zheng, Luis Ceze, Arvind Krishnamurthy, Tianqi Chen, Baris Kasikci",
        "venue": "MLSys",
        "year": "2024",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_washington_university"
    },
    # Co-author publications at DeepSeek
    {
        "title": "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model",
        "authors": "DeepSeek-AI",
        "venue": "arXiv",
        "year": "2024",
        "links": [
            {"url": "https://arxiv.org/pdf/2405.04434?", "text": "PDF"},
            {"url": "https://arxiv.org/pdf/2405.04434?", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_deepseek"
    },
    # Co-author publications at ByteDance SEED
    {
        "title": "MegaScale-MoE: Large-Scale Communication-Efficient Training of Mixture-of-Experts Models in Production",
        "authors": "Chao Jin, Ziheng Jiang, Zhihao Bai, Zheng Zhong, Juncai Liu, Xiang Li, Ningxin Zheng, Xi Wang, Cong Xie, Qi Huang, Wen Heng, Yiyuan Ma, Wenlei Bao, Size Zheng, Yanghua Peng, Haibin Lin, Xuanzhe Liu, Xin Jin, Xin Liu",
        "venue": "EuroSys",
        "year": "2026",
        "links": [
            {"url": "https://arxiv.org/pdf/2505.11432", "text": "PDF"},
            {"url": "https://arxiv.org/pdf/2505.11432", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_bytedance_seed"
    },
    {
        "title": "ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference",
        "authors": "Hanshi Sun, Li-Wen Chang, Wenlei Bao, Size Zheng, Ningxin Zheng, Xin Liu, Harry Dong, Yuejie Chi, Beidi Chen",
        "venue": "ICML",
        "year": "2025",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_bytedance_seed"
    },
    {
        "title": "MxMoE: Mixed-precision Quantization for MoE with Accuracy and Performance Co-Design",
        "authors": "Haojie Duanmu, Xiuhong Li, Zhihang Yuan, Size Zheng, Jiangfei Duan, Xingcheng Zhang, Dahua Lin",
        "venue": "ICML",
        "year": "2025",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_bytedance_seed"
    },
    {
        "title": "COMET: Fine-grained Computation-communication Overlapping for Mixture-of-Experts",
        "authors": "Shulai Zhang, Ningxin Zheng, Haibin Lin, Ziheng Jiang, Wenlei Bao, Chengquan Jiang, Qi Hou, Weihao Cui, Size Zheng, Li-Wen Chang, Quan Chen, Xin Liu",
        "venue": "MLSys",
        "year": "2025",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_bytedance_seed"
    },
    # Co-author publications as Independent Researcher
    {
        "title": "SnakeMan: Applying Relation-centric Notation to Model and Optimize Data Swizzle in the Cache of Modern NPU",
        "authors": "Hanyu Zhang, Fangxu Guo, Liqiang Lu, Long Wang, Yunfei Du, Zhe Wang, Jinghan Zhang, Jie Zhang, Chenli Xue, Chengpeng Wu, Ziyi Zhang, Yun Liang, Size Zheng, Jianwei Yin",
        "venue": "HPCA",
        "year": "2026",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": False,
        "organization": "as_independent_researcher"
    },
    {
        "title": "MI-LLM: Multiplier-free LLM Inference on Commodity Processing-in-Memory Hardware",
        "authors": "Puyun Hu, Minhui Xie, Linjiang Li, Kuiyaohui Zhang, Erge Xiang, Jing Wang, Size Zheng, Xiao Zhang, Yunpeng Chai",
        "venue": "TC",
        "year": "2025",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "https://www.computer.org/csdl/journal/tc/5555/01/11219263/2bbyqoNTcVG", "text": "link"}
        ],
        "first_author": False,
        "organization": "as_independent_researcher"
    },
    {
        "title": "Qtenon: Towards Low-Latency Architecture Integration for Accelerating Hybrid Quantum-Classical Computing",
        "authors": "Chenning Tao, Liqiang Lu, Size Zheng, Li-Wen Chang, Minghua Shen, Hanyu Zhang, Fangxin Liu, Kaiwen Zhou, Jianwei Yin",
        "venue": "ISCA",
        "year": "2025",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": False,
        "organization": "as_independent_researcher"
    },
    {
        "title": "DyREM: Dynamically Mitigating Quantum Readout Error with Embedded Accelerator",
        "authors": "Kaiwen Zhou, Liqiang Lu, Hanyu Zhang, Debin Xiang, Chenning Tao, xinkui zhao, Size Zheng and Jianwei Yin",
        "venue": "DAC",
        "year": "2025",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": False,
        "organization": "as_independent_researcher"
    },
    {
        "title": "SpREM: Exploiting Hamming Sparsity for Fast Quantum Readout Error Mitigation",
        "authors": "Hanyu Zhang, Liqiang Lu, Siwei Tan, Size Zheng, Jia Yu and Jianwei Yin",
        "venue": "DAC",
        "year": "2024",
        "links": [
            {"url": "", "text": "PDF"},
            {"url": "", "text": "link"}
        ],
        "first_author": False,
        "organization": "as_independent_researcher"
    },
    # Additional preprints
    {
        "title": "ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference",
        "authors": "Hanshi Sun, Li-Wen Chang, Wenlei Bao, Size Zheng, Ningxin Zheng, Xin Liu, Harry Dong, Yuejie Chi, Beidi Chen",
        "venue": "arXiv",
        "year": "2024",
        "links": [
            {"url": "https://arxiv.org/abs/2410.21465", "text": "PDF"},
            {"url": "https://arxiv.org/abs/2410.21465", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_bytedance_seed"
    },
    {
        "title": "ATOM: LOW-BIT QUANTIZATION FOR EFFICIENT AND ACCURATE LLM SERVING",
        "authors": "Yilong Zhao, Chien-Yu Lin, Kan Zhu, Zihao Ye, Lequn Chen, Size Zheng, Luis Ceze, Arvind Krishnamurthy, Tianqi Chen, Baris Kasikci",
        "venue": "arXiv",
        "year": "2023",
        "links": [
            {"url": "https://arxiv.org/abs/2310.19102", "text": "PDF"},
            {"url": "https://arxiv.org/abs/2310.19102", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_washington_university"
    },
    {
        "title": "HASCO: Towards Agile HArdware and Software CO-design for Tensor Computation",
        "authors": "Qingcheng Xiao, Size Zheng, Bingzhe Wu, Pengcheng Xu, Xuehai Qian, Yun Liang",
        "venue": "CoRR",
        "year": "2021",
        "links": [
            {"url": "../files/ISCA21-xqc.pdf", "text": "PDF"},
            {"url": "https://arxiv.org/abs/2105.01585", "text": "link"}
        ],
        "first_author": False,
        "organization": "at_peking_university"
    },
]

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('publication-jinja.j2')
template_org = env.get_template('publication-jinja-org.j2')

# Helper function to determine paper type from venue
def get_paper_type(venue):
    """Determine paper type from venue name."""
    if venue in PREPRINT_VENUES:
        return "Preprint"
    if venue in JOURNAL_VENUES:
        return "Journal"
    # Everything else is a conference
    return "Conference"

# Function to organize publications from unified list
def organize_publications(all_papers):
    """
    Organize papers from unified list into different views.
    Returns: (preprints, journals, conferences, first_author_pubs, co_author_pubs)
    Note: Creates separate copies for type-based and org-based views to maintain separate IDs.
    """
    preprints = []
    journals = []
    conferences = []
    first_author_pubs = {
        "at_peking_university": [],
        "at_bytedance_seed": [],
        "at_washington_university": [],
        "at_deepseek": [],
        "as_independent_researcher": []
    }
    co_author_pubs = {
        "at_peking_university": [],
        "at_bytedance_seed": [],
        "at_washington_university": [],
        "at_deepseek": [],
        "as_independent_researcher": []
    }
    
    for paper in all_papers:
        # Create separate copies for type-based view and org-based view
        # This ensures IDs can be assigned independently
        paper_copy_type = paper.copy()
        paper_copy_org = paper.copy()
        
        # Determine paper type
        paper_type = get_paper_type(paper["venue"])
        
        # Add to type-based lists (for "By Type & Time" view)
        if paper_type == "Preprint":
            preprints.append(paper_copy_type)
        elif paper_type == "Journal":
            journals.append(paper_copy_type)
        else:  # Conference
            conferences.append(paper_copy_type)
        
        # Add to organization-based lists (for "By Organization & Contribution" view)
        org = paper["organization"]
        if paper["first_author"]:
            if org in first_author_pubs:
                first_author_pubs[org].append(paper_copy_org)
        else:
            if org in co_author_pubs:
                co_author_pubs[org].append(paper_copy_org)
    
    return preprints, journals, conferences, first_author_pubs, co_author_pubs

# Generate all views from unified list
preprints, journals, conferences, first_author_publications, co_author_publications = organize_publications(all_publications)

# Function to automatically assign IDs based on year and order
def assign_ids(papers, prefix):
    """
    Assign IDs to papers based on year (ascending, oldest first) and list order.
    For papers with the same year, maintain the list order (top to bottom = newest to oldest).
    Numbering: 1 = oldest, highest number = newest.
    """
    # Group by year while maintaining original list order within each year
    papers_by_year = {}
    for paper in papers:
        year = int(paper["year"])
        if year not in papers_by_year:
            papers_by_year[year] = []
        papers_by_year[year].append(paper)
    
    # Sort years ascending (oldest first) and flatten, maintaining order within each year
    # For same year, reverse the order since list is newest first, but we want oldest first for numbering
    sorted_years = sorted(papers_by_year.keys())
    sorted_papers = []
    for year in sorted_years:
        # Reverse the list for each year so oldest comes first
        sorted_papers.extend(reversed(papers_by_year[year]))
    
    # Assign IDs (1 = oldest, highest = newest)
    for idx, paper in enumerate(sorted_papers, 1):
        paper["id"] = f"{prefix} {idx}"
    
    return sorted_papers

# Automatically assign IDs
preprints = assign_ids(preprints, "Preprint")
journals = assign_ids(journals, "Journal")
conferences = assign_ids(conferences, "Conference")

# Also assign IDs to first_author_publications and co_author_publications
# Group by type (Conference, Preprint, Journal) and assign IDs
for org_key in first_author_publications:
    papers = first_author_publications[org_key]
    # Group by type
    by_type = {"Conference": [], "Preprint": [], "Journal": []}
    for paper in papers:
        paper_type = get_paper_type(paper["venue"])
        by_type[paper_type].append(paper)
    
    # Assign IDs for each type
    for paper_type, paper_list in by_type.items():
        if paper_list:
            assign_ids(paper_list, paper_type)

for org_key in co_author_publications:
    papers = co_author_publications[org_key]
    # Group by type
    by_type = {"Conference": [], "Preprint": [], "Journal": []}
    for paper in papers:
        paper_type = get_paper_type(paper["venue"])
        by_type[paper_type].append(paper)
    
    # Assign IDs for each type
    for paper_type, paper_list in by_type.items():
        if paper_list:
            assign_ids(paper_list, paper_type)

# Organization names mapping
org_names = {
    "at_peking_university": "At Peking University",
    "at_bytedance_seed": "At ByteDance Seed",
    "at_washington_university": "At University of Washington",
    "at_deepseek": "At DeepSeek",
    "as_independent_researcher": "As Independent Researcher"
}

# Prepare organization-based view data
def prepare_org_view():
    org_view_data = {}
    
    # First author publications
    for org_key, papers in first_author_publications.items():
        if org_key not in org_view_data:
            org_view_data[org_key] = []
        org_view_data[org_key].extend(papers)
    
    # Co-author publications
    for org_key, papers in co_author_publications.items():
        if org_key not in org_view_data:
            org_view_data[org_key] = []
        org_view_data[org_key].extend(papers)
    
    return org_view_data

org_view_data = prepare_org_view()

# Print the generated Markdown
# Output to _pages directory
with open("../_pages/publications.md", "w") as fout:
    fout.write("""---
title: "Publications"
permalink: /publications/
author_profile: true
---

<!-- See a full list on  [Google Scholar](https://scholar.google.com/citations?user=_7Q8uIYAAAAJ&hl=en)   -->

<style>
.view-toggle {
    margin-bottom: 20px;
    display: flex;
    gap: 10px;
}
.view-toggle button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    border: 2px solid #007bff;
    background-color: white;
    color: #007bff;
    border-radius: 5px;
    transition: all 0.3s;
}
.view-toggle button:hover {
    background-color: #f0f0f0;
}
.view-toggle button.active {
    background-color: #007bff;
    color: white;
}
.publication-view {
    display: none;
}
.publication-view.active {
    display: block;
}
</style>

<div class="view-toggle">
    <button onclick="showView('type')" id="btn-type">By Type & Time</button>
    <button onclick="showView('org')" id="btn-org" class="active">By Organization & Contribution</button>
</div>

<div id="view-type" class="publication-view">
    <h2>Preprints</h2>
""")
    
    # Render preprints (newest first)
    fout.write(template.render(papers=list(reversed(preprints))))
    
    fout.write("""
    <h2>Journals</h2>
""")
    
    # Render journals (newest first)
    fout.write(template.render(papers=list(reversed(journals))))
    
    fout.write("""
    <h2>Conferences</h2>
""")
    
    # Render conferences (newest first)
    fout.write(template.render(papers=list(reversed(conferences))))
    
    fout.write("""
</div>

<div id="view-org" class="publication-view active">
""")
    
    # Render organization-based view
    # Order: ByteDance Seed (1st), DeepSeek (2nd), University of Washington (3rd), Peking University (4th), Independent Researcher (last)
    for org_key in ["at_bytedance_seed", "at_deepseek", "at_washington_university", "at_peking_university", "as_independent_researcher"]:
        org_name = org_names[org_key]
        first_author_papers = first_author_publications[org_key]
        co_author_papers = co_author_publications[org_key]
        
        if first_author_papers or co_author_papers:
            fout.write(f"<h2>{org_name}</h2>")
            
            if first_author_papers:
                fout.write("<h3>First Author</h3>")
                # Sort by year descending (newest first), then by type
                sorted_papers = sorted(first_author_papers, key=lambda p: (int(p["year"]), get_paper_type(p["venue"])), reverse=True)
                fout.write(template_org.render(papers=sorted_papers))
            
            if co_author_papers:
                fout.write("<h3>Co-Author</h3>")
                # Sort by year descending (newest first), then by type
                sorted_papers = sorted(co_author_papers, key=lambda p: (int(p["year"]), get_paper_type(p["venue"])), reverse=True)
                fout.write(template_org.render(papers=sorted_papers))
    
    fout.write("""
</div>

<script>
function showView(viewType) {
    // Hide all views
    document.getElementById('view-type').classList.remove('active');
    document.getElementById('view-org').classList.remove('active');
    
    // Remove active class from all buttons
    document.getElementById('btn-type').classList.remove('active');
    document.getElementById('btn-org').classList.remove('active');
    
    // Show selected view and activate button
    if (viewType === 'type') {
        document.getElementById('view-type').classList.add('active');
        document.getElementById('btn-type').classList.add('active');
    } else {
        document.getElementById('view-org').classList.add('active');
        document.getElementById('btn-org').classList.add('active');
    }
}
</script>
""")
