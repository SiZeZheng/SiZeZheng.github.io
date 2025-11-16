---
layout: single
title: ""
permalink: /cv/
author_profile: false
---

{% include base_path %}

<style>
/* Hide page title header and site title in masthead for CV page */
.page__title,
.page__inner-wrap header h1,
.masthead__menu-item--lg a {
    display: none !important;
}

/* Custom CV header with download URL (top right) */
.cv-header {
    text-align: right;
    font-size: 10pt;
    color: #666;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid #e0e0e0;
    font-family: "Times New Roman", Times, serif;
}

.cv-header a {
    color: #007bff;
    text-decoration: none;
}

.cv-header a:hover {
    text-decoration: underline;
}
</style>

<div class="cv-header">
    Download this CV: <a href="{{ base_path }}/cv/">https://sizezheng.github.io/cv/</a>
</div>

<!-- Load PDF generation libraries -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>

<!-- CV Download Function - Inline to avoid loading issues -->
<script>
// Immediate test - verify script execution
console.log('=== CV Download Script Starting ===');
console.log('Script execution test');

// Wrap everything in try-catch to catch any errors
try {

// Wait for libraries to load
function waitForLibraries(maxWait = 5000) {
    return new Promise((resolve, reject) => {
        const startTime = Date.now();
        const checkLibraries = () => {
            if (window.jspdf && window.html2canvas) {
                resolve();
            } else if (Date.now() - startTime > maxWait) {
                reject(new Error('PDF generation libraries not loaded'));
            } else {
                setTimeout(checkLibraries, 100);
            }
        };
        checkLibraries();
    });
}

// Download CV as PDF
window.downloadCV = async function downloadCV() {
    const button = document.getElementById('download-cv-btn');
    if (!button) {
        alert('Download button not found. Please refresh the page.');
        return;
    }
    
    const originalText = button.textContent;
    button.textContent = 'Generating PDF...';
    button.disabled = true;
    
    try {
        await waitForLibraries();
        
        if (!window.jspdf || !window.html2canvas) {
            throw new Error('PDF generation libraries not loaded');
        }
        
        const { jsPDF } = window.jspdf;
        const element = document.getElementById('cv-content');
        
        if (!element) {
            throw new Error('CV content not found');
        }
        
        // Hide download button
        const downloadBtnContainer = button.parentElement;
        const originalDisplay = downloadBtnContainer ? downloadBtnContainer.style.display : '';
        if (downloadBtnContainer) {
            downloadBtnContainer.style.display = 'none';
        }
        
        // Wait for images to load
        const images = element.querySelectorAll('img');
        await Promise.all(Array.from(images).map(img => {
            if (img.complete && img.naturalHeight !== 0) return Promise.resolve();
            return new Promise((resolve) => {
                img.onload = resolve;
                img.onerror = resolve;
                setTimeout(resolve, 2000);
            });
        }));
        
        await new Promise(resolve => setTimeout(resolve, 300));
        
        // Capture with html2canvas
        const canvas = await html2canvas(element, {
            scale: 2,
            useCORS: true,
            logging: false,
            backgroundColor: '#ffffff',
            allowTaint: false,
            width: element.scrollWidth,
            height: element.scrollHeight
        });
        
        // Restore button
        if (downloadBtnContainer) {
            downloadBtnContainer.style.display = originalDisplay;
        }
        
        // Create PDF
        const pdf = new jsPDF('p', 'mm', 'a4');
        const pdfWidth = pdf.internal.pageSize.getWidth();
        const pdfHeight = pdf.internal.pageSize.getHeight();
        
        const imgWidth = canvas.width;
        const imgHeight = canvas.height;
        
        // Convert to mm: 1px = 0.2646mm (at 96 DPI)
        const pxToMm = 25.4 / 96;
        const elementWidth = element.scrollWidth;
        const elementHeight = element.scrollHeight;
        const canvasScale = imgWidth / elementWidth;
        
        const elementWidthMM = elementWidth * pxToMm;
        const elementHeightMM = elementHeight * pxToMm;
        const scale = pdfWidth / elementWidthMM;
        const scaledWidthMM = elementWidthMM * scale;
        const scaledHeightMM = elementHeightMM * scale;
        
        // Add pages
        let currentY = 0;
        let pageNum = 0;
        
        while (currentY < scaledHeightMM) {
            if (pageNum > 0) {
                pdf.addPage();
            }
            
            const pageEndY = Math.min(currentY + pdfHeight, scaledHeightMM);
            const sourceY = (currentY / scaledHeightMM) * imgHeight;
            const pageHeightPx = ((pageEndY - currentY) / scaledHeightMM) * imgHeight;
            const destHeightMM = pageEndY - currentY;
            
            // Create page canvas
            const pageCanvas = document.createElement('canvas');
            pageCanvas.width = imgWidth;
            pageCanvas.height = Math.ceil(pageHeightPx);
            const pageCtx = pageCanvas.getContext('2d');
            
            pageCtx.fillStyle = '#ffffff';
            pageCtx.fillRect(0, 0, pageCanvas.width, pageCanvas.height);
            pageCtx.drawImage(canvas, 0, sourceY, imgWidth, pageHeightPx, 0, 0, imgWidth, pageHeightPx);
            
            const pageImgData = pageCanvas.toDataURL('image/jpeg', 0.95);
            pdf.addImage(pageImgData, 'JPEG', 0, 0, scaledWidthMM, destHeightMM);
            
            currentY = pageEndY;
            pageNum++;
        }
        
        pdf.save('Size_Zheng_CV.pdf');
        
        button.textContent = originalText;
        button.disabled = false;
    } catch (error) {
        console.error('Error generating PDF:', error);
        alert('Error generating PDF: ' + error.message);
        
        const downloadBtnContainer = button.parentElement;
        if (downloadBtnContainer) {
            downloadBtnContainer.style.display = '';
        }
        
        button.textContent = originalText;
        button.disabled = false;
    }
};

console.log('=== CV Download Script Loaded ===');

} catch(e) {
    console.error('FATAL ERROR in CV download script:', e);
    console.error('Error stack:', e.stack);
    alert('FATAL ERROR: Script failed to load. Error: ' + e.message + '\n\nCheck console for details.');
}
</script>

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
                const license = data.license ? data.license.spdx_id : null;
                const badgeEl = document.getElementById(badgeId);
                if (badgeEl) {
                    let html = `<span class="badge badge-stars">⭐ ${stars} stars</span>`;
                    if (license) {
                        html += `<span class="badge badge-license">${license}</span>`;
                    }
                    badgeEl.innerHTML = html;
                }
            }
        } catch (error) {
            console.warn(`Failed to load stats for ${repo}:`, error);
        }
    });
}

// Load project stats in background (non-blocking, optional)
// Wait for DOM to be ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadProjectStats);
} else {
    loadProjectStats();
}
</script>

<div style="text-align: center; margin: 20px 0;">
    <button id="download-cv-btn" onclick="if(typeof window.downloadCV==='function'){window.downloadCV();}else{alert('Please wait for the page to fully load, then try again.');}"
            style="background-color: #8B0000; color: white; padding: 15px 30px; border: none; border-radius: 8px; font-size: 18px; font-weight: bold; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        📥 Download CV as PDF
    </button>
    <p style="margin-top: 10px; color: #666; font-size: 14px;">Or use your browser's print function (Ctrl+P / Cmd+P) to save as PDF</p>
</div>


<div id="cv-content">
    <!-- About Section - Directly from about.md content -->
    <section id="about-section">
        <div class="about-header">
            <h1>{{ site.author.name }}</h1>
            {% if site.author.avatar %}
            <img src="{{ site.author.avatar | prepend: '/images/' | prepend: base_path }}" alt="Profile Photo" class="profile-image" id="cv-profile-img">
            {% endif %}
        </div>
        
        {% include about-content.html %}
    </section>
    
    <!-- Publications Section - Load from publications page -->
    <section id="publications-section">
        <h2>Publications</h2>
        <div id="publications-content">
            {% include publications-view-org.html %}
        </div>
    </section>
    
    <!-- Projects Section - Load from projects page -->
    <section id="projects-section">
        <h2>Open Source Projects</h2>
        <div id="projects-content">
            {% include projects-content.html %}
        </div>
    </section>
</div>

<style>
#cv-content {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: "Times New Roman", Times, serif;
    font-size: 12pt; /* 小四号字体 */
    line-height: 1.6;
    background-color: #ffffff;
}

#cv-content section {
    margin-bottom: 40px;
    page-break-inside: avoid;
}

/* Prevent page breaks inside individual items */
#cv-content .project-card {
    page-break-inside: avoid;
    break-inside: avoid;
}

#cv-content .about-header {
    page-break-inside: avoid;
    break-inside: avoid;
}

/* Prevent publication items from being split */
#cv-content [style*="margin-bottom: 20px"] {
    page-break-inside: avoid;
    break-inside: avoid;
}

/* Ensure publication entries stay together */
#cv-content > section > div > div[style*="margin-bottom: 20px"] {
    page-break-inside: avoid;
    break-inside: avoid;
}

/* Keep headings with their content */
#cv-content h2 {
    page-break-after: avoid;
    break-after: avoid;
    page-break-before: auto;
}

#cv-content h3 {
    page-break-after: avoid;
    break-after: avoid;
    page-break-before: auto;
}

/* Keep publication entries together - more specific selectors */
#cv-content #publications-content > div {
    page-break-inside: avoid;
    break-inside: avoid;
}

/* Keep list items together when possible */
#cv-content li {
    page-break-inside: avoid;
    break-inside: avoid;
}

#cv-content h1 {
    font-size: 20pt;
    margin-bottom: 20px;
    color: #8B0000;
    border-bottom: 3px solid #8B0000;
    padding-bottom: 10px;
    font-family: "Times New Roman", Times, serif;
    font-weight: bold;
}

#cv-content h2 {
    font-size: 15pt;
    margin-top: 30px;
    margin-bottom: 15px;
    color: #8B0000;
    border-bottom: 2px solid #8B0000;
    padding-bottom: 5px;
    font-family: "Times New Roman", Times, serif;
    font-weight: bold;
}

#cv-content h3 {
    font-size: 13pt;
    margin-top: 20px;
    margin-bottom: 10px;
    color: #333;
    font-family: "Times New Roman", Times, serif;
    font-weight: bold;
}

#cv-content ul {
    margin-left: 20px;
    margin-bottom: 15px;
    font-family: "Times New Roman", Times, serif;
}

#cv-content li {
    margin-bottom: 8px;
    font-family: "Times New Roman", Times, serif;
    page-break-inside: avoid;
    break-inside: avoid;
}

#cv-content p {
    font-family: "Times New Roman", Times, serif;
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
    page-break-inside: avoid;
    break-inside: avoid;
}

#cv-content .project-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
    flex-wrap: wrap;
    gap: 10px;
}

#cv-content .project-title {
    font-size: 13pt;
    font-weight: bold;
    color: #8B0000;
    margin: 0;
    font-family: "Times New Roman", Times, serif;
}

#cv-content .project-badges {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

#cv-content .badge {
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: bold;
}

#cv-content .badge-stars {
    background-color: #f1f8ff;
    color: #0366d6;
    border: 1px solid #c8e1ff;
}

#cv-content .badge-license {
    background-color: #f6f8fa;
    color: #586069;
    border: 1px solid #d1d5da;
}

#cv-content .project-description {
    margin-bottom: 10px;
    color: #333;
    line-height: 1.6;
}

#cv-content .project-links {
    margin-top: 10px;
}

#cv-content .project-link-text {
    margin-bottom: 8px;
    font-size: 14px;
    line-height: 1.6;
    color: #333;
}

#cv-content .project-link-text strong {
    color: #8B0000;
    margin-right: 5px;
}

#cv-content .project-link-text a {
    color: #007bff;
    text-decoration: none;
    word-break: break-all;
}

#cv-content .project-link-text a:hover {
    text-decoration: underline;
}

/* Style for project links imported from projects.md */
#cv-content .project-links {
    display: block;
    margin-top: 10px;
}

#cv-content .project-links a {
    display: block;
    margin-bottom: 5px;
    color: #007bff;
    text-decoration: none;
    word-break: break-all;
    font-size: 14px;
}

#cv-content .project-links a:hover {
    text-decoration: underline;
}

/* Hide images in CV */
#cv-content .project-image-container,
#cv-content .project-image,
#cv-content img.project-image {
    display: none !important;
}

#cv-content .profile-image {
    float: right;
    width: 150px;
    height: auto;
    max-height: 200px;
    border-radius: 8px;
    margin-left: 20px;
    margin-bottom: 20px;
    object-fit: contain;
    object-position: center;
    border: 2px solid #8B0000;
}

#cv-content .about-header {
    display: flex;
    align-items: flex-start;
    margin-bottom: 20px;
    page-break-inside: avoid;
    break-inside: avoid;
}

#cv-content .about-header h1 {
    flex: 1;
    margin-bottom: 0;
}

/* Hide interactive elements in CV */
#cv-content .view-toggle,
#cv-content button,
#cv-content script {
    display: none !important;
}

@media print {
    @page {
        margin: 15mm;
        size: A4;
    }
    
    /* Hide navigation and other non-content elements */
    .masthead,
    .page__footer,
    .sidebar,
    .cv-header,
    button,
    #download-cv-btn,
    .page__inner-wrap > header {
        display: none !important;
    }
    
    /* Show only CV content */
    #cv-content {
        padding: 0;
        max-width: 100%;
        margin: 0;
    }
    
    #cv-content section {
        page-break-inside: avoid;
        break-inside: avoid;
    }
    
    /* Stronger page break control for print */
    #cv-content .project-card,
    #cv-content .about-header,
    #cv-content [style*="margin-bottom: 20px"] {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    
    /* Keep publication entries together */
    #cv-content #publications-content > div[style*="margin-bottom"] {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    
    /* Prevent orphans and widows */
    #cv-content p,
    #cv-content li {
        orphans: 3;
        widows: 3;
    }
}
</style>
