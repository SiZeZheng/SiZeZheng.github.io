---
layout: single
title: "Open Source Projects"
permalink: /projects/
author_profile: true
---

{% include base_path %}

<!-- Featured Project: Triton-distributed -->
<div class="project-card featured-project">
    <div class="project-header">
        <h2 class="project-title">Triton-distributed</h2>
        <div class="project-badges">
            <span class="badge badge-stars">⭐ 1.2k stars</span>
            <span class="badge badge-license">MIT License</span>
        </div>
    </div>
    
    <div class="project-description">
        <p>
            <strong>Triton-distributed</strong> is a distributed compiler based on Triton for parallel systems. 
            It provides a set of easy-to-use primitives to support the development of distributed compute-communication 
            overlapping kernels, enabling efficient parallel computation on modern AI systems.
        </p>
        <p>
            The project offers both low-level and high-level primitives for programming communication kernels, 
            allowing users to easily combine communication with computation to design overlapping kernels. 
            Triton-distributed can achieve comparable or better performance than hand-tuned libraries.
        </p>
    </div>
    
    <div class="project-image-container" style="text-align: center; margin: 20px 0;">
        <img src="{{ base_path }}/images/triton-distributed-overview.png" alt="Triton-distributed Overview" class="project-image" 
             onerror="this.onerror=null; this.style.display='none'; document.getElementById('image-placeholder').style.display='block';">
        <p id="image-placeholder" style="display: none; text-align: center; color: #666; font-size: 0.9em; margin-top: 20px; padding: 20px; background-color: #f8f9fa; border-radius: 5px; border: 2px dashed #dee2e6;">
            <em>📷 Add your overview image at: <code>images/triton-distributed-overview.png</code></em>
        </p>
    </div>
    
    <div class="project-features">
        <h3>Key Features</h3>
        <ul>
            <li>Low-level primitives for distributed compute-communication overlapping kernels</li>
            <li>Support for single-node and cross-node operations (GEMM, MoE, Flash-Decoding)</li>
            <li>High performance: comparable or better than hand-tuned libraries</li>
            <li>Easy-to-use API for programming communication kernels</li>
            <li>Support for multiple backends (NVIDIA, AMD GPUs)</li>
            <li>Comprehensive documentation and tutorials</li>
        </ul>
    </div>
    
    <div class="project-links">
        <a href="https://github.com/ByteDance-Seed/Triton-distributed" target="_blank" class="project-link">
            📦 GitHub Repository
        </a>
        <a href="https://triton-distributed.readthedocs.io/en/latest/" target="_blank" class="project-link project-link-secondary">
            📚 Documentation
        </a>
    </div>
</div>

<!-- Other Projects -->
<h2 style="margin-top: 40px; margin-bottom: 20px; color: #8B0000;">Other Open Source Projects</h2>

<!-- FlexTensor -->
<div class="project-card">
    <div class="project-header">
        <h2 class="project-title">FlexTensor</h2>
        <div class="project-badges" id="flextensor-badges">
            <span class="badge badge-stars">⭐ Loading...</span>
            <span class="badge badge-license">MIT License</span>
        </div>
    </div>
    <div class="project-description">
        <p>
            <strong>FlexTensor</strong> is an automatic schedule exploration and optimization framework for tensor computation on heterogeneous systems. 
            It can optimize tensor computation programs without human interference, allowing programmers to only work on high-level programming abstraction 
            without considering the hardware platform details.
        </p>
        <p>
            FlexTensor systematically explores the optimization design spaces that are composed of many different schedules for different hardware. 
            Then, FlexTensor combines different exploration techniques, including heuristic method and machine learning method to find the optimized schedule configuration.
        </p>
    </div>
    <div class="project-links">
        <a href="https://github.com/pku-liang/FlexTensor" target="_blank" class="project-link">
            📦 GitHub Repository
        </a>
    </div>
</div>

<!-- compiler-and-arch -->
<div class="project-card">
    <div class="project-header">
        <h2 class="project-title">compiler-and-arch</h2>
        <div class="project-badges" id="compiler-arch-badges">
            <span class="badge badge-stars">⭐ Loading...</span>
        </div>
    </div>
    <div class="project-description">
        <p>
            <strong>compiler-and-arch</strong> is a curated list of tutorials, papers, talks, and open-source projects for emerging compiler and architecture research. 
            This repository serves as a comprehensive resource for researchers and practitioners interested in compiler design and computer architecture.
        </p>
    </div>
    <div class="project-links">
        <a href="https://github.com/KnowingNothing/compiler-and-arch" target="_blank" class="project-link">
            📦 GitHub Repository
        </a>
    </div>
</div>

<!-- AMOS -->
<div class="project-card">
    <div class="project-header">
        <h2 class="project-title">AMOS</h2>
        <div class="project-badges" id="amos-badges">
            <span class="badge badge-stars">⭐ Loading...</span>
        </div>
    </div>
    <div class="project-description">
        <p>
            <strong>AMOS</strong> (Automatic Mapping Generation, Verification, and Exploration for ISA-based Spatial Accelerators) is a framework for automatic mapping generation and optimization for spatial accelerators. 
            It provides tools for exploring and optimizing mappings for various hardware accelerators.
        </p>
    </div>
    <div class="project-links">
        <a href="https://github.com/pku-liang/AMOS" target="_blank" class="project-link">
            📦 GitHub Repository
        </a>
    </div>
</div>

<!-- MatmulTutorial -->
<div class="project-card">
    <div class="project-header">
        <h2 class="project-title">MatmulTutorial</h2>
        <div class="project-badges" id="matmul-badges">
            <span class="badge badge-stars">⭐ Loading...</span>
        </div>
    </div>
    <div class="project-description">
        <p>
            <strong>MatmulTutorial</strong> is an easy-to-understand TensorOp Matmul tutorial that provides comprehensive guides for understanding matrix multiplication operations on modern accelerators. 
            It offers detailed explanations and examples for implementing efficient matrix multiplication kernels.
        </p>
    </div>
    <div class="project-links">
        <a href="https://github.com/KnowingNothing/MatmulTutorial" target="_blank" class="project-link">
            📦 GitHub Repository
        </a>
    </div>
</div>

<script>
// Load GitHub stats for projects (optional, non-blocking)
async function loadProjectStats() {
    const projects = [
        { repo: 'pku-liang/FlexTensor', badgeId: 'flextensor-badges' },
        { repo: 'KnowingNothing/compiler-and-arch', badgeId: 'compiler-arch-badges' },
        { repo: 'pku-liang/AMOS', badgeId: 'amos-badges' },
        { repo: 'KnowingNothing/MatmulTutorial', badgeId: 'matmul-badges' }
    ];
    
    projects.forEach(async ({ repo, badgeId }) => {
        try {
            const response = await fetch(`https://api.github.com/repos/${repo}`);
            if (response.ok) {
                const data = await response.json();
                const stars = data.stargazers_count || 0;
                const forks = data.forks_count || 0;
                const license = data.license ? data.license.spdx_id : null;
                const language = data.language || '';
                const badgeEl = document.getElementById(badgeId);
                if (badgeEl) {
                    let html = `<span class="badge badge-stars">⭐ ${stars} stars</span>`;
                    if (forks > 0) {
                        html += `<span class="badge badge-forks">🍴 ${forks} forks</span>`;
                    }
                    if (license) {
                        html += `<span class="badge badge-license">${license}</span>`;
                    }
                    if (language) {
                        html += `<span class="badge badge-language">${language}</span>`;
                    }
                    badgeEl.innerHTML = html;
                }
            }
        } catch (error) {
            console.warn(`Failed to load stats for ${repo}:`, error);
        }
    });
}

// Load stats in background (non-blocking)
loadProjectStats();
</script>

<style>
.project-card {
    margin-bottom: 40px;
    padding: 20px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    background-color: #fafafa;
}

.featured-project {
    border: 2px solid #8B0000;
    background-color: #fff;
}

.project-header {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
    gap: 15px;
}

.project-title {
    font-size: 24px;
    font-weight: bold;
    color: #8B0000;
    margin: 0;
}

.project-badges {
    display: flex;
    gap: 10px;
    align-items: center;
    flex-wrap: wrap;
}

.badge {
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: bold;
}

.badge-stars {
    background-color: #f1f8ff;
    color: #0366d6;
    border: 1px solid #c8e1ff;
}

.badge-license {
    background-color: #f6f8fa;
    color: #586069;
    border: 1px solid #d1d5da;
}

.badge-forks {
    background-color: #fff5f5;
    color: #c53030;
    border: 1px solid #fed7d7;
}

.badge-language {
    background-color: #f0f8ff;
    color: #0066cc;
    border: 1px solid #b3d9ff;
}

.project-image {
    width: 100%;
    max-width: 800px;
    margin: 20px auto;
    display: block;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.project-description {
    font-size: 16px;
    line-height: 1.6;
    color: #333;
    margin-bottom: 15px;
}

.project-links {
    display: flex;
    gap: 15px;
    flex-wrap: wrap;
    margin-top: 15px;
}

.project-link {
    display: inline-flex;
    align-items: center;
    padding: 8px 16px;
    background-color: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 5px;
    font-weight: 500;
    transition: background-color 0.3s;
}

.project-link:hover {
    background-color: #0056b3;
}

.project-link-secondary {
    background-color: #6c757d;
}

.project-link-secondary:hover {
    background-color: #545b62;
}

.project-features {
    margin-top: 20px;
}

.project-features h3 {
    font-size: 18px;
    color: #8B0000;
    margin-bottom: 10px;
}

.project-features ul {
    list-style-type: none;
    padding-left: 0;
}

.project-features li {
    padding: 5px 0;
    padding-left: 25px;
    position: relative;
}

.project-features li:before {
    content: "✓";
    position: absolute;
    left: 0;
    color: #28a745;
    font-weight: bold;
}
</style>

