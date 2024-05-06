$(document).ready(function() {
    $('#star').raty({
        score: 3, // Note initiale
        number: 5, // Nombre d'étoiles
        starOff: '{% static "mblog/images/star-off.png" %}',// Chemin vers l'image de l'étoile non sélectionnée
        starOn: '{% static "mblog/images/star-on.png" %}',// Chemin vers l'image de l'étoile sélectionnée

        click: function (score, evt) {
            $.ajax({
                url: '/like_post/',
                data: {
                    'post_id': '123', // Remplacez par l'ID de votre post
                    'value': score,
                    'csrfmiddlewaretoken': '{{ csrf_token }}'
                },
                type: 'POST',
                success: function(response) {
                    // Mettez à jour l'interface utilisateur si nécessaire
                }
            });
            // Fonction appelée lorsque l'utilisateur clique sur une étoile
            alert('Vous avez sélectionné ' + score + ' étoiles !');
        }
    });
});