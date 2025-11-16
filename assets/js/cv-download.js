// CV Download Function
console.log('CV download script loaded');

// Wait for libraries to load
function waitForLibraries(maxWait = 5000) {
    return new Promise((resolve, reject) => {
        const startTime = Date.now();
        const checkLibraries = () => {
            if (window.jspdf && window.html2canvas) {
                console.log('Libraries loaded successfully');
                resolve();
            } else if (Date.now() - startTime > maxWait) {
                console.error('Libraries failed to load:', {
                    jspdf: !!window.jspdf,
                    html2canvas: !!window.html2canvas
                });
                reject(new Error('Libraries failed to load within timeout'));
            } else {
                setTimeout(checkLibraries, 100);
            }
        };
        checkLibraries();
    });
}

// Download CV as PDF
window.downloadCV = async function downloadCV() {
    console.log('downloadCV function called');
    const button = document.getElementById('download-cv-btn');
    if (!button) {
        console.error('Download button not found');
        alert('Download button not found. Please refresh the page.');
        return;
    }
    
    const originalText = button.textContent;
    button.textContent = 'Generating PDF...';
    button.disabled = true;
    
    try {
        // Wait for libraries to load
        await waitForLibraries();
        
        // Check if libraries are loaded
        if (!window.jspdf || !window.html2canvas) {
            throw new Error('PDF generation libraries not loaded. Please refresh the page.');
        }
        
        const { jsPDF } = window.jspdf;
        const element = document.getElementById('cv-content');
        
        if (!element) {
            throw new Error('CV content not found');
        }
        
        // Hide the download button for PDF
        const downloadBtnContainer = button.parentElement;
        const originalDisplay = downloadBtnContainer ? downloadBtnContainer.style.display : '';
        if (downloadBtnContainer) {
            downloadBtnContainer.style.display = 'none';
        }
        
        // Ensure profile image is loaded
        const profileImg = document.getElementById('cv-profile-img');
        if (profileImg && !profileImg.complete) {
            await new Promise((resolve) => {
                profileImg.onload = resolve;
                profileImg.onerror = resolve;
                setTimeout(resolve, 2000);
            });
        }
        
        // Wait a bit for any dynamic content to render
        await new Promise(resolve => setTimeout(resolve, 500));
        
        // Add data attributes to elements that should not be split
        const nonBreakableElements = element.querySelectorAll('.project-card, .about-header, [style*="margin-bottom: 20px"]');
        nonBreakableElements.forEach(el => {
            el.setAttribute('data-no-break', 'true');
        });
        
        // Use html2canvas to capture the content with better page break handling
        const canvas = await html2canvas(element, {
            scale: 2,
            useCORS: true,
            logging: false,
            windowWidth: element.scrollWidth,
            windowHeight: element.scrollHeight,
            backgroundColor: '#ffffff',
            allowTaint: true,
            onclone: (clonedDoc) => {
                // Ensure all no-break elements are marked in the cloned document
                const clonedElement = clonedDoc.getElementById('cv-content');
                if (clonedElement) {
                    const clonedNonBreakable = clonedElement.querySelectorAll('[data-no-break="true"]');
                    clonedNonBreakable.forEach(el => {
                        el.style.pageBreakInside = 'avoid';
                        el.style.breakInside = 'avoid';
                    });
                }
            }
        });
        
        // Restore button
        if (downloadBtnContainer) {
            downloadBtnContainer.style.display = originalDisplay;
        }
        
        const imgData = canvas.toDataURL('image/png', 1.0');
        const pdf = new jsPDF('p', 'mm', 'a4');
        
        const pdfWidth = pdf.internal.pageSize.getWidth();
        const pdfHeight = pdf.internal.pageSize.getHeight();
        const imgWidth = canvas.width;
        const imgHeight = canvas.height;
        
        // Calculate dimensions to fit page width
        const ratio = pdfWidth / imgWidth;
        const imgScaledWidth = imgWidth * ratio;
        const imgScaledHeight = imgHeight * ratio;
        
        // Calculate page breaks more intelligently
        // Try to avoid cutting through important elements
        const pageHeightMM = pdfHeight;
        const pixelsPerMM = imgHeight / imgScaledHeight;
        const pageHeightPixels = pageHeightMM * pixelsPerMM;
        
        // Get positions of non-breakable elements
        const elementPositions = [];
        nonBreakableElements.forEach(el => {
            const rect = el.getBoundingClientRect();
            const elementTop = rect.top - element.getBoundingClientRect().top;
            const elementBottom = elementTop + rect.height;
            elementPositions.push({ top: elementTop, bottom: elementBottom });
        });
        
        // Add image to PDF with smart pagination
        let currentY = 0;
        let pageNum = 0;
        
        while (currentY < imgScaledHeight) {
            if (pageNum > 0) {
                pdf.addPage();
            }
            
            // Calculate how much content fits on this page
            let pageEndY = currentY + pageHeightMM;
            
            // Check if any non-breakable element would be cut
            for (const pos of elementPositions) {
                const elementTopMM = (pos.top / pixelsPerMM);
                const elementBottomMM = (pos.bottom / pixelsPerMM);
                const elementTopPage = elementTopMM - currentY;
                const elementBottomPage = elementBottomMM - currentY;
                
                // If element starts on this page but doesn't fit, move it to next page
                if (elementTopPage >= 0 && elementTopPage < pageHeightMM && elementBottomPage > pageHeightMM) {
                    // Move the page break before this element
                    pageEndY = Math.min(pageEndY, elementTopMM - 5); // Add 5mm margin
                    break;
                }
            }
            
            // Calculate the source Y position and height for this page
            const sourceY = (currentY / pageHeightMM) * imgHeight;
            const pageHeightPx = ((pageEndY - currentY) / pageHeightMM) * imgHeight;
            const destY = 0;
            const destHeight = pageEndY - currentY;
            
            // Create a temporary canvas for this page
            const pageCanvas = document.createElement('canvas');
            pageCanvas.width = imgWidth;
            pageCanvas.height = pageHeightPx;
            const pageCtx = pageCanvas.getContext('2d');
            pageCtx.drawImage(canvas, 0, sourceY, imgWidth, pageHeightPx, 0, 0, imgWidth, pageHeightPx);
            
            const pageImgData = pageCanvas.toDataURL('image/png', 1.0');
            pdf.addImage(pageImgData, 'PNG', 0, destY, imgScaledWidth, destHeight);
            
            currentY = pageEndY;
            pageNum++;
        }
        
        pdf.save('Size_Zheng_CV.pdf');
        console.log('PDF saved successfully');
        
        button.textContent = originalText;
        button.disabled = false;
    } catch (error) {
        console.error('Error generating PDF:', error);
        console.error('Error stack:', error.stack);
        
        // Restore button display in case of error
        const downloadBtnContainer = button.parentElement;
        if (downloadBtnContainer) {
            downloadBtnContainer.style.display = '';
        }
        
        alert('Error generating PDF: ' + error.message + '\n\nPlease try again or use the browser\'s print function (Ctrl+P / Cmd+P) to save as PDF.');
        button.textContent = originalText;
        button.disabled = false;
    }
};

console.log('downloadCV function defined:', typeof window.downloadCV);

