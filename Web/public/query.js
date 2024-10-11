document.getElementById('searchForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const query = document.getElementById('searchInput').value;
    const category = document.getElementById('classSelect').value;

    const requestData = {
        query: query,
        category: category
    };

    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
    })
    .then(response => response.json())
    .then(data => {
        const resultsList = document.getElementById('resultsList');
        resultsList.innerHTML = '';
        const resultsIntro = document.getElementById('resultsIntro');
        resultsIntro.style.display = data.length > 0 ? 'block' : 'none';
        resultsIntro.textContent = data[0];

        if (data.length > 0) {
            (data.slice(1)).forEach(item => {
                const itemDiv = document.createElement('div');
                const parts = item.split(':');
                const nodeName = parts[0].trim();
                const relation = parts.length > 1 ? ': ' + parts.slice(1).join(':').trim() : '';

                const itemLink = document.createElement('a');
                itemLink.textContent = nodeName;
                itemLink.href = '#';
                itemLink.style.textDecoration = 'none';
                itemLink.style.color = 'inherit';
                itemLink.addEventListener('click', function(e) {
                    e.preventDefault();
                    searchWikidata(nodeName);
                });

                itemLink.addEventListener('mouseover', function(e) {
                    getWikipediaSummary(nodeName);
                });

                itemLink.addEventListener('mouseout', function() {
                    hideTooltip();
                });

                itemDiv.appendChild(itemLink);
                if (relation) {
                    itemDiv.appendChild(document.createTextNode(relation));
                }
                resultsList.appendChild(itemDiv);
            });
        } else {
            resultsList.textContent = 'Aucun résultat trouvé';
        }
    })
    .catch(error => console.error('Error:', error));
});

function searchWikidata(term) {
    const wikidataLoading = document.getElementById('wikidataLoading');
    wikidataLoading.style.display = 'block';

    const url = `https://www.wikidata.org/w/api.php?action=wbsearchentities&search=${encodeURIComponent(term)}&language=fr&format=json&origin=*`;
    
    fetch(url)
        .then(response => response.json())
        .then(data => {
            wikidataLoading.style.display = 'none';
            if (data.search && data.search.length > 0) {
                const entityId = data.search[0].id;
                window.open(`https://www.wikidata.org/wiki/${entityId}`, '_blank');
            } else {
                alert('Aucune correspondance trouvée sur Wikidata');
            }
        })
        .catch(error => {
            wikidataLoading.style.display = 'none';
            console.error('Erreur lors de la recherche Wikidata:', error);
            alert('Une erreur est survenue lors de la recherche sur Wikidata');
        });
}

function getWikipediaSummary(term) {
    const url = `https://fr.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(term)}`;
    
    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.extract) {
                showTooltip(data.extract);
            }
        })
        .catch(error => {
            console.error('Erreur lors de la récupération du résumé Wikipedia:', error);
        });
}

function showTooltip(content) {
    const tooltip = document.getElementById('tooltip');
    tooltip.textContent = content;
    tooltip.style.display = 'block';
    
    document.addEventListener('mousemove', moveTooltip);
}

function hideTooltip() {
    const tooltip = document.getElementById('tooltip');
    tooltip.style.display = 'none';
    
    document.removeEventListener('mousemove', moveTooltip);
}

function moveTooltip(e) {
    const tooltip = document.getElementById('tooltip');
    tooltip.style.left = (e.pageX + 10) + 'px';
    tooltip.style.top = (e.pageY + 10) + 'px';
}