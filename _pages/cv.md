---
layout: single
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
---

{% include base_path %}

<div style="text-align: center; margin: 20px 0;">
    <button id="download-cv-btn" onclick="downloadCV()" 
            style="background-color: #8B0000; color: white; padding: 15px 30px; border: none; border-radius: 8px; font-size: 18px; font-weight: bold; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: all 0.3s;">
        📥 Download CV as PDF
    </button>
    <p style="margin-top: 10px; color: #666; font-size: 14px;">Or use your browser's print function (Ctrl+P / Cmd+P) to save as PDF</p>
</div>

<div id="cv-content">
    <!-- About Section -->
    <section id="about-section">
        <h1>Size Zheng</h1>
        
        <p>I lead the <a href="https://github.com/ByteDance-Seed/Triton-distributed">Triton-distributed</a> project at ByteDance Seed.</p>
        
        <p>I completed my Ph.D. in the School of CS at Peking University, where I was advised by <a href="https://ericlyun.github.io/">Prof. Yun Liang</a>. 
        I worked with Professor <a href="https://homes.cs.washington.edu/~luisceze/">Luis Ceze</a> on LLM serving and optimization from September 2023 to January 2024 as visiting Ph.D. in <a href="https://sampl.cs.washington.edu/">SAMPL</a> at the University of Washington.
        After this, I worked at DeepSeek AI for a short term as research intern.
        At 2024, I joined ByteDance Seed as Machine Learning System Researcher Scientist.</p>
        
        <p>My recent publications investigate new algorithms, abstractions, and frameworks for efficient training and inference on CPU and GPU. My research has been recognized with MICRO, ASPLOS, ISCA, HPCA, TPDS, DAC, and MLSys. I received my B.S. degree in the department of Computer Intelligence Science at Peking University.</p>
        
        <p>I am PC member of ChinaSys; reviewer of TPDS and TACO; sub-reviewer of MICRO, PPoPP, MLSys, ICS, and ICCAD.</p>
        
        <p><strong>Email:</strong> zheng.size [AT] bytedance.com or zhengsz [AT] pku.edu.cn or zhengsz [AT] mail.tsinghua.edu.cn</p>
        
        <h2>Research Interests</h2>
        <ul>
            <li><strong>High-performance Inference System:</strong> System design for large language and vision models</li>
            <li><strong>AI Compiler:</strong> Compiler Design for the next generation of accelerators</li>
            <li><strong>Distributed Systems:</strong> Computation-communication co-optimization and automation</li>
        </ul>
        
        <h2>Awards</h2>
        <ul>
            <li><strong>July 2024</strong> Outstanding Doctoral Dissertation Award of Peking University</li>
            <li><strong>July 2024</strong> Outstanding Ph.D. Graduate of both Beijing and Peking University</li>
        </ul>
    </section>
    
    <!-- Publications Section -->
    <section id="publications-section">
        <h2>Publications</h2>
        <div id="publications-content">
            <p>Loading publications...</p>
        </div>
    </section>
    
    <!-- Projects Section -->
    <section id="projects-section">
        <h2>Open Source Projects</h2>
        <div id="projects-content">
            <p>Loading projects...</p>
        </div>
    </section>
</div>

<style>
#cv-content {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    line-height: 1.6;
}

#cv-content section {
    margin-bottom: 40px;
    page-break-inside: avoid;
}

#cv-content h1 {
    font-size: 32px;
    margin-bottom: 20px;
    color: #8B0000;
    border-bottom: 3px solid #8B0000;
    padding-bottom: 10px;
}

#cv-content h2 {
    font-size: 24px;
    margin-top: 30px;
    margin-bottom: 15px;
    color: #8B0000;
    border-bottom: 2px solid #8B0000;
    padding-bottom: 5px;
}

#cv-content h3 {
    font-size: 18px;
    margin-top: 20px;
    margin-bottom: 10px;
    color: #333;
}

#cv-content ul {
    margin-left: 20px;
    margin-bottom: 15px;
}

#cv-content li {
    margin-bottom: 8px;
}

#cv-content a {
    color: #007bff;
    text-decoration: none;
}

#cv-content a:hover {
    text-decoration: underline;
}

#cv-content .project-card {
    margin-bottom: 20px;
    padding: 15px;
    border: 1px solid #e0e0e0;
    border-radius: 5px;
    background-color: #fafafa;
}

@media print {
    #cv-content {
        padding: 0;
    }
    
    #cv-content section {
        page-break-inside: avoid;
    }
}
</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>

<script>
// Load publications content
async function loadPublications() {
    try {
        const response = await fetch('{{ base_path }}/publications/');
        const html = await response.text();
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        
        // Extract publications content - get the "By Organization & Contribution" view
        const viewOrg = doc.querySelector('#view-org');
        if (viewOrg) {
            const content = viewOrg.cloneNode(true);
            // Remove buttons and other interactive elements
            content.querySelectorAll('.view-toggle, button, script').forEach(el => el.remove());
            document.getElementById('publications-content').innerHTML = content.innerHTML;
        } else {
            // Fallback: get main content
            const mainContent = doc.querySelector('.page__content') || doc.querySelector('main') || doc.querySelector('article');
            if (mainContent) {
                const content = mainContent.cloneNode(true);
                const navElements = content.querySelectorAll('nav, .masthead, .page__footer, script, style, .view-toggle, button');
                navElements.forEach(el => el.remove());
                document.getElementById('publications-content').innerHTML = content.innerHTML;
            } else {
                document.getElementById('publications-content').innerHTML = '<p>Publications content could not be loaded.</p>';
            }
        }
    } catch (error) {
        console.error('Error loading publications:', error);
        document.getElementById('publications-content').innerHTML = '<p>Error loading publications. Please visit the <a href="{{ base_path }}/publications/">Publications page</a>.</p>';
    }
}

// Load projects content
async function loadProjects() {
    try {
        // Wait a bit for dynamic content to load on projects page
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        const response = await fetch('{{ base_path }}/projects/');
        const html = await response.text();
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        
        // Extract projects content
        const mainContent = doc.querySelector('.page__content') || doc.querySelector('main') || doc.querySelector('article');
        if (mainContent) {
            const content = mainContent.cloneNode(true);
            // Remove navigation, scripts, and interactive elements
            const navElements = content.querySelectorAll('nav, .masthead, .page__footer, script, style');
            navElements.forEach(el => el.remove());
            
            // Get pinned projects container
            const pinnedContainer = content.querySelector('#pinned-projects-container');
            if (pinnedContainer && !pinnedContainer.innerHTML.includes('Loading')) {
                document.getElementById('projects-content').innerHTML = content.innerHTML;
            } else {
                // If still loading, show a message
                document.getElementById('projects-content').innerHTML = '<p>Loading projects... Please refresh the page if projects do not appear.</p>';
                // Try again after a delay
                setTimeout(loadProjects, 3000);
            }
        } else {
            document.getElementById('projects-content').innerHTML = '<p>Projects content could not be loaded.</p>';
        }
    } catch (error) {
        console.error('Error loading projects:', error);
        document.getElementById('projects-content').innerHTML = '<p>Error loading projects. Please visit the <a href="{{ base_path }}/projects/">Projects page</a>.</p>';
    }
}

// Download CV as PDF
async function downloadCV() {
    const button = document.getElementById('download-cv-btn');
    const originalText = button.textContent;
    button.textContent = 'Generating PDF...';
    button.disabled = true;
    
    try {
        // Ensure all content is loaded
        await loadPublications();
        await loadProjects();
        await new Promise(resolve => setTimeout(resolve, 3000)); // Wait for dynamic content
        
        const { jsPDF } = window.jspdf;
        const element = document.getElementById('cv-content');
        
        // Hide the download button for PDF
        const downloadBtn = document.querySelector('#download-cv-btn').parentElement;
        const originalDisplay = downloadBtn.style.display;
        downloadBtn.style.display = 'none';
        
        // Use html2canvas to capture the content
        const canvas = await html2canvas(element, {
            scale: 2,
            useCORS: true,
            logging: false,
            windowWidth: element.scrollWidth,
            windowHeight: element.scrollHeight,
            backgroundColor: '#ffffff'
        });
        
        // Restore button
        downloadBtn.style.display = originalDisplay;
        
        const imgData = canvas.toDataURL('image/png');
        const pdf = new jsPDF('p', 'mm', 'a4');
        
        const pdfWidth = pdf.internal.pageSize.getWidth();
        const pdfHeight = pdf.internal.pageSize.getHeight();
        const imgWidth = canvas.width;
        const imgHeight = canvas.height;
        const ratio = pdfWidth / imgWidth;
        const imgScaledWidth = imgWidth * ratio;
        const imgScaledHeight = imgHeight * ratio;
        
        // Calculate how many pages we need
        const totalPages = Math.ceil(imgScaledHeight / pdfHeight);
        
        for (let i = 0; i < totalPages; i++) {
            if (i > 0) {
                pdf.addPage();
            }
            const yPosition = -(i * pdfHeight * (imgScaledHeight / imgScaledWidth));
            pdf.addImage(imgData, 'PNG', 0, yPosition, imgScaledWidth, imgScaledHeight);
        }
        
        pdf.save('Size_Zheng_CV.pdf');
        
        button.textContent = originalText;
        button.disabled = false;
    } catch (error) {
        console.error('Error generating PDF:', error);
        alert('Error generating PDF. Please try again or use the browser\'s print function (Ctrl+P / Cmd+P) to save as PDF.');
        button.textContent = originalText;
        button.disabled = false;
    }
}

// Load content when page is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        loadPublications();
        loadProjects();
    });
} else {
    loadPublications();
    loadProjects();
}
</script>
