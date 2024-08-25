
         const ctx = document.getElementById('pieChart').getContext('2d');
         const pieChart = new Chart(ctx, {
            type: 'pie',
            data: {
               labels: ['Homme', 'Femme'],
               datasets: [
                  {
                     data: [60, 40], // Exemples de données
                     backgroundColor: ['#3498db', '#e74c3c'], // Couleurs pour Homme et Femme
                     borderWidth: 1,
                  },
               ],
            },
            options: {
               responsive: true,
               maintainAspectRatio: false,
               plugins: {
                  legend: {
                     display: false, // On désactive la légende intégrée pour utiliser la légende personnalisée
                  },
               },
            },
         });
      