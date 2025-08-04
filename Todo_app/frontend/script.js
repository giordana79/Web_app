const API_URL = "http://127.0.0.1:5000/todos";

const todoList = document.getElementById("todo-list");
const todoForm = document.getElementById("todo-form");
const taskInput = document.getElementById("task-input");

async function fetchTodos() {
  const res = await fetch(API_URL);
  const todos = await res.json();
  todoList.innerHTML = "";
  todos.forEach(addTodoToDOM);
}

function addTodoToDOM(todo) {
  const li = document.createElement("li");
  li.dataset.id = todo.id;
  if (todo.done) li.classList.add("done");

  const span = document.createElement("span");
  span.textContent = todo.task;
  span.style.cursor = "pointer";
  span.onclick = () => toggleDone(todo);

  const delBtn = document.createElement("button");
  delBtn.textContent = "Elimina";
  delBtn.onclick = () => deleteTodo(todo);

  li.appendChild(span);
  li.appendChild(delBtn);
  todoList.appendChild(li);
}

async function toggleDone(todo) {
  const updated = { done: !todo.done };
  await fetch(`${API_URL}/${todo.id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(updated),
  });
  fetchTodos();
}

async function deleteTodo(todo) {
  await fetch(`${API_URL}/${todo.id}`, {
    method: "DELETE",
  });
  fetchTodos();
}

todoForm.onsubmit = async (e) => {
  e.preventDefault();
  const task = taskInput.value.trim();
  if (!task) return;
  await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ task }),
  });
  taskInput.value = "";
  fetchTodos();
};

// Carica la lista all’avvio
fetchTodos();
