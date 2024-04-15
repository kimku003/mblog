      $(document).ready(function () {
        $('.star').click(function () {
          var value = $(this).data('value')
          var postId = $(this).closest('.rating').data('post-id')
      
          var csrftoken = $('#csrf-token-form [name=csrfmiddlewaretoken]').val()
      
          $.ajax({
            url: '/like_post/',
            data: {
             'post_id': postId,
              'value': value,
              'csrfmiddlewaretoken': csrftoken // Ajoutez le token CSRF ici
            },
            type: 'POST',
            success: function (response) {
              // Mettez à jour le nombre de likes affiché
              $('.likes-count').text(response.likes)
            }
          })
        })
      })
