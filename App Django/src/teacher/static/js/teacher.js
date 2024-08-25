function openModal() {
   document.getElementById('deleteModal').classList.remove('hidden');
}

function closeModal() {
   document.getElementById('deleteModal').classList.add('hidden');
}

function deleteItem() {
   // Logique de suppression ici
   alert('Élément supprimé');
   closeModal();
}
