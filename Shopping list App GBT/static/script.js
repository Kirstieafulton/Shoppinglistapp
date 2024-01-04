document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.fa-trash-alt');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            if (!confirm('Are you sure you want to delete this item?')) {
                event.preventDefault();
            }
        });
    });
});
