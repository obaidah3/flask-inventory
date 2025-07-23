const selectedItems = new Map();

async function fetchSamples() {
  const res = await fetch('/sample_products');
  const data = await res.json();
  const container = document.getElementById('sampleItems');
  container.innerHTML = '';

  data.samples.forEach(prod => {
    const col = document.createElement('div');
    col.className = 'col';
    col.innerHTML = `
      <div class="card h-100">
        <div class="card-body">
          <h5 class="card-title">${prod.name}</h5>
          <p class="card-text">Price: $${prod.price} | Category: ${prod.category}</p>
          <button class="btn btn-primary" onclick='addItem(${JSON.stringify(prod)})'>Add</button>
        </div>
      </div>
    `;
    container.appendChild(col);
  });
}

function addItem(item) {
  if (!selectedItems.has(item.name)) {
    item.quantity = 1;
    selectedItems.set(item.name, item);
  } else {
    selectedItems.get(item.name).quantity++;
  }
  renderSelected();
}

function removeItem(name) {
  selectedItems.delete(name);
  renderSelected();
}

function changeQuantity(name, delta) {
  const item = selectedItems.get(name);
  item.quantity = Math.max(1, item.quantity + delta);
  renderSelected();
}

function renderSelected() {
  const list = document.getElementById('selectedItems');
  list.innerHTML = '';
  selectedItems.forEach(item => {
    const li = document.createElement('li');
    li.className = 'list-group-item d-flex justify-content-between align-items-center';
    li.innerHTML = `
      <div>
        <strong>${item.name}</strong> - $${item.price} (${item.category})
      </div>
      <div class="quantity-controls">
        <button class="btn btn-sm btn-outline-secondary" onclick="changeQuantity('${item.name}', -1)">−</button>
        <span>${item.quantity}</span>
        <button class="btn btn-sm btn-outline-secondary" onclick="changeQuantity('${item.name}', 1)">+</button>
        <button class="btn btn-sm btn-danger ms-2" onclick="removeItem('${item.name}')">Remove</button>
      </div>
    `;
    list.appendChild(li);
  });
}

document.getElementById('applyBtn').addEventListener('click', async () => {
  const items = Array.from(selectedItems.values());
const res = await fetch('/apply_quantity_update', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(items)
  });

  if (res.ok) {
    alert('Products applied successfully');
    selectedItems.clear();
    renderSelected();
    fetchProducts();
  } else {
    alert('Failed to apply products');
  }
});

async function fetchProducts() {
  const res = await fetch('/products');
  const data = await res.json();
  const tbody = document.getElementById('productTableBody');
  tbody.innerHTML = '';

  data.forEach(prod => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${prod.name}</td>
      <td>${prod.quantity}</td>
      <td>$${prod.price}</td>
      <td>${prod.category}</td>
      <td>${prod.created_at}</td>
    `;
    tbody.appendChild(row);
  });
}

// Run on load
fetchSamples();
fetchProducts();
