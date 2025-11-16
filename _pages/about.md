---
permalink: /
title: "About"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<div style="text-align: center; margin: 30px 0;">
    <a href="{{ base_path }}/cv/" onclick="event.preventDefault(); window.location.href='{{ base_path }}/cv/';" 
       style="display: inline-block; background-color: #8B0000; color: white; padding: 15px 30px; border-radius: 8px; text-decoration: none; font-size: 18px; font-weight: bold; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: all 0.3s;">
        📄 Download CV (PDF)
    </a>
</div>

<!-- I am now machine learning system researcher scientist at ByteDance. I am in TopSeed program. -->
<!-- I am also PostDoc at Tsinghua University and work with Professor [Jidong Zhai](https://pacman.cs.tsinghua.edu.cn/~zjd/) on distributed machine learning compilers for LLMs. -->
I lead the [Triton-distributed](https://github.com/ByteDance-Seed/Triton-distributed) project at ByteDance Seed.

<!-- I am also going to take the ByteDance-Tsinghua postdoc program by the end of 2024. -->
I completed my Ph.D. in the School of CS at Peking University, where I was advised by [Prof. Yun Liang](https://ericlyun.github.io/). 
I worked with Professor [Luis Ceze](https://homes.cs.washington.edu/~luisceze/) on LLM serving and optimization from September 2023 to January 2024 as visiting Ph.D. in [SAMPL](https://sampl.cs.washington.edu/) at the University of Washington.
After this, I worked at DeepSeek AI for a short term as research intern.
At 2024, I joined ByteDance Seed as Machine Learning System Researcher Scientist.
My recent publications investigate new algorithms, abstractions, and frameworks for efficient training and inference on CPU and GPU. My research has been recognized with MICRO, ASPLOS, ISCA, HPCA, TPDS, DAC, and MLSys. I received my B.S. degree in the department of Computer Intelligence Science at Peking University.
I am PC member of ChinaSys; reviewer of TPDS and TACO; sub-reviewer of MICRO, PPoPP, MLSys, ICS, and ICCAD.


Email: zheng.size [AT] outlook.com

<!-- <span style="color: red;"><strong>I am seeking highly motivated full-time employees and research interns. If interested, please contact me directly!</strong></span>  -->


# Research Interests

<style>
  /* 美化研究兴趣列表样式 */
  .interests-list {
    list-style-type: none; /* 移除默认的列表样式 */
    padding: 0;
  }
  .interests-list li {
    margin-bottom: 0px; /* 增加每条研究兴趣之间的间距 */
    padding: 10px;
    border-left: 0px solid black; /* 添加左侧边框 */
    background-color: #f8f9fa; /* 添加背景颜色 */
    border-radius: 0px; /* 添加圆角 */
  }
  .interests-list li strong {
    color: black; /* 设置研究兴趣标题颜色 */
  }
</style>

<ul class="interests-list">
  <li><strong>High-performance Inference System:</strong> System design for large language and vision models </li>
  <li><strong>AI Compiler:</strong> Compiler Design for the next generation of accelerators </li>
  <li><strong>Distributed Systems:</strong> Computation-communication co-optimization and automation </li>
</ul>

# Awards

<style>
  /* 美化奖项列表样式 */
  .awards-list {
    list-style-type: none; /* 移除默认的列表样式 */
    padding: 0;
  }
  .awards-list li {
    margin-bottom: 15px; /* 增加每条奖项之间的间距 */
    padding: 10px;
    border-left: 4px solid black; /* 添加左侧边框 */
    background-color: #f8f9fa; /* 添加背景颜色 */
    border-radius: 4px; /* 添加圆角 */
  }
  .awards-list li strong {
    color: black; /* 设置奖项日期颜色 */
  }
</style>

<ul class="awards-list">
  <li><strong>July 2024</strong> Outstanding Doctoral Dissertation Award of Peking University</li>
  <li><strong>July 2024</strong> Outstanding Ph.D. Graduate of both Beijing and Peking University</li>
</ul>

<!-- # Research Interests
<!-- My research interest is at distributed system, LLM inference/serving optimization, high-performance computing for machine learning, optimizing compiler design, and code generation. -->
<!-- <ul>
  <li><strong>High-performance Inference System:</strong> System design for large language and vision models </li>
  <li><strong>AI Compiler:</strong> Compiler Design for the next generation of accelerators </li>
  <li><strong>Distributed Systems:</strong> Computation-communication co-optimization and automation </li>
</ul> -->


<!-- # Awards

<ul>
  <li><strong>July 2024</strong> - Outstanding Doctoral Dissertation Award of Peking University</li>
  <li><strong>July 2024</strong> - Outstanding Ph.D. Graduate of both Beijing and Peking University</li>
</ul> -->


<!-- # News

<ul>
  <li><strong>September 2024</strong> - Our paper <span style="color: red;">ArkVale: Efficient Generative LLM Inference with Recallable Key-Value Eviction</span> has been accepted by NeurIPS 2024!</li>
  <li><strong>August 2024</strong> - Join ByteDance as TopSeed researcher </li>
</ul> -->
# News

<style>
  /* 美化新闻列表样式 */
  .news-list {
    list-style-type: none; /* 移除默认的列表样式 */
    padding: 0;
  }
  .news-list li {
    margin-bottom: 15px; /* 增加每条新闻之间的间距 */
    padding: 10px;
    border-left: 4px solid black; /* 添加左侧边框 */
    background-color: #f8f9fa; /* 添加背景颜色 */
    border-radius: 4px; /* 添加圆角 */
  }
  .news-list li strong {
    color: black; /* 设置日期颜色 */
  }
  .news-list li span {
    color: red; /* 设置论文标题颜色 */
    font-weight: bold; /* 设置论文标题加粗 */
  }
</style>

<ul class="news-list">
  <li><strong>May 2025</strong> Our project <span>Triton-distributed</span> has been released</li>
  <li><strong>May 2025</strong> Our papers <span>ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference</span> and <span>MxMoE: Mixed-precision Quantization for MoE with Accuracy and Performance Co-Design</span> have been accepted by ICML 2025!</li>
  <li><strong>March 2025</strong> Our paper <span>Qtenon: Towards Low-Latency Architecture Integration for Accelerating Hybrid Quantum-Classical Computing</span> has been accepted by ISCA 2025!</li>
  <li><strong>Februray 2025</strong> Our paper <span>Comet: Fine-grained Computation-communication
  Overlapping for Mixture-of-Experts</span> has been accepted by MLSys 2025!</li>
  <li><strong>Februray 2025</strong> Our paper <span>TileLink: Generating Efficient Compute-Communication Overlapping Kernels using Tile-Centric Primitives</span> has been accepted by MLSys 2025!</li>
  <!-- <li><strong>January 2025</strong> Join Tsinghua-ByteDance Joint PostDoc Program </li> -->
  <li><strong>December 2024</strong> Visit Vinod at Nvidia Redmond and give a technique talk </li>
  <li><strong>September 2024</strong> Our paper <span>ArkVale: Efficient Generative LLM Inference with Recallable Key-Value Eviction</span> has been accepted by NeurIPS 2024!</li>
  <!-- <li><strong>August 2024</strong> Join ByteDance as TopSeed researcher </li> -->
</ul>
<!-- <ul>
  <li><strong>September 2024</strong> - Our paper **ArkVale: Efficient Generative LLM Inference with Recallable Key-Value Eviction** has been accepted by NeurIPS 2024!</li>
  <li><strong>August 2024</strong> - Join ByteDance as TopSeed researcher </li>
</ul> -->
