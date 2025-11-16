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

<!-- Pinned Projects -->
<h2 style="margin-top: 40px; margin-bottom: 20px; color: #8B0000;">Pinned Projects</h2>
<div id="pinned-projects-container">
    <p style="text-align: center; color: #666;">Loading pinned projects...</p>
</div>

<script>
// GitHub API configuration
const GITHUB_USERNAME = 'KnowingNothing';
const PINNED_CACHE_KEY = 'github_pinned_projects_cache';
const PINNED_CACHE_TIMESTAMP_KEY = 'github_pinned_projects_cache_timestamp';
const CACHE_DURATION = 24 * 60 * 60 * 1000; // 24 hours in milliseconds

// Cache management functions
function getCachedPinnedProjects() {
    try {
        const cached = localStorage.getItem(PINNED_CACHE_KEY);
        const timestamp = localStorage.getItem(PINNED_CACHE_TIMESTAMP_KEY);
        
        if (cached && timestamp) {
            const age = Date.now() - parseInt(timestamp, 10);
            if (age < CACHE_DURATION) {
                return JSON.parse(cached);
            }
        }
    } catch (error) {
        console.warn('Error reading pinned projects cache:', error);
    }
    return null;
}

function setCachedPinnedProjects(repos) {
    try {
        localStorage.setItem(PINNED_CACHE_KEY, JSON.stringify(repos));
        localStorage.setItem(PINNED_CACHE_TIMESTAMP_KEY, Date.now().toString());
    } catch (error) {
        console.warn('Error writing pinned projects cache:', error);
    }
}

// Fetch pinned repositories (using REST API to get top repos by stars)
// Note: GitHub REST API doesn't have a direct endpoint for pinned repos,
// so we fetch all repos and sort by stars to get the most important ones
async function fetchPinnedRepositories() {
    try {
        // Fetch all repositories (owned and contributed)
        const response = await fetch(`https://api.github.com/users/${GITHUB_USERNAME}/repos?sort=stars&per_page=100&type=all`);
        if (!response.ok) {
            throw new Error('Failed to fetch GitHub repositories: ' + response.status);
        }
        const repos = await response.json();
        
        // Filter out forked repositories and sort by stars (descending)
        const sortedRepos = repos
            .filter(repo => !repo.fork)
            .sort((a, b) => b.stargazers_count - a.stargazers_count)
            .slice(0, 6); // Get top 6 repositories
        
        // Update cache
        setCachedPinnedProjects(sortedRepos);
        
        return sortedRepos;
    } catch (error) {
        console.error('Error fetching pinned repositories:', error);
        return [];
    }
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Render project card
function renderProjectCard(repo) {
    const stars = repo.stargazers_count || 0;
    const forks = repo.forks_count || 0;
    const description = escapeHtml(repo.description || 'No description available.');
    const homepage = repo.homepage;
    const name = escapeHtml(repo.name);
    const licenseName = repo.license ? (repo.license.spdx_id || 'License') : null;
    const language = repo.language || '';
    
    return `
        <div class="project-card">
            <div class="project-header">
                <h2 class="project-title">${name}</h2>
                <div class="project-badges">
                    <span class="badge badge-stars">⭐ ${stars} stars</span>
                    ${forks > 0 ? `<span class="badge badge-forks">🍴 ${forks} forks</span>` : ''}
                    ${licenseName ? `<span class="badge badge-license">${escapeHtml(licenseName)}</span>` : ''}
                    ${language ? `<span class="badge badge-language">${escapeHtml(language)}</span>` : ''}
                </div>
            </div>
            
            <div class="project-description">
                <p>${description}</p>
            </div>
            
            <div class="project-links">
                <a href="${repo.html_url}" target="_blank" class="project-link">
                    📦 GitHub Repository
                </a>
                ${homepage ? `<a href="${escapeHtml(homepage)}" target="_blank" class="project-link project-link-secondary">🌐 Website</a>` : ''}
            </div>
        </div>
    `;
}

// Load and display pinned projects
async function loadPinnedProjects() {
    const container = document.getElementById('pinned-projects-container');
    if (!container) {
        console.error('Pinned projects container not found');
        return;
    }
    
    // Try to load from cache first
    const cachedRepos = getCachedPinnedProjects();
    if (cachedRepos && cachedRepos.length > 0) {
        // Display cached data immediately
        container.innerHTML = cachedRepos.map(repo => renderProjectCard(repo)).join('');
        
        // Refresh cache in background
        fetchPinnedRepositories().then(repos => {
            if (repos && repos.length > 0) {
                container.innerHTML = repos.map(repo => renderProjectCard(repo)).join('');
            }
        }).catch(error => {
            console.warn('Background refresh of pinned projects failed:', error);
            // Keep showing cached data
        });
    } else {
        // No cache, show loading and fetch
        container.innerHTML = '<p style="text-align: center; color: #666;">Loading pinned projects...</p>';
        
        try {
            const repos = await fetchPinnedRepositories();
            
            if (repos.length === 0) {
                container.innerHTML = '<p style="text-align: center; color: #666;">No pinned projects found.</p>';
                return;
            }
            
            container.innerHTML = repos.map(repo => renderProjectCard(repo)).join('');
        } catch (error) {
            console.error('Error loading pinned projects:', error);
            container.innerHTML = '<p style="text-align: center; color: #d32f2f;">Failed to load pinned projects. Please check the console for details.</p>';
        }
    }
}

// Load projects when page is ready
(function() {
    // Wait for the container to exist
    function init() {
        const container = document.getElementById('pinned-projects-container');
        if (container) {
            loadPinnedProjects();
        } else {
            // Retry after a short delay
            setTimeout(init, 100);
        }
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        // Page already loaded, try immediately
        init();
    }
})();
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

