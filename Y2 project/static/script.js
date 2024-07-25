function updateAllCategories(imageUrls) {
  let categories = document.querySelectorAll('.category');
  categories.forEach(function(category, index) {
    let img = category.querySelector('img');
    img.src = imageUrls[index];
    img.alt = "Category " + (index + 1);
    // Optionally, update title and description as well
    // category.querySelector('h2').textContent = "New Title";
    // category.querySelector('p').textContent = "New Description";
  });
}
function navigateToIndex() {
  window.location.href = 'garden';
  }
// Function to handle click event and update all categories
function changeAllCategories(imageUrls) {
  updateAllCategories(imageUrls);
  navigateToIndex();
}