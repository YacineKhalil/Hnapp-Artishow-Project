document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('searchForm');
    const loadingMessage = document.getElementById('loadingMessage');

    searchForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const query = (document.getElementById('searchInput') as HTMLInputElement).value;
    
        loadingMessage.style.display = 'block';

        fetch(`/rechercher?q=${query}`)    // URL à changer quand le serveur fait avec Flask (Daniel) sera opérationnel
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.error('Erreur lors de la récupération des données :', error);
            })
            .finally(() => {
                loadingMessage.style.display = 'none';
            });
    });
});