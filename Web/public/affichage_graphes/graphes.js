document.addEventListener('DOMContentLoaded', function() {
    const classSelect = document.getElementById('classSelect');
    const graphContainer = document.getElementById('graphContainer');
    const fullscreenBtn = document.getElementById('fullscreenBtn');

    classSelect.addEventListener('change', function() {
        const selectedClass = this.value;
        
        if (selectedClass) {
            const pdfUrl = `${selectedClass}.pdf`; // Utilise l'extension .pdf
            graphContainer.innerHTML = `<embed src="${pdfUrl}" type="application/pdf" width="100%" height="100%">`;
            fullscreenBtn.style.display = 'inline-block';
            fullscreenBtn.onclick = function() {
                window.open(pdfUrl, '_blank');
            };
        } else {
            graphContainer.innerHTML = '';
            fullscreenBtn.style.display = 'none';
        }
    });
});