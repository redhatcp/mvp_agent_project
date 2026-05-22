export async function runAgent(name) {
  const res = await fetch("http://localhost:8000/api/run_agent", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ name })
  });
  return res.json();
}

export async function getTasks() {
  const res = await fetch("http://localhost:8000/api/tasks");
  return res.json();
}